

# Generated at 2022-06-14 11:50:21.117060
# Unit test for function run_on_executor
def test_run_on_executor():
    check_error_async = None  # type: typing.Optional[Callable]
    if hasattr(asyncio, "run_coroutine_threadsafe"):
        # asyncio.run_coroutine_threadsafe is new in 3.4.4
        # unit test with tornado.testing.asyncio_test
        async def check_error_async(future: "Future[_T]") -> Any:
            return future.result()
    else:
        def check_error_async(future: "Future[_T]") -> Any:
            # asyncio.get_event_loop().run_until_complete
            return future.result()

    @run_on_executor(executor="_thread_pool")
    def test(self, arg):
        raise ReturnValueIgnoredError()


# Generated at 2022-06-14 11:50:23.475384
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42
    f1 = Future()
    f1.set_exception(ValueError())
    with pytest.raises(ValueError):
        f1.result()  # type: ignore

# Generated at 2022-06-14 11:50:27.343366
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import unittest

    class FutureSetExceptionTest(unittest.TestCase):
        def setUp(self):
            import logging
            from tornado.log import gen_log
            from tornado.platform.asyncio import AsyncIOMainLoop

            self.io_loop = AsyncIOMainLoop()
            self.io_loop.make_current()
            self.log_obs = []  # type: List[Tuple[int, str]]

            def log_observer(logger, level, msg, args, kwargs, exc_info=None):
                self.log_obs.append((level, msg))

            logging.root.addHandler(logging.StreamHandler())
            gen_log.add_observer(log_observer)


# Generated at 2022-06-14 11:50:33.492368
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()

    def check_f2(f3):
        assert f2.done()
        assert f3 is f1
        assert not f2.cancelled()

    chain_future(f1, f2)
    f1.set_result(None)
    future_add_done_callback(f2, check_f2)

# Generated at 2022-06-14 11:50:44.889234
# Unit test for function chain_future
def test_chain_future():
    success_expected = False
    failure_expected = False
    failure = None

    def fail():
        raise Exception("should not be reached")

    def handle_result(f: Future) -> None:
        nonlocal success_expected, failure_expected, failure
        if failure_expected:
            failure = f.exception()
        elif not success_expected:
            fail()
        success_expected = False

    def handle_exception(f: Future) -> None:
        nonlocal success_expected, failure_expected, failure
        if success_expected:
            failure = f.exception()
        elif not failure_expected:
            fail()
        failure_expected = False

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

# Generated at 2022-06-14 11:50:59.196477
# Unit test for function chain_future
def test_chain_future():
    def callback(future):
        future.callback_called = True

    f1 = Future()
    f2 = Future()

    # If f1 is already done, f2 should be called immediately
    f2.callback_called = False
    chain_future(f1, f2)
    assert not f2.callback_called
    f1.set_result(None)
    assert f2.callback_called

    # Even if f2 is already done, f2 should still be called
    f1.callback_called = False
    chain_future(f1, f2)
    assert not f1.callback_called
    f2.set_result(None)
    assert f1.callback_called

    # f2 should always be called, even if f1 raises an exception
    f1.callback_called = False

# Generated at 2022-06-14 11:51:04.332530
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.platform.asyncio import to_asyncio_future

    class Foo:
        def __init__(self):
            self.executor = futures.ThreadPoolExecutor(1)

        @run_on_executor
        def foo(self, a, b, callback=None):
            return a + b

    f = Foo()
    future = to_asyncio_future(f.foo(1, 2))
    assert future.result() == 3

# Generated at 2022-06-14 11:51:13.321558
# Unit test for function chain_future
def test_chain_future():
    # Make sure that this compiles (see #4458).  This test does not run
    # in isolation, but if it does not compile, it will fail the
    # `tornado.test.gen_test` suite, which imports this module.
    from tornado.ioloop import IOLoop

    future1 = Future()
    future2 = Future()
    future3 = IOLoop().run_in_executor(None, lambda: None)  # type: Future[None]
    chain_future(future1, future2)
    chain_future(future2, future3)

# Generated at 2022-06-14 11:51:20.574388
# Unit test for function chain_future
def test_chain_future():
    import logging
    import unittest

    from tornado.httpclient import AsyncHTTPClient
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncHTTPTestCase, gen_test, bind_unused_port

    class MyTestCase(AsyncHTTPTestCase):
        def test_chain(self):
            f = Future()

            async def async_test():
                await f

            IOLoop.current().add_callback(async_test)
            chain_future(f, self.stop())
            self.wait()

        @gen_test
        def test_chain_future(self):
            # Use bind_unused_port to bind a port to the future.
            # If the Future is copied, the port will still be free
            # and the test is guaranteed to fail.
            sock, port = bind_un

# Generated at 2022-06-14 11:51:31.757000
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop.current()
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_result(42)
    yield g
    assert g.result() == 42
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_exception(ZeroDivisionError())
    yield g
    assert isinstance(g.exception(), ZeroDivisionError)
    f = Future()
    g = Future()
    chain_future(f, g)
    f.cancel()
    io_loop.add_future(f, lambda _: None)
    yield g
    assert g.cancelled()

# Generated at 2022-06-14 11:51:46.709686
# Unit test for function chain_future
def test_chain_future():
    import time

    f1 = Future()
    f2 = Future()

    chain_future(f1, f2)
    assert not f2.done()

    f1.set_result(None)
    assert f2.done()

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    def f2_cancel():
        time.sleep(0.01)
        f2.cancel()

    IOLoop.current().add_callback(f2_cancel)
    f1.set_result(None)
    assert f2.cancelled()

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    def f2_set_result():
        time.sleep(0.01)
        f2

# Generated at 2022-06-14 11:51:55.304175
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert f1.done() is False
    assert f2.done() is False
    f1.set_result(1)
    assert f1.result() == f2.result() == 1
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert f1.done() is False
    assert f2.done() is False
    f1.set_exception(KeyError)
    assert f1.exception() is f2.exception() is KeyError


# Tests for function future_set_exc_info

# Generated at 2022-06-14 11:52:03.266221
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_result(None)
    assert future2.done()
    assert future2.result() is None


if asyncio.Future is Future:
    # Python 3.5 or newer
    # Only use add_done_callback, which is the "official" API.
    # Note that callback registration is not currently per-future in asyncio.
    # (they are registered globally)
    if hasattr(asyncio.Future, "add_done_callback"):
        def future_add_done_callback(  # noqa: F811
            future: "Future[_T]", callback: Callable[["Future[_T]"], None]
        ) -> None:
            future.add_done_callback(callback)



# Generated at 2022-06-14 11:52:07.531570
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    class MyException(Exception):
        pass
    future = futures.Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, MyException())

# Generated at 2022-06-14 11:52:13.733576
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from concurrent.futures import Future

    class WaitFuture(Future):
        def result(self):
            return super().result()

    def get_result(future: WaitFuture) -> int:
        return future.result()

    future = WaitFuture()
    future.set_result(42)

    assert get_result(future) == 42
    assert dummy_executor.submit(get_result, future) == 42



# Generated at 2022-06-14 11:52:17.032197
# Unit test for function chain_future
def test_chain_future():
    a, b = futures.Future(), futures.Future()

    async def test_chain():
        await a
        assert b.done()

    chain_future(a, b)
    IOLoop.current().run_sync(test_chain)

# Generated at 2022-06-14 11:52:22.373158
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()
    try:
        f.set_exception(ValueError())
        self.fail()
    except asyncio.InvalidStateError:
        pass
    future_set_exc_info(f, (ValueError, ValueError(), None))


if hasattr(asyncio.Future, "version_info"):
    # Python 3.6 or newer
    Future.__await__ = lambda future: future.__await__()

Future.add_done_callback = future_add_done_callback

# Generated at 2022-06-14 11:52:30.284052
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    @future_set_result_unless_cancelled
    def test_future(future: "Future[_T]", value: _T) -> None:
        pass
    f = Future()
    f.cancel()
    test_future(f, None)
    f = Future()
    test_future(f, True)
    assert f.result()


if __name__ == "__main__":
    test_future_set_result_unless_cancelled()

# Generated at 2022-06-14 11:52:37.062728
# Unit test for function chain_future
def test_chain_future():
    from tornado.platform.asyncio import AsyncIOLoop

    def f():
        pass

    def g():
        pass

    loop = AsyncIOLoop()
    a = loop.run_sync(f)
    b = loop.run_sync(g)
    chain_future(a, b)
    # TODO: test that b was called with the same args as a
    # TODO: test that a can raise an exception; b must then raise the same exception.


# Generated at 2022-06-14 11:52:43.033106
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    future_set_result_unless_cancelled(f, 42)
    assert f.result() == 42

    f = Future()
    f.cancel()
    future_set_result_unless_cancelled(f, 42)
    f.cancelled()

# Generated at 2022-06-14 11:53:02.102411
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    ioloop = IOLoop.current()

    def add_two(fut):
        fut.set_result(fut.result() + 2)

    def fail(fut):
        fut.set_exception(Exception())

    def check(fut, expected, expected_exc_type=None):
        try:
            result = fut.result()
        except Exception as e:
            result = type(e)
        assert result == expected, (result, expected)

    def check_raise(fut, exc_type):
        try:
            result = fut.result()
        except exc_type:
            return
        assert False, type(result)

    f1 = Future()
    f2 = Future()
    f3 = Future()
    f4 = Future()
   

# Generated at 2022-06-14 11:53:10.795056
# Unit test for function chain_future
def test_chain_future():
    import unittest

    from tornado import testing

    asyncio = testing.AsyncMock()
    io_loop = testing.MockAsyncIOLoop()
    io_loop.asyncio_loop = asyncio

    first = Future()
    second = Future()

    with testing.ExpectLog(app_log, ".*Cannot call.*"):
        chain_future(first, second)

    first.set_result(42)
    assert not second.done()

    with testing.ExpectLog(app_log, ".*Cannot call.*"):
        chain_future(first, second)
        io_loop.add_future(first, lambda future: None)

    with testing.ExpectLog(app_log, ".*Cannot call.*"):
        chain_future(first, second)
        io_loop.add_

# Generated at 2022-06-14 11:53:22.109915
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    loop = IOLoop.current()

    # Create a Future to be chained with the one returned by the
    # decorated function
    outer_future = Future()  # type: Future[int]

    # A dummy function to be decorated.
    def func(x: int, y: int) -> int:
        return x + y

    # This is the decorator that passes a Future to the decorated
    # function.
    def run_on_executor(f: Callable[..., int]) -> Callable[..., Future[int]]:
        def wrapper(x: int, y: int) -> Future[int]:
            conc_future = dummy_executor.submit(f, x, y)
            chain_future(conc_future, outer_future)
            return outer_future

        return

# Generated at 2022-06-14 11:53:33.307166
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    future3 = Future()

    chain_future(future1, future2)

    # Nothing has happened yet
    assert not future1.done()
    assert not future2.done()
    assert not future3.done()

    # Set result on future1, future2 should get the same result
    future1.set_result(42)
    assert future1.result() == 42
    assert future2.result() == 42

    # Set exception on future3, future2 should not get the same result
    future3.set_exception(ValueError())
    assert future3.exception() is not None
    assert future2.result() == 42



# Generated at 2022-06-14 11:53:41.499262
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop, TimeoutError

    io_loop = IOLoop()

    def set_result(f, v):
        io_loop.add_callback(f.set_result, v)  # type: ignore

    def f1():
        f = Future()
        io_loop.add_callback(set_result, f, 2)
        return f

    f2 = Future()

    chain_future(f1(), f2)

    def cb(f):
        assert f.result() == 2
        io_loop.stop()

    future_add_done_callback(f2, cb)
    assert f2.done() is False
    io_loop.start()



# Generated at 2022-06-14 11:53:54.260222
# Unit test for function chain_future
def test_chain_future():
    inner = Future()
    outer = Future()
    chain_future(inner, outer)
    assert not outer.done()
    inner.set_result(42)
    assert outer.result() == 42
    assert outer.done()


# Notes on tracking dependencies:
#
# "parent" and "child" refer to the chains of futures leading to this one.
#
# As a dependency of a parent, a future has a "callbacks" attribute
# which is a set of (parent, child) pairs. Each element is a reference
# to the parent future and the future in the parent's "children" that
# connects this future to the parent.
#
# As part of a child chain, a future has a "children" attribute which
# is a set of futures that are waiting for this one to complete.

# We use Object instead of Future so these can be

# Generated at 2022-06-14 11:54:01.686210
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    future = Future()
    future_set_exception_unless_cancelled(future, Exception("my exception"))
    assert future.exception() is not None
    try:
        future.result()
        assert False
    except Exception as e:
        assert str(e) == "my exception"
    future_set_exception_unless_cancelled(future, Exception("ignored exception"))
    future.cancel()
    try:
        future.result()
    except Exception as e:
        assert "my exception" in str(e)
    else:
        assert False

# Generated at 2022-06-14 11:54:09.699687
# Unit test for function chain_future
def test_chain_future():
    import time
    import tornado.testing
    import tornado.gen

    @tornado.testing.gen_test
    def test_wait_all_future(c):
        f1 = c._executor.submit(time.sleep, 0.01)
        f2 = c.wait_all_future(f1)
        assert not f2.done()
        yield f2
        assert f2.done()

    tornado.testing.AsyncTestCase.run_test(test_wait_all_future)



# Generated at 2022-06-14 11:54:15.824400
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import unittest.mock

    class TestChainFuture(unittest.TestCase):
        def test_simple(self):
            f1 = Future()
            f2 = Future()
            chain_future(f1, f2)
            f1.set_result(42)
            self.assertEqual(f2.result(), 42)

        def test_cancel_before(self):
            f1 = Future()
            f2 = Future()
            # cancel f1 before chain_future runs
            f1.cancel()
            chain_future(f1, f2)
            self.assertTrue(f2.cancelled())

        def test_cancel_after(self):
            f1 = Future()
            f2 = Future()
            chain_future(f1, f2)


# Generated at 2022-06-14 11:54:21.314557
# Unit test for function chain_future
def test_chain_future():
    from tornado.gen import coroutine, Return

    @coroutine
    def inner() -> None:
        raise Return(42)

    @coroutine
    def outer() -> int:
        fut = Future()
        chain_future(inner(), fut)
        result = yield fut
        raise Return(result)

    assert outer().result() == 42

# Generated at 2022-06-14 11:54:40.414755
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 42)
    assert future.done()
    assert future.result() == 42

    future = Future()
    future_set_result_unless_cancelled(future, None)
    assert future.done()
    assert future.result() is None

    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 42)
    assert future.done()
    assert future.cancelled()

# Generated at 2022-06-14 11:54:52.859814
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import contextlib
    import io
    import unittest

    class FutureSetExceptionUnlessCancelledTestCase(unittest.TestCase):
        def test_future_set_exception_unless_cancelled(self):
            @contextlib.contextmanager
            def capture_stderr():
                save = sys.stderr
                capture = io.StringIO()
                sys.stderr = capture
                try:
                    yield capture
                finally:
                    sys.stderr = save

            @contextlib.contextmanager
            def null_stderr():
                save = sys.stderr
                sys.stderr = io.BytesIO()
                try:
                    yield
                finally:
                    sys.stderr = save

            # test set_exception() on a cancelled Future

# Generated at 2022-06-14 11:54:57.703018
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, "result")
    assert future.result() == "result"

    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, "unexpected result")
    assert future.cancelled()

# Generated at 2022-06-14 11:55:04.599231
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import functools
    import threading
    import unittest

    from concurrent import futures
    import tornado.ioloop
    import tornado.gen

    class Futures(unittest.TestCase):
        def test_chain_future(self):
            # type: () -> None
            executor = futures.ThreadPoolExecutor(1)

            def slow_func():
                # type: () -> int
                time.sleep(0.01)
                return 42

            @tornado.gen.coroutine
            def f():
                # type: () -> int
                f1 = executor.submit(slow_func)
                f2 = tornado.concurrent.Future()
                chain_future(f1, f2)
                result = yield f2
                self.assertEqual(result, 42)



# Generated at 2022-06-14 11:55:11.811239
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f1 = Future()
    f1.cancel()
    future_set_exception_unless_cancelled(f1, Exception())
    f2 = Future()
    future_set_exception_unless_cancelled(f2, Exception())
    assert f2.exception()
    f3 = Future()
    future_set_exception_unless_cancelled(f3, ValueError())
    assert f3.exception()

# Generated at 2022-06-14 11:55:20.597824
# Unit test for function chain_future
def test_chain_future():
    import time
    import tornado.testing
    import tornado.gen
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.platform.asyncio import to_asyncio_future

    loop = AsyncIOMainLoop()
    loop.make_current()

    @tornado.gen.coroutine
    def f():
        yield tornado.gen.moment

    def f1():
        return f()

    def f2():
        return to_asyncio_future(f1())

    @tornado.testing.gen_test
    def test_chain():
        future = Future()
        chain_future(f1(), future)
        yield future

    @tornado.testing.gen_test
    def test_chain_loop():
        future = Future()

# Generated at 2022-06-14 11:55:27.254542
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    exc = Exception("exception 1")
    future = Future()
    future_set_exception_unless_cancelled(future, exc)
    exception_raised = True
    try:
        future.result()
    except Exception as ex:
        assert ex is exc
        exception_raised = True
    assert exception_raised

    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, exc)
    assert future.cancelled()

# Generated at 2022-06-14 11:55:35.703849
# Unit test for function chain_future
def test_chain_future():
    import unittest

    class Test(unittest.TestCase):
        def test_chain(self):
            a = futures.Future()
            b = futures.Future()
            chain_future(a, b)
            a.set_result(42)
            self.assertEqual(b.result(), 42)

        def test_cancelled(self):
            a = futures.Future()
            b = futures.Future()
            b.cancel()
            chain_future(a, b)
            a.set_result(42)
            with self.assertRaises(futures.CancelledError):
                b.result()

# Generated at 2022-06-14 11:55:41.592917
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()
    a.set_result(None)
    assert b.done()
    b = Future()
    chain_future(a, b)
    assert b.done()

# Generated at 2022-06-14 11:55:50.144594
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    exc_info = (None, RuntimeError(), None)
    future = Future()
    future_set_exc_info(future, exc_info)
    assert future.exception().with_traceback(future.exc_info()[2]) == exc_info[1]

    exc_info = (None, RuntimeError(), None)
    # Construct a future with a special exception, so it can be used as a
    # sentinel to indicate that the right exception is set.
    future = Future()
    future._exception = RuntimeError('foo')

    future_set_exc_info(future, exc_info)
    assert future.exception().with_traceback(future.exc_info()[2]) == exc_info[1]

# Generated at 2022-06-14 11:56:06.147858
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    async_future = Future()  # type: Future[int]
    conc_future = futures.Future()  # type: futures.Future[int]
    result = 1
    conc_future.set_result(result)
    chain_future(conc_future, async_future)
    assert result == async_future.result()

# Generated at 2022-06-14 11:56:19.456603
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase

    class T(AsyncTestCase):
        def test_chain_future(self):
            parent = Future()
            child = Future()
            self.assertFalse(parent.done())
            self.assertFalse(child.done())
            chain_future(parent, child)
            parent.set_result(None)
            self.assertTrue(parent.done())
            self.assertTrue(child.done())

    T().test_chain_future()


# These are the old names, to be deprecated in a future version.
# They still take both concurrent.futures.Future and tornado.concurrent.Future
# but they return the latter type.
# In the future they will become aliases for the real methods,
# and be removed again at some point in the distant future.
# These all have

# Generated at 2022-06-14 11:56:25.094492
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    def test_func(future):
        future_set_exception_unless_cancelled(future, RuntimeError("error"))

    f = Future()
    future_add_done_callback(f, test_func)
    f.set_result("success")
    f = Future()
    f.cancel()
    future_add_done_callback(f, test_func)



# Generated at 2022-06-14 11:56:30.119323
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2._state == f1._state
    f2.set_result(1729)
    assert f1._state == f2._state

# Generated at 2022-06-14 11:56:32.862695
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from tornado import web

    class testHandler(web.RequestHandler):
        executor = dummy_executor

        @run_on_executor(executor='executor')
        def get(self):
            return "get"

    response = testHandler().get()
    assert response.result() == 'get'

# Generated at 2022-06-14 11:56:42.360773
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()

    class Helloworld:
        def __init__(self):
            self.loop = asyncio.get_event_loop()
            self.future = Future()

        def cancel(self):
            self.future.cancel()

        def test(self):
            # f = self.loop.create_future()
            # future_set_result_unless_cancelled(f, "haha")
            # print(f.result())
            future_set_result_unless_cancelled(self.future, "haha")
            print(self.future.result())

    h = Helloworld()
    h.cancel()
    h.test()



# Generated at 2022-06-14 11:56:48.967407
# Unit test for function chain_future
def test_chain_future():
    f1 = futures.Future()
    f2 = futures.Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42



# Generated at 2022-06-14 11:56:58.651676
# Unit test for function future_set_exception_unless_cancelled

# Generated at 2022-06-14 11:57:11.294340
# Unit test for function chain_future
def test_chain_future():
    # Given a chain_future function
    # When we chain two Future objects together
    # Then the second should complete with the same result as the first
    # test chain_future
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_result(1)
    assert future2.result() == 1

# Generated at 2022-06-14 11:57:20.237837
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import tornado.testing
    import tornado.platform.asyncio

    tornado.platform.asyncio.AsyncIOMainLoop().install()

    class FutureTest(unittest.TestCase):
        def test_chain_future_to_concurrent_future(self):
            async_future = Future()
            conc_future = futures.Future()
            chain_future(conc_future, async_future)
            conc_future.set_result("foo")
            self.assertIsInstance(async_future.result(), str)
            self.assertEqual(async_future.result(), "foo")

        def test_chain_future_to_tornado_future(self):
            async_future = Future()
            tornado_future = Future()
            chain_future(tornado_future, async_future)

# Generated at 2022-06-14 11:57:51.695399
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exc_info(future, sys.exc_info())
    assert not future.cancelled()
    future = Future()
    try:
        raise ValueError()
    except ValueError as e:
        future_set_exc_info(future, sys.exc_info())
        assert not future.cancelled()
    future = Future()
    future_set_exception_unless_cancelled(future, ValueError("test"))
    assert not future.cancelled()

# Generated at 2022-06-14 11:58:02.624482
# Unit test for function chain_future
def test_chain_future():
    import unittest

    from tornado.testing import AsyncTestCase

    class ChainFutureTest(AsyncTestCase):
        """Unit test for function chain_future"""

        def test_chain(self):
            f1 = Future()
            f2 = Future()

            chain_future(f1, f2)

            f1.set_result(42)
            self.assertEqual(f2.result(), 42)

            f1 = Future()
            f2 = Future()
            f3 = Future()

            # Cancel f2 before it has a chance to complete
            f2.cancel()

            chain_future(f1, f2)
            chain_future(f2, f3)

            f1.set_result(42)

            self.assertTrue(f2.cancelled())

# Generated at 2022-06-14 11:58:07.250376
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    # Arrange
    import asyncio
    import time

    async def f():
        xx = await asyncio.sleep(0, result='xxx')
        print(xx)

    async def test1():
        executor = DummyExecutor()
        await f()

    # Action
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test1())
    loop.close()


if __name__ == "__main__":
    test_DummyExecutor_submit()

# Generated at 2022-06-14 11:58:19.213728
# Unit test for function chain_future
def test_chain_future():
    io_loop = asyncio.get_event_loop()

    async_future = Future()
    conc_future = futures.Future()

    chain_future(conc_future, async_future)

    result = object()
    conc_future.set_result(result)
    assert async_future.result() is result

    async_future = Future()
    conc_future = futures.Future()

    chain_future(conc_future, async_future)

    exc = Exception()
    conc_future.set_exception(exc)
    assert async_future.exception() is exc

    # Test compatibility with concurrent.futures.Future
    async_future = Future()
    conc_future = futures.Future()

    chain_future(conc_future, async_future)

    result = object()
    io_loop.run

# Generated at 2022-06-14 11:58:30.559906
# Unit test for function chain_future
def test_chain_future():
    f = Future()

    def copy(future):
        assert future is a
        if not b.done():
            if hasattr(a, "exc_info") and a.exc_info() is not None:
                future_set_exc_info(b, a.exc_info())
            elif a.exception() is not None:
                b.set_exception(a.exception())
            else:
                b.set_result(a.result())

    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    result = b.result()
    assert result == 42

    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_exception(ZeroDivisionError())

# Generated at 2022-06-14 11:58:37.638765
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import tornado.ioloop

    class ChainFutureTest(unittest.TestCase):
        @gen_test
        async def test_chain_future(self):
            future1 = Future()
            future2 = Future()
            chain_future(future1, future2)
            v = object()
            future1.set_result(v)
            self.assertTrue(future2.done())
            self.assertEqual(future2.result(), v)

    return unittest.main()

# Generated at 2022-06-14 11:58:51.200174
# Unit test for function chain_future
def test_chain_future():
    future = Future()
    f = Future()
    chain_future(future, f)
    future.set_result(1)
    assert f.result() == 1
    future2 = Future()
    f2 = Future()
    chain_future(future2, f2)
    future2.set_exception(Exception())
    assert f2.exception() is not None
    f3 = Future()
    assert f3.cancelled() is False
    future_set_result_unless_cancelled(f3, 2)
    assert f3.result() == 2
    f3.cancel()
    assert f3.cancelled() is True
    future_set_result_unless_cancelled(f3, 3)
    assert f3.cancelled() is True
    f4 = Future()

# Generated at 2022-06-14 11:58:57.771723
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()  # type: Future[str]
    f2 = Future()  # type: Future[str]
    chain_future(f1, f2)
    f1.set_result("foo")
    assert f2.result() == "foo"

    f1 = Future()
    f2 = Future()
    f1.set_result("foo")
    chain_future(f1, f2)
    assert f2.result() == "foo"

    f1 = Future()
    f2 = Future()
    f2.set_result("foo")
    chain_future(f1, f2)
    assert f2.result() == "foo"



# Generated at 2022-06-14 11:59:09.528048
# Unit test for function chain_future
def test_chain_future():
    def check(async_future, conc_future):
        with nested(
            patch.object(async_future, "set_result"),
            patch.object(async_future, "set_exception"),
        ) as (set_result, set_exception):
            value = object()
            conc_future.set_result(value)
            set_result.assert_called_once_with(value)
            exc = object()
            conc_future.set_exception(exc)
            set_exception.assert_called_once_with(exc)

    check(Future(), futures.Future())
    check(futures.Future(), Future())

# Generated at 2022-06-14 11:59:22.105883
# Unit test for function chain_future
def test_chain_future():
    from tornado.platform.asyncio import to_asyncio_future

    a = Future()
    b = Future()

    chain_future(a, b)
    a.set_result(None)
    assert b.result() is None

    a = Future()
    b = Future()
    c = Future()

    chain_future(a, b)
    chain_future(b, c)
    a.result()
    b.result()
    c.result()

    # Check that result() doesn't raise an exception
    a = Future()
    b = Future()
    c = Future()

    chain_future(a, b)
    chain_future(b, c)
    a.set_exception(ValueError)
    assert isinstance(b.exception(), ValueError)