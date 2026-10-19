

# Generated at 2022-06-14 11:50:15.821325
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = asyncio.Future()
    assert not f.cancelled()
    f.cancel()
    assert f.cancelled()
    future_set_exception_unless_cancelled(f, ValueError())

# Generated at 2022-06-14 11:50:22.569693
# Unit test for function chain_future
def test_chain_future():
    f1, f2 = concurrent.futures.Future(), Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42

    f1, f2 = Future(), concurrent.futures.Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42

    # This tests that chain_future doesn't put the output future into an
    # invalid state if the input finishes with an exception.  It's hard to
    # make this test robust because we're testing code in different
    # threads, so the test may pass even if the bug remains.  But it's
    # better than nothing.
    f1, f2 = Future(), concurrent.futures.Future()
    chain_

# Generated at 2022-06-14 11:50:26.064376
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from tornado.ioloop import IOLoop
    from tornado.gen import coroutine, Return

    @coroutine
    def func():
        raise Return(1)

    assert func.__name__ == "func"
    assert func.__qualname__ == "test_DummyExecutor_submit.<locals>.func"

    @coroutine
    def test():
        loop = IOLoop.current()
        assert isinstance(loop, IOLoop)
        res = yield dummy_executor.submit(func)
        assert res == 1

    IOLoop.current().run_sync(test)

# Generated at 2022-06-14 11:50:34.511876
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest.mock
    from tornado.testing import AsyncTestCase, gen_test

    class Test(AsyncTestCase):
        @run_on_executor
        def function(self):
            return 42

        async def async_function(self):
            return await self.function()

        def test_function(self):
            result = yield self.async_function()
            self.assertEqual(result, 42)

        @unittest.mock.patch("tornado.concurrent.run_on_executor.executor")
        def test_executor(self, executor: unittest.mock.Mock) -> None:
            result = yield self.async_function()
            self.assertEqual(executor.submit.call_count, 1)

# Generated at 2022-06-14 11:50:36.513182
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, "ok")
    assert future.result() == "ok"

# Generated at 2022-06-14 11:50:46.529586
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop
    import functools

    io_loop = IOLoop()

    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()

    io_loop.add_callback(functools.partial(a.set_result, 1))
    io_loop.add_timeout(io_loop.time(), io_loop.stop)
    io_loop.start()
    assert b.result() == 1

    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()
    io_loop.add_callback(lambda: a.set_exception(ValueError()))
    io_loop.add_timeout(io_loop.time(), io_loop.stop)
    io_loop

# Generated at 2022-06-14 11:51:00.087305
# Unit test for function chain_future
def test_chain_future():
    import unittest.mock

    def future_convert(future: Future) -> futures.Future:
        # Convert an asyncio Future to a concurrent.futures Future.
        # The resulting future has the same interface as the old Future
        # but is basically useless since it will never invoke its callbacks
        f = futures.Future()
        chain_future(future, f)
        return f

    f1 = Future()
    f2 = future_convert(f1)
    mock_handler = unittest.mock.Mock()
    f2.add_done_callback(mock_handler)
    f1.set_result(42)
    assert f2.result() == 42
    assert mock_handler.call_args[0][0].result() == 42

# Generated at 2022-06-14 11:51:06.034209
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    exc = Exception()
    future = Future()
    future_set_exception_unless_cancelled(future, exc)
    assert future.exception() is exc

    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, exc)
    assert future.exception() is None

# Generated at 2022-06-14 11:51:16.277923
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    a = Future()  # type: Any
    b = Future()  # type: Any
    chain_future(a, b)

    a.set_result(42)
    assert 42 == b.result()

    a = Future()  # type: Any
    b = Future()  # type: Any
    chain_future(b, a)

    a.set_result(42)
    assert 42 == b.result()

    a = Future()  # type: Any
    b = Future()  # type: Any
    chain_future(b, a)
    a.set_result(42)
    b.cancel()
    assert 42 == a.result()
    assert not b.cancelled()

    a = Future()  # type: Any
    b = Future()  # type: Any

# Generated at 2022-06-14 11:51:20.162304
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import logging
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, ValueError("this should log"))
    logger = logging.getLogger()
    assert any(map(lambda r: "this should log" in r.msg, logger.handlers[0].records))
    # Ensure everything is back to the way it was.
    logger.handlers[0].records.clear()

# Generated at 2022-06-14 11:51:29.763608
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    async def test_futures(future):
        return future

    future = test_futures(asyncio.Future())
    future.set_result("")
    assert future_set_exception_unless_cancelled(future, None) is None

    future = test_futures(asyncio.Future())
    future.set_exception(asyncio.CancelledError())
    assert future_set_exception_unless_cancelled(future, None) is None

# Generated at 2022-06-14 11:51:37.952707
# Unit test for function chain_future
def test_chain_future():
    from concurrent import futures
    from tornado.ioloop import IOLoop

    executor = futures.ThreadPoolExecutor(1)
    io_loop = IOLoop.current()
    f1 = executor.submit(lambda: 1)
    f2 = Future()
    chain_future(f1, f2)
    assert f2.result() == 1
    f3 = Future()
    chain_future(f2, f3)
    assert f3.result() == 1

    f4 = Future()
    f5 = Future()
    chain_future(f4, f5)
    f4.set_exception(RuntimeError())
    test_future = Future()
    f5.add_done_callback(lambda f5: io_loop.add_callback(lambda: test_future.set_result(f5)))
   

# Generated at 2022-06-14 11:51:40.783706
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    assert b.result() == 42



# Generated at 2022-06-14 11:51:51.757616
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    c = Future()
    chain_future(a, b)
    a.set_result(1)
    assert 1 == b.result()
    a = Future()
    b = Future()
    c = Future()
    chain_future(a, b)
    try:
        1 / 0
    except ZeroDivisionError:
        exc_info = sys.exc_info()
    a.set_exc_info(exc_info)
    assert exc_info[1] is b.exception()
    a = Future()
    b = Future()
    c = Future()
    chain_future(a, b)
    a.cancel()
    assert b.cancelled()

# Generated at 2022-06-14 11:52:00.271346
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    loop = asyncio.get_event_loop()
    async_future = Future()  # type: Future
    conc_future = futures.Future()  # type: futures.Future

    def set_result(_, future):
        # type: (None, Future) -> None
        future.set_result(1)

    def set_concurrent_result(_):
        # type: (None) -> None
        assert not conc_future.done()
        conc_future.set_result(1)

    loop.call_soon(set_concurrent_result, None)
    chain_future(conc_future, async_future)
    loop.run_until_complete(async_future)

    assert async_future.result() == 1
    assert conc_future.result() == 1

    # Check that

# Generated at 2022-06-14 11:52:07.452951
# Unit test for function chain_future
def test_chain_future():
    from tornado import gen
    from tornado.testing import AsyncTestCase, gen_test

    class MyTest(AsyncTestCase):
        def setUp(self):
            super(MyTest, self).setUp()
            self.executor = futures.ThreadPoolExecutor(1)
            self.io_loop.add_callback(
                lambda: self.stop(gen.moment)  # type: ignore
            )
            self.wait()

        @gen_test
        def test_chain_future(self):
            # type: () -> None
            a = gen.Future()
            b = gen.Future()
            chain_future(a, b)
            self.executor.submit(lambda: a.set_result(42))

# Generated at 2022-06-14 11:52:18.711626
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    class MyTask(asyncio.Task):
        def __init__(self, loop, default_exc=None, *args, **kwargs):
            super(MyTask, self).__init__(loop, *args, **kwargs)
            self.default_exc = default_exc

        def get_stack(self):
            return list(self._source_traceback)
    future = MyTask(loop=asyncio.get_event_loop())
    exc = RuntimeError('123')
    future_set_exception_unless_cancelled(future, exc)
    try:
        future.result()
    except RuntimeError as e:
        assert e.args == exc.args
    # Cancelled task with default exception

# Generated at 2022-06-14 11:52:32.154260
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def check_future(future, type, value):
        # type: (Future, str, Any) -> None
        assert future.done()
        assert type == "success" or type == "exception"
        if type == "exception":
            assert "Exception" in str(value)
        else:
            assert value == 1

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    f1 = Future()  # type: Future
    f2 = Future()  # type: Future
    chain_future(f1, f2)
    # f1 success
    f1.set_result(1)
    loop.run_until_complete(f2)
    check_future(f2, "success", f2.result())

    f1

# Generated at 2022-06-14 11:52:38.767181
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    def callback(future):
        raise Exception("callback should not be invoked")

    future = Future()
    future.add_done_callback(callback)
    exc_info = (None, Exception(), None)
    future_set_exc_info(future, exc_info)
    try:
        future.result()
        assert False
    except Exception as e:
        assert isinstance(e, Exception)

    future = Future()
    future.add_done_callback(callback)
    future.cancel()
    future_set_exc_info(future, exc_info)
    assert future.done()
    assert not future.cancelled()

# Generated at 2022-06-14 11:52:45.003571
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.cancel()
    future_set_exc_info(future, sys.exc_info())
    assert future.exception() is None
    future = Future()
    future_set_exc_info(future, sys.exc_info())
    assert isinstance(future.exception(), ZeroDivisionError)

# Generated at 2022-06-14 11:53:05.591305
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing
    import tornado.ioloop

    class F(Future):
        def __init__(self):
            super().__init__()
            self.callbacks = []

        def add_done_callback(self, callback):
            self.callbacks.append(callback)

        def set_result(self, value):
            super().set_result(value)
            # We need to do this explicitly in our test, but Future does it
            # for us in real life.
            for cb in self.callbacks:
                cb(self)

        def set_exception(self, value):
            super().set_exception(value)
            for cb in self.callbacks:
                cb(self)

    @tornado.testing.gen_test
    def f():
        f1 = F()
       

# Generated at 2022-06-14 11:53:08.428084
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, RuntimeError('foo'))



# Generated at 2022-06-14 11:53:19.886263
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase

    def make_future(value):
        future = Future()
        future_set_result_unless_cancelled(future, value)
        return future

    @gen_test
    def f():
        a = make_future(42)
        # This future (b) won't be used, but should still be correctly cancelled:
        b = Future()
        chain_future(a, b)
        self.assertEqual(b.result(), 42)
        self.assertEqual(a.result(), 42)

    AsyncTestCase().run_sync(f)



# Generated at 2022-06-14 11:53:21.837425
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    import pytest

    def foo():
        pass
    dummy_executor.submit(foo)

# Generated at 2022-06-14 11:53:33.426289
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import contextlib
    import sys

    future = Future()
    future.cancel()

    # If this test doesn't crash, it passes.
    future_set_exception_unless_cancelled(future, ZeroDivisionError())

    @contextlib.contextmanager
    def capture_exception() -> typing.Iterator[BaseException]:
        try:
            yield None
        except Exception as e:
            return e

    exc = capture_exception()
    future_set_exception_unless_cancelled(future, ZeroDivisionError())
    assert exc is None

    exc = capture_exception()
    future_set_exception_unless_cancelled(future, ZeroDivisionError())
    assert isinstance(exc, ZeroDivisionError)

# Generated at 2022-06-14 11:53:40.532955
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, ValueError())
    assert future.exception() is not None
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError())
    assert future.exception() is None  # future should still be cancelled
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError())
    assert future.exception() is None  # future should still be cancelled

# Generated at 2022-06-14 11:53:49.117373
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    loop = asyncio.get_event_loop()
    f = Future()  # type: Future[None]

    @asyncio.coroutine
    def setter():
        f.set_result(None)

    asyncio.ensure_future(setter(), loop=loop)
    g = Future()  # type: Future[None]
    chain_future(f, g)
    assert g.done()



# Generated at 2022-06-14 11:53:56.639756
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    if not future.cancelled():
        future_set_exc_info(future, sys.exc_info())
    assert not future.cancelled()
    assert future.exception() is not None
    future = Future()
    future.cancel()
    future_set_exc_info(future, sys.exc_info())
    assert future.cancelled()
    assert future.exception() is None


__all__ = [
    "Future",
    "ReturnValueIgnoredError",
    "dummy_executor",
    "is_future",
    "chain_future",
    "run_on_executor",
]

# Generated at 2022-06-14 11:54:09.481187
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    g = Future()
    # Set f's result; g should also become done.
    chain_future(f, g)
    f.set_result(None)
    assert g.done()
    # Set f's exception; g should also become done.
    f2 = Future()
    g2 = Future()
    chain_future(f2, g2)
    f2.set_exception(ValueError())
    assert g2.done()
    try:
        g2.result()
    except ValueError:
        pass
    else:
        assert 0, "did not propagate exception"
    # Cancel f; g should also become cancelled.
    f3 = Future()
    g3 = Future()
    chain_future(f3, g3)
    f3.cancel()
    assert g3

# Generated at 2022-06-14 11:54:16.835006
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import random
    import unittest
    import functools
    import typing

    from tornado.ioloop import IOLoop

    if sys.version_info < (3, 5):
        raise unittest.SkipTest("asyncio.Future was added in Python 3.5")

    async def f():
        # type: () -> int
        await asyncio.sleep(random.random())
        return 42

    def callback(future):
        # type: (Future[int]) -> None
        IOLoop.current().stop()
        assert future.result() == 42

    async_future = f()
    conc_future = asyncio.run_coroutine_threadsafe(async_future, IOLoop.current().asyncio_loop)

# Generated at 2022-06-14 11:54:47.008362
# Unit test for function chain_future

# Generated at 2022-06-14 11:54:49.651294
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f: Future[int] = Future()
    with f:
        future_set_exception_unless_cancelled(f, Exception())

# Generated at 2022-06-14 11:55:00.225726
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import concurrent.futures
    import functools
    import tornado.ioloop
    import tornado.testing

    @tornado.testing.gen_test
    def f():
        # type: () -> None

        e = dummy_executor
        f1 = e.submit(lambda: 1 + 2)
        f2 = Future()
        chain_future(f1, f2)

        res = yield f2
        assert res == 3

        f3 = e.submit(
            lambda: 3 / 0
        )  # type: ignore  # function don't take parameters
        f4 = Future()
        chain_future(f3, f4)

        try:
            yield f4
            assert False  # shouldn't reach here
        except ZeroDivisionError:
            pass

        f5 = e

# Generated at 2022-06-14 11:55:07.448125
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f1 = Future()
    f2 = Future()
    future_set_result_unless_cancelled(f1, 2)
    future_set_result_unless_cancelled(f2, 3)
    f1.cancel()
    assert f1.cancelled()
    assert f2.result() == 3



# Generated at 2022-06-14 11:55:18.593906
# Unit test for function chain_future
def test_chain_future():
    logging.basicConfig()
    f = Future()
    f2 = Future()

    @gen.coroutine
    def f1():
        yield gen.moment
        raise Exception("test")

    def f3(fut):
        fut.set_result(3)

    chain_future(f1(), f)
    chain_future(f, f2)
    f2.add_done_callback(f3)

    IOLoop.current().run_sync(f2)
    assert(f2.result() == 3)



# Generated at 2022-06-14 11:55:22.410983
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    # Avoid setting an exception directly, save the
    # InvalidStateError exception.
    f.set_exception(Exception("error"))
    future_set_exception_unless_cancelled(f, Exception("cancelled"))

# Generated at 2022-06-14 11:55:27.650405
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    print("test_DummyExecutor_submit():")

    def test_func(x, y):
        return x + y

    fut = dummy_executor.submit(test_func, 2, 3)
    assert fut.result() == 5

# Generated at 2022-06-14 11:55:37.080531
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import unittest
    from tornado import gen
    from tornado import ioloop

    class Test(unittest.TestCase):
        def is_future_cancellation_logged(self):
            # Check if a future cancelled before error occur will log its exception
            future = Future()
            future.cancel()
            try:
                future_set_exception_unless_cancelled(future, ValueError())
            except ValueError:
                self.fail()

            io_loop = ioloop.IOLoop.instance()
            io_loop.make_current()
            io_loop.clear_current()

            self.assertIsNotNone(io_loop._exception_handler.exception)

# Generated at 2022-06-14 11:55:48.601022
# Unit test for function chain_future
def test_chain_future():
    import itertools
    import weakref
    import unittest

    from tornado.testing import AsyncTestCase, gen_test, main

    class TestFuture(Future):
        def __init__(self, *args, **kwargs):
            super(TestFuture, self).__init__(*args, **kwargs)
            self.callbacks = []  # type: List[Tuple[Callable, Future]]

        def add_done_callback(self, callback):
            self.callbacks.append((callback, None))  # type: ignore

        def add_done_callback_with_future(self, callback, future):
            self.callbacks.append((callback, future))  # type: ignore

    class TestFuture2(TestFuture):
        pass


# Generated at 2022-06-14 11:55:57.968080
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42

    f3 = Future()
    f4 = Future()
    chain_future(f3, f4)
    f3.set_exception(ZeroDivisionError())
    # Using assertRaises here doesn't work because the exception isn't raised
    # until the next IOLoop iteration.
    f4.add_done_callback(lambda f: f.exception())
    return f4

# Generated at 2022-06-14 11:56:43.362035
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import tornado.testing
    import tornado.platform.asyncio

    class RunOnExecutorTest(unittest.TestCase):
        def setUp(self):
            super(RunOnExecutorTest, self).setUp()
            self.io_loop = tornado.platform.asyncio.AsyncIOMainLoop()
            self.io_loop.make_current()

            self.executor = futures.ThreadPoolExecutor(1)
            self.executor_fn_was_run = False
            self.fut = asyncio.Future()

        def tearDown(self):
            self.io_loop.clear_current()
            self.io_loop.close(all_fds=True)
            super(RunOnExecutorTest, self).tearDown()


# Generated at 2022-06-14 11:56:46.661040
# Unit test for function chain_future
def test_chain_future():
    async def async_main():
        future1 = futures.Future()
        future2 = Future()
        chain_future(future1, future2)
        future1.set_result(42)
        result = await future2
        return result
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(async_main())
    loop.close()
    assert result == 42



# Generated at 2022-06-14 11:56:54.418617
# Unit test for function chain_future
def test_chain_future():
    asynchronous = futures.Future()
    synchronous = futures.Future()
    chain_future(synchronous, asynchronous)
    assert not asynchronous.done()
    synchronous.set_result(42)
    assert asynchronous.done()
    assert asynchronous.result() == 42
    asynchronous = Future()
    synchronous = Future()
    chain_future(synchronous, asynchronous)
    assert not asynchronous.done()
    synchronous.set_result(42)
    assert asynchronous.done()
    assert asynchronous.result() == 42

# Generated at 2022-06-14 11:57:00.882667
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import unittest
    import tornado.testing

    class ChainFutureTest(unittest.TestCase):
        def test_chain(self):
            # type: () -> None
                b = Future()
                a = Future()
                chain_future(a, b)
                a.set_result(42)
                self.assertEqual(b.result(), 42)

                b = Future()
                a = Future()
                chain_future(a, b)
                a.set_exception(RuntimeError("hello"))
                self.assertEqual(str(b.exception()), "hello")

                b = Future()
                a = Future()
                chain_future(a, b)

                ex = None

# Generated at 2022-06-14 11:57:04.448369
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    try:
        raise RuntimeError("blah")
    except Exception as e:
        exc_info = e

    future_set_exception_unless_cancelled(future, exc_info)
    assert not future.done()
    assert not future.cancelled()
    result = future.result()
    assert False



# Generated at 2022-06-14 11:57:12.934452
# Unit test for function chain_future
def test_chain_future():
    def check_result(result):
        if result != 5:
            raise Exception("Bad result: %r" % result)

    f = concurrent.futures.Future()
    g = Future()
    chain_future(f, g)
    f.set_result(5)
    g.add_done_callback(check_result)

# Generated at 2022-06-14 11:57:20.539358
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()

    # test_exc is not used during the test: it's just a convenient way of
    # creating an exception with a unique __repr__ value.
    test_exc = Exception("test")
    exc = None

    def cb(f): nonlocal exc; exc = f.exception()

    f.add_done_callback(cb)

    future_set_exc_info(f, (None, test_exc, None))
    assert exc is None

    excinfo = (None, test_exc, None)
    future_set_exc_info(f, excinfo)
    assert exc is None


if __name__ == "__main__":
    import unittest
    unittest.main()

# Generated at 2022-06-14 11:57:34.289295
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future_success = Future()
    future_success.cancel()
    future_set_result_unless_cancelled(future_success, "works")
    assert not future_success.done()
    assert not future_success.running()
    assert future_success.cancelled()

    future_cancelled = Future()
    future_set_result_unless_cancelled(future_cancelled, "works")
    assert future_cancelled.done()
    assert not future_cancelled.running()
    assert not future_cancelled.cancelled()
    assert future_cancelled.result() == "works"

    future_failed = Future()
    future_failed.set_exception(ValueError("error"))
    future_set_result_unless_cancelled(future_failed, "works")


# Generated at 2022-06-14 11:57:47.181993
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import functools


    class FutureTest(unittest.TestCase):
        def setUp(self):
            self.io_loop = IOLoop()
            self.future = Future()

        def future_set_result_unless_cancelled_helper(
            self, value: Any, result: Any, cancelled=False
        ) -> None:
            future = Future()
            if cancelled:
                future.cancel()
            future_set_result_unless_cancelled(future, value)
            self.assertEqual(result, future.result())

        def test_future_set_result_unless_cancelled(self) -> None:
            value = object()

# Generated at 2022-06-14 11:57:57.734434
# Unit test for method submit of class DummyExecutor

# Generated at 2022-06-14 11:59:22.343711
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = asyncio.Future()
    future_set_result_unless_cancelled(future, 'value')
    assert future.result() == 'value'
    future = asyncio.Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 'value')
    assert future.cancelled()

# Generated at 2022-06-14 11:59:28.328899
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.cancel()

    # future_set_exception_unless_cancelled should not reraise
    future_set_exception_unless_cancelled(future, ValueError("test"))
    future_set_exception_unless_cancelled(future, ValueError("test"))

    # future.exception should return the last unrarefied exception
    assert isinstance(future.exception(), ValueError)

# Generated at 2022-06-14 11:59:34.628476
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class TestCase(AsyncTestCase):

        @gen_test
        def test_chain_future(self):

            a = Future()
            b = Future()
            chain_future(a, b)
            a.set_result(42)
            self.assertEqual(b.result(), 42)

# Generated at 2022-06-14 11:59:45.158922
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    asyncio_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(asyncio_loop)
    try:
        import concurrent.futures
    except ImportError:
        raise unittest.SkipTest("futures module not available")
    import tornado.ioloop
    import tornado.testing
    import tornado.platform.asyncio
    tornado.platform.asyncio.AsyncIOMainLoop().install()

    def double(n):
        # type: (int) -> int
        return n * 2

    def err(n, exc):
        # type: (int, Exception) -> int
        raise exc

    f = Future()
    # Success.
    f2 = Future()
    chain_future(f, f2)
    f.set_

# Generated at 2022-06-14 11:59:50.729719
# Unit test for function chain_future
def test_chain_future():
    try:
        import unittest2 as unittest  # type: ignore
    except ImportError:
        import unittest  # type: ignore
    f = Future()
    f2 = Future()
    chain_future(f, f2)
    f.set_result(None)
    f2.result()



# Generated at 2022-06-14 12:00:01.295389
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    i = [0]
    fut1 = Future()
    fut2 = Future()
    fut3 = Future()
    fut4 = Future()

    fut1.add_done_callback(lambda f: i.__setitem__(0, i[0] + 1))
    fut2.add_done_callback(lambda f: i.__setitem__(0, i[0] + 1))
    fut3.add_done_callback(lambda f: i.__setitem__(0, i[0] + 1))
    fut4.add_done_callback(lambda f: i.__setitem__(0, i[0] + 1))

    assert not fut1.done()
    assert not fut2.done()
    assert not fut3.done()
    assert not fut4.done()


# Generated at 2022-06-14 12:00:12.768636
# Unit test for function chain_future
def test_chain_future():
    def copy(source, target):
        assert source is a
        if target.done():
            return
        if source.exc_info() is not None:
            target.set_exc_info(source.exc_info())
        elif source.exception() is not None:
            target.set_exception(source.exception())
        else:
            target.set_result(source.result())

    a = Future()
    b = Future()
    copy(a, b)
    assert not a.done()
    assert not b.done()
    a.set_result(42)
    assert a.done()
    assert b.done()
    assert b.result() == 42
