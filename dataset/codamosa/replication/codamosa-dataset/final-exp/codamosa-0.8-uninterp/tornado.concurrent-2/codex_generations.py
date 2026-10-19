

# Generated at 2022-06-14 11:50:14.437980
# Unit test for function run_on_executor
def test_run_on_executor():
    import io
    import threading
    import unittest

    from tornado.escape import native_str

    from tornado.test.util import unittest

    class MyClass(object):
        executor = dummy_executor

        @run_on_executor
        def function_blocking(self, a, b):
            return a + b

        @run_on_executor
        def function_blocking_no_result(self):
            pass

        @run_on_executor(executor="my_other_executor")
        def function_blocking_on_other_executor(self):
            pass

    class MyBadClass(object):
        # Can't use class with no executor
        @run_on_executor
        def function_blocking(self):
            pass


# Generated at 2022-06-14 11:50:19.115835
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():  # noqa: E999
    future = Future()
    future_set_exception_unless_cancelled(future, RuntimeError("test_exc"))
    assert future.exception()
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, RuntimeError("test_exc"))
    assert not future.exception()

# Generated at 2022-06-14 11:50:30.339781
# Unit test for function chain_future
def test_chain_future():
    result = None
    error = None
    fut1 = Future()
    fut2 = Future()

    def callback(future):
        nonlocal result, error
        if future.exception() is None:
            result = future.result()
        else:
            error = future.exception()

    chain_future(fut1, fut2)
    fut2.add_done_callback(callback)
    assert fut2.done() is False
    fut1.set_result(42)
    assert fut2.done() is True
    assert result == 42

    error = None
    fut1 = Future()
    fut2 = Future()
    chain_future(fut1, fut2)
    fut2.add_done_callback(callback)
    assert fut2.done() is False

# Generated at 2022-06-14 11:50:38.464885
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f = Future()
    g = Future()
    chain_future(f, g)

    assert not f.done()
    assert not g.done()

    f.set_result(3)
    assert g.result() == 3

    f = Future()
    g = Future()
    f.set_result(5)
    chain_future(f, g)
    assert g.result() == 5


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 11:50:47.130572
# Unit test for function chain_future
def test_chain_future():
    from tornado.gen import Return
    import concurrent.futures

    io_loop = asyncio.get_event_loop()

    async def async_return(future: Future, value: object) -> None:
        await asyncio.sleep(1)
        future.set_result(value)

    def return_later(value: object) -> Future:
        f1 = Future()  # type: Future
        io_loop.add_callback(async_return, f1, value)
        return f1

    def test_with(
        f1: Future,
        f2: Future,
        f3: Future,
        value: Any,
        expected_result: Any,
        expected_exception: Optional[BaseException] = None,
    ) -> None:
        chain_future(f1, f2)
        chain_

# Generated at 2022-06-14 11:51:00.788948
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import mock

    f1 = Future()
    f2 = Future()
    f3 = Future()

    def g(f):
        # type: (Future) -> None
        assert f is f1
        f2.set_result("result")

    chain_future(f1, f2)
    chain_future(f2, f3)
    f1.add_done_callback(g)

    with mock.patch("tornado.gen.Future.set_result") as set_result:
        class Exception(object):
            pass

        f1.set_exception(Exception())
        assert set_result.call_args is None
        f3.result()

    f1 = Future()
    f2 = Future()
    f3 = Future()

# Generated at 2022-06-14 11:51:11.041355
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    from concurrent.futures import Future as ConcFuture

    class FutureTest(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            future = Future()
            result = 10
            other = Future()
            chain_future(future, other)
            future.set_result(result)
            self.assertEqual(result, (yield other))

            future = ConcFuture()
            future.set_result(result)
            other = Future()
            chain_future(future, other)
            self.assertEqual(result, (yield other))

# Generated at 2022-06-14 11:51:19.412648
# Unit test for function chain_future
def test_chain_future():  # pragma: no cover
    import tornado.testing

    def f(x: int) -> int:
        return x + 1

    def g(x: int) -> None:
        f_result = x.result()
        assert f_result == 6
        g_result.set_result(None)

    def h(x: Any) -> None:
        assert x.result() is None
        h_result.set_result(None)

    io_loop = tornado.ioloop.IOLoop()
    g_result = Future()
    h_result = Future()

    f_result = future_add_done_callback(io_loop.run_in_executor(None, f, 5), g)
    chain_future(g_result, h_result)

# Generated at 2022-06-14 11:51:31.069966
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    results = []
    f = Future()
    future_set_exception_unless_cancelled(f, Exception("test"))
    assert f.exception() is not None
    f = Future()
    future_set_exception_unless_cancelled(f, Exception("test1"))
    f = Future()
    cb = lambda x: results.append(x.exception())
    future_add_done_callback(f, cb)
    f.cancel()
    future_set_exception_unless_cancelled(f, Exception("test2"))
    # Check that the callback did not get a second Exception.
    assert results[0].args[0] == "test1"

# Generated at 2022-06-14 11:51:38.638641
# Unit test for function chain_future
def test_chain_future():

    def add(x, y):
        return x + y

    f2 = Future()
    f1 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(1)
    f1.set_result(2)
    assert f2.result() == 1

    # test exception transfer
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    # dereferenced outside of exception handler so py3 does
    # not think this is a nested exception
    exc_info = (ZeroDivisionError, ZeroDivisionError(), None)

    def error_task():
        1 / 0

    f1.add_done_callback(lambda f: f.set_exc_info(exc_info))
    f1

# Generated at 2022-06-14 11:51:54.945272
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    from tornado.testing import AsyncTestCase, gen_test

    class FutureTestCase(AsyncTestCase):
        @gen_test
        def test_future_set_result_unless_cancelled(self):
            future = Future()
            future_set_result_unless_cancelled(future, 42)

# Generated at 2022-06-14 11:52:04.974527
# Unit test for function run_on_executor
def test_run_on_executor():
    import time

    def func(arg1, arg2, kwarg=None):
        time.sleep(0.1)
        return arg1 + arg2 + kwarg

    class Foo:
        executor = dummy_executor

        @run_on_executor
        def add(self, arg1, arg2, kwarg=None):
            return arg1 + arg2 + kwarg

    foo = Foo()

    for attr in ("add", "run_on_executor"):
        assert hasattr(Foo, attr)
        assert not hasattr(Foo, "__wrapped__")

    f = foo.add(1, 2, kwarg=3)
    assert isinstance(f, futures.Future)
    assert f.result() == 6


# Generated at 2022-06-14 11:52:13.887950
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f1.done()
    assert not f2.done()
    f1.set_result(42)
    assert f2.result() == 42
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ZeroDivisionError())
    with pytest.raises(ZeroDivisionError):
        f2.result()



# Generated at 2022-06-14 11:52:22.345392
# Unit test for function chain_future
def test_chain_future():
    import time

    @gen.coroutine
    def f():
        yield gen.moment

    f1 = f()

    @gen.coroutine
    def g():
        yield gen.moment

    f2 = f1.clone()

    def callback():
        pass

    chain_future(f1, f2)
    if sys.version_info < (3, 5, 2):
        # Futures have a different callback API in Python <= 3.5.1
        time.sleep(0)
        assert f1.done()
        callback = f1._callbacks.pop()[0]
        assert not f1._callbacks
        callback(f1)
        f1._callbacks.append((callback, ()))
    assert not f2.done()
    f1.set_result(42)
    f2.result

# Generated at 2022-06-14 11:52:28.195851
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception("test"))
    assert future.exception() is not None
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception("test"))
    assert future.exception() is None

# Generated at 2022-06-14 11:52:37.726828
# Unit test for function chain_future
def test_chain_future():
    from tornado.concurrent import Future
    from tornado.testing import gen_test
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import to_asyncio_future

    async def func():
        f = Future()
        IOLoop.current().add_callback(f.set_result, None)
        f = to_asyncio_future(f)
        return f

    @gen_test
    async def test_chain():
        f = Future()
        f2 = func()
        chain_future(f2, f)
        await f2
        assert f2.done()
        assert f.done()
        await f

    IOLoop.current().run_sync(test_chain)

# Generated at 2022-06-14 11:52:50.757122
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    result = []
    # test for python 3.5 and above
    if hasattr(asyncio, 'run'):
        result = []

        class Handler(object):
            executor = dummy_executor

            @run_on_executor
            def f(self, a, b, c):
                # type: (int, int, int) -> int
                result.append([a, b, c])
                return a + b + c

        h = Handler()
        f = h.f(1, 2, 3)
        # test Future
        assert isinstance(f, Future)
        assert asyncio.run(f) == 6
        assert result.pop() == [1, 2, 3]

        result.append('fail')
        f = h.f(1, 2, KeyError())

# Generated at 2022-06-14 11:52:55.008476
# Unit test for function chain_future
def test_chain_future():
    @run_on_executor
    def f(x):
        return x
    fut = Future()
    fut2 = Future()
    chain_future(fut, fut2)
    fut.set_result(42)
    assert fut2.result() == 42



# Generated at 2022-06-14 11:53:05.213772
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test

    @run_on_executor
    def wait(future, callback):
        callback(future.result())

    @gen_test
    async def f():
        future = Future()
        future.set_result('result')
        assert future.result() == 'result'

        chained_future = Future()

        # Chain two futures together and make sure that the result is
        # the same on both.
        chain_future(future, chained_future)
        await wait(chained_future, lambda x: x)

        assert future.result() == chained_future.result()
        assert future.result() == 'result'

# Generated at 2022-06-14 11:53:17.110987
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from .lock import Condition
    from .platform.asyncio import AsyncIOLoop

    with AsyncIOLoop() as loop:
        cond = Condition()

        def hello(wait: bool) -> str:
            if wait:
                cond.wait(timeout=60)
            return "hello"

        future = dummy_executor.submit(hello, wait=False)
        assert future.result() == "hello"

        future = dummy_executor.submit(hello, wait=True)
        cond.notify_all()
        assert future.result() == "hello"

        future = dummy_executor.submit(hello, wait=True)
        future_add_done_callback(future, lambda fut: cond.notify_all())
        assert future.result() == "hello"


# Generated at 2022-06-14 11:53:35.806422
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.concurrent import Future, wrap_future
    from tornado.testing import gen_test, AsyncTestCase

    class TestChainFuture(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            p = Future()
            q = wrap_future(p)
            chain_future(p, q)
            self.assertTrue(q.done())
            self.assertEqual(q.result(), None)

            p = Future()
            p.set_result(5)
            q = wrap_future(p)
            self.assertTrue(q.done())
            self.assertEqual(q.result(), None)

            p = Future()
            q = wrap_future(p)
            q.set_result(6)

# Generated at 2022-06-14 11:53:42.878831
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import concurrent.futures
    import functools
    import sys

    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.testing import AsyncTestCase, gen_test

    AsyncIOMainLoop().install()

    class TestFuture(unittest.TestCase):
        def setUp(self):
            # For AsyncTestCase, set up functions are run in the
            # main thread, not the test runner greenlet, so we can
            # use futures.
            self.executor = concurrent.futures.ThreadPoolExecutor(2)
            self.future1 = futures.Future()
            self.future2 = futures.Future()
            self.future1.set_result(None)


# Generated at 2022-06-14 11:53:44.741995
# Unit test for function chain_future
def test_chain_future():
    @gen.coroutine
    def inner():
        raise gen.Return(42)

    @gen.coroutine
    def outer():
        fut = Future()
        chain_future(inner(), fut)
        result = yield fut
        self.assertEqual(result, 42)

    # Make sure it works with yield expressions too
    result = yield outer()

# Generated at 2022-06-14 11:53:46.654551
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    asyncio_future = Future()
    concurrent_future = futures.Future()
    chain_future(concurrent_future, asyncio_future)
    concurrent_future.set_result(None)
    assert asyncio_future.result() is None

# Generated at 2022-06-14 11:53:56.544493
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import AsyncIOLoop
    from concurrent import futures

    def f(x, y):
        return x + y

    def f2(x, y, z):
        return x + y + z

    ioloop = IOLoop.current()

    def stop_loop():
        io_loop.stop()

    # test with tornado Future first
    io_loop = IOLoop()
    io_loop.make_current()
    io_loop.add_future(
        f2(
            f(gen.coroutine(lambda: 5)(), gen.coroutine(lambda: 7)()),
            gen.coroutine(lambda: 10)(),
        ),
        stop_loop,
    )
    io_loop.start()

    # test with

# Generated at 2022-06-14 11:54:09.371474
# Unit test for function chain_future
def test_chain_future():
    from tornado.platform.asyncio import to_asyncio_future
    from tornado.testing import AsyncTestCase, gen_test

    class Test(AsyncTestCase):
        def test_chain(self):
            f1 = Future()
            f2 = to_asyncio_future(futures.Future())
            chain_future(f1, f2)
            f1.set_result(42)
            self.assertEqual(f2.result(), 42)

        @gen_test
        def test_chain_to_concurrent_future(self):
            f1 = Future()
            f2 = futures.Future()
            chain_future(f1, f2)
            f1.set_result(42)
            self.assertEqual(f2.result(), 42)


# Generated at 2022-06-14 11:54:15.693285
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    from tornado.ioloop import IOLoop
    import time
    import unittest

    class TestFuture(unittest.TestCase):
        def setUp(self):
            # type: () -> None
            self.executor = futures.ThreadPoolExecutor(4)
            self.io_loop = IOLoop()
            self.io_loop.make_current()

        def tearDown(self):
            # type: () -> None
            self.executor.shutdown()

        def test_run_on_executor(self):
            # type: () -> None
            @run_on_executor(executor='executor')
            def func(self, a, b):
                # type: (TestFuture, int, float) -> float
                time.sleep(.001)
                self

# Generated at 2022-06-14 11:54:19.244355
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def fn(a:int, b:int) -> int:
        return a + b
    executor = DummyExecutor()
    assert executor.submit(fn, 1, 2).result() == 3


# Generated at 2022-06-14 11:54:27.760114
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = loop.create_future()
    # Cancel future
    future.cancel()
    # Set exception on previously cancelled future
    future_set_exception_unless_cancelled(future, ValueError())
    # Future object should not be done
    assert not future.done()
    # Reset future
    future = loop.create_future()
    # Set exception on non-cancelled future
    future_set_exception_unless_cancelled(future, ValueError())
    # Future object should be done
    assert future.done()

# Generated at 2022-06-14 11:54:40.162179
# Unit test for function chain_future
def test_chain_future():
    import unittest

    class ChainFutureTest(unittest.TestCase):
        def test_result_chain(self):
            a = Future()
            b = Future()
            chain_future(a, b)
            self.assertFalse(b.done())
            a.set_result(42)
            self.assertTrue(b.done())
            self.assertEqual(42, b.result())

        def test_exc_chain(self):
            a = Future()
            b = Future()
            chain_future(a, b)
            self.assertFalse(b.done())
            a.set_exception(ValueError("foo"))
            self.assertTrue(b.done())
            self.assertEqual("foo", b.exception().args[0])


# Generated at 2022-06-14 11:54:58.387739
# Unit test for function chain_future
def test_chain_future():
    def future_with_result(result, future):
        future.set_result(result)
        return future

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    future_with_result(3, f1)
    assert f2.result() == 3

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    future_with_result(4, f2)
    assert f2.result() == 4

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ZeroDivisionError())
    assert f2.exception() is not None
    assert isinstance(f2.exception(), ZeroDivisionError)


# Generated at 2022-06-14 11:55:12.751308
# Unit test for function chain_future
def test_chain_future():
    import unittest

    import sys
    import traceback

    from tornado.testing import AsyncTestCase, gen_test

    class ChainFutureTest(AsyncTestCase):
        def test_main(self):
            there = Future()
            back = Future()
            result = [None]
            exc_info = [None]

            def set_result(arg):
                result[0] = arg
            there.add_done_callback(set_result)

            def set_exc(exc):
                exc_info[0] = sys.exc_info()
            there.add_done_callback(set_exc)

            chain_future(back, there)

            back.set_result('foo')
            self.assertEqual(result[0], 'foo')
            self.assertEqual(exc_info[0], None)

           

# Generated at 2022-06-14 11:55:17.687831
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ValueError)
    with pytest.raises(ValueError):
        f2.result()



# Generated at 2022-06-14 11:55:28.610160
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import tornado.ioloop
    import unittest
    from tornado.concurrent import Future

    class MainIOLoopTest(unittest.TestCase):
        def setUp(self):
            self.io_loop = tornado.ioloop.IOLoop()
            self.future = Future()
            self.future.set_result(True)

        def test_future_set_exception_unless_cancelled(self):
            f = self.future
            future_set_exception_unless_cancelled(f, RuntimeError("Test"))
            self.assertIsNone(f.exception())

        def test_future_set_exception_unless_cancelled_cancelled(self):
            f = self.future
            f.cancel()

            self.assertEqual(f.cancelled(), True)


# Generated at 2022-06-14 11:55:33.392690
# Unit test for function chain_future
def test_chain_future():
    def check_copy_success(source, dest):
        assert not dest.done()
        source.set_result(None)
        assert dest.done()
        assert dest.exception() is None

    def check_copy_failure(source, dest):
        assert not dest.done()
        source.set_exception(RuntimeError("foo"))
        assert dest.done()
        assert dest.exception().args == ("foo",)

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    check_copy_success(f1, f2)
    check_copy_failure(f1, f2)

    f1 = Future()
    f2 = Future()
    chain_future(f2, f1)
    check_copy_success(f2, f1)

# Generated at 2022-06-14 11:55:46.739834
# Unit test for function chain_future
def test_chain_future():
    loop = asyncio.get_event_loop()
    a = Future()
    b = Future()
    chain_future(a, b)
    thread_pool = futures.ThreadPoolExecutor(1)
    result = None
    exception = None

    def cb(fut: Future) -> None:
        nonlocal result, exception
        if fut.exception() is not None:
            exception = fut.exception()
        else:
            result = fut.result()

    a.set_result(1)
    # The value of a is copied over to b, but the callback is not invoked
    # until b is completed
    assert not b.done()
    future_add_done_callback(b, cb)
    assert result == 1
    assert exception is None

    result = None
    exception = None
    a = thread

# Generated at 2022-06-14 11:56:00.006325
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing
    io_loop = tornado.testing.AsyncTestCase.get_new_ioloop()

    @gen.coroutine
    def inner():
        (yield gen.sleep(0.01))
        raise Exception("inner error")

    @gen.coroutine
    def outer():
        f = inner()
        try:
            yield f
        except Exception as e:
            return str(e)
        raise Exception("outer error")

    def check_result(f):
        io_loop.stop()
        try:
            f.result()
        except Exception as e:
            result = "caught %s" % e
        else:
            result = "no exception"
        self.assertEqual(result, "caught inner error")

    f = outer()

# Generated at 2022-06-14 11:56:09.233066
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    f.set_result(1)
    g = Future()
    chain_future(f, g)
    assert g.result() == 1
    h = Future()
    f.add_done_callback(lambda future: future_set_result_unless_cancelled(h, 2))
    assert h.result() == 2
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_result(3)
    assert g.result() == 3
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_exception(ZeroDivisionError())
    try:
        g.result()
    except ZeroDivisionError:
        pass



# Generated at 2022-06-14 11:56:14.389030
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ZeroDivisionError())
    assert f2.exception() is not None

# Generated at 2022-06-14 11:56:25.431777
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import unittest.mock
    from typing import List

    future = Future()
    exc = ZeroDivisionError()
    future_set_exception_unless_cancelled(future, exc)
    # check for a pending exception
    assert future.exception() == exc
    assert future.exception() is exc

    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, exc)
    # check that the future doesn't now have an exception
    assert future.exception() is None

    # Test that the exception is logged
    with unittest.mock.patch("tornado.log.app_log.error") as mock_error:
        exc = ZeroDivisionError()
        future = Future()
        future.cancel()
        future_set_exception_

# Generated at 2022-06-14 11:56:53.213924
# Unit test for function chain_future
def test_chain_future():
    def cb(f):
        pass

    f = Future()
    f2 = Future()
    chain_future(f, f2)
    chain_future(f2, f)
    f.add_done_callback(cb)
    f2.add_done_callback(cb)

    f.set_result(None)
    assert not f2.cancelled()
    assert f2.done()

# Generated at 2022-06-14 11:57:00.469144
# Unit test for function run_on_executor
def test_run_on_executor():
    import random
    import unittest

    class MockExecutor:
        def submit(
            self, fn: Callable[..., _T], *args: Any, **kwargs: Any
        ) -> "futures.Future[_T]":
            self.n += 1
            self.fn = fn
            self.args = args
            self.kwargs = kwargs
            future = futures.Future()
            self.done = False

            def copy(f: "futures.Future[_T]") -> None:
                assert f is self.future
                future.set_result(f.result())
                self.done = True

            self.future = futures.Future()
            self.future.add_done_callback(copy)
            return future


# Generated at 2022-06-14 11:57:05.875329
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    # Tests that an asyncio.Future cannot be set twice
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    if sys.version_info >= (3, 7):
        assert future.done()
    else:
        # asyncio.Future.done() is not available in older versions of python
        # but setting a Future should still succeed in this case
        pass
    with pytest.raises(InvalidStateError):
        future_set_result_unless_cancelled(future, 2)



# Generated at 2022-06-14 11:57:17.652632
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    async def test_exc(future, exc_class):
        try:
            await future
        except Exception as e:
            assert e.__class__ == exc_class

    exc_class = Exception("test_exc")
    future = Future()
    future_set_exception_unless_cancelled(future, exc_class)
    test_exc(future, exc_class)

    future2 = Future()
    future_set_exception_unless_cancelled(future2, exc_class)
    future2.cancel()
    test_exc(future2, asyncio.CancelledError)

# Generated at 2022-06-14 11:57:30.258332
# Unit test for function run_on_executor
def test_run_on_executor():
    from unittest.mock import MagicMock

    class Foo:
        def __init__(self, executor):
            self.executor = executor
            self.called = False

        @run_on_executor
        def bar(self):
            self.called = True
            return None

        @run_on_executor(executor="executor2")
        def baz(self):
            self.called = True
            return None

    executor = MagicMock()
    executor.submit.side_effect = lambda fn, *args, **kwargs: fn(*args, **kwargs)
    foo = Foo(executor)
    foo.bar()
    foo.baz()
    assert foo.called

    executor.submit.side_effect = RuntimeError()
    foo.bar()

# Generated at 2022-06-14 11:57:38.937411
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    e = DummyExecutor()

    def f(a, b, c):
        return a, b, c

    future = e.submit(f, 1, 2, c=3)
    assert future.result() == (1, 2, 3)

    future = e.submit(f, 1, b=2, c=3)
    assert future.result() == (1, 2, 3)

    def g():
        raise Exception("expected")

    future = e.submit(g)
    try:
        future.result()
    except Exception as e:
        assert str(e) == "expected"
    else:
        raise AssertionError("expected exception")

# Generated at 2022-06-14 11:57:52.118271
# Unit test for function chain_future
def test_chain_future():

    def func1(message):
        print("func1:", message)
        return message

    def func2(message):
        print("func2:", message)
        return message

    def func3(message):
        print("func3:", message)
        return message

    def func4(future):
        print("func4:", future.result())

    def callback(future):
        print("callback:", future.result())

    # func1 -> func2 -> callback
    future1 = asyncio.get_event_loop().run_in_executor(
        dummy_executor, func1, 'hello1'
    )
    future2 = asyncio.get_event_loop().run_in_executor(
        dummy_executor, func2, 'hello2'
    )
    future1.add_done_callback

# Generated at 2022-06-14 11:58:03.024423
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import concurrent.futures
    from tornado.concurrent import Future
    from tornado.ioloop import IOLoop

    class MyTestCase(unittest.TestCase):
        def setUp(self):
            self.io_loop = IOLoop()
            self.executor = concurrent.futures.ThreadPoolExecutor(1)

        @run_on_executor
        def blocking_method(self):
            import time
            time.sleep(0.1)
            return 42

        @run_on_executor
        def blocking_method_future(self):
            import time
            time.sleep(0.1)
            return Future()

        async def async_method(self):
            return await self.blocking_method()

        async def async_method_future(self):
            return await self

# Generated at 2022-06-14 11:58:09.313584
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import time

    event_stream = []

    def callback1(future):
        event_stream.append('callback1 invoked')

    def callback2(future):
        event_stream.append('callback2 invoked')

    f = Future()
    f2 = Future()
    chain_future(f, f2)
    chain_future(f, f2)
    f.add_done_callback(callback1)
    f.add_done_callback(callback2)
    f2.add_done_callback(callback1)
    f2.add_done_callback(callback2)

    f.set_result(42)
    assert event_stream == [
        'callback1 invoked',
        'callback2 invoked',
        'callback1 invoked',
        'callback2 invoked',
    ]
    assert f2

# Generated at 2022-06-14 11:58:15.275740
# Unit test for function chain_future
def test_chain_future():
    @coroutine
    def chain(source, target):
        result = yield source
        target.set_result(result)

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    IOLoop.current().add_callback(f1.set_result, 42)
    assert f2.result() == 42



# Generated at 2022-06-14 11:58:31.327062
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f = Future()  # type: Future[int]
    g = Future()  # type: Future[int]
    chain_future(f, g)
    f.set_result(42)
    assert g.result() == 42
    f2 = Future()  # type: Future[int]
    g2 = Future()  # type: Future[int]
    f2.set_exception(ValueError())
    chain_future(f2, g2)
    assert isinstance(g2.exception(), ValueError)
    f3 = Future()  # type: Future[int]
    g3 = Future()  # type: Future[int]
    f3.set_result(42)
    g3.set_result(84)
    chain_future(f3, g3)


# Generated at 2022-06-14 11:58:34.473378
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    f.set_result(123)
    g = Future()
    chain_future(f, g)
    assert g.result() == 123

# Generated at 2022-06-14 11:58:36.431412
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    exc = RuntimeError()
    future_set_exception_unless_cancelled(future, exc)
    assert future.exception() is exc
    future.cancel()
    future_set_exception_unless_cancelled(future, RuntimeError())
    assert future.exception() is exc



# Generated at 2022-06-14 11:58:39.077501
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    future = Future()
    assert future.done() is False
    future_set_exception_unless_cancelled(future, RuntimeError())
    assert future.done() is True
    assert isinstance(future.exception(), RuntimeError)


# Generated at 2022-06-14 11:58:43.856768
# Unit test for function chain_future
def test_chain_future():
    async def f():
        f1 = Future()
        f2 = Future()
        chain_future(f1, f2)
        f1.set_result(42)
        assert (await f2) == 42

    asyncio.run(f())

# Generated at 2022-06-14 11:58:54.400323
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_result(42)
    assert g.result() == 42
    assert g.done()

    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_exception(RuntimeError("foo"))
    assert g.exception() is not None
    assert "foo" in g.exception().args[0]
    assert g.done()

    f = Future()
    g = Future()
    chain_future(f, g)
    f.cancel()
    assert g.cancelled()
    assert g.done()



# Generated at 2022-06-14 11:59:07.752467
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.testing import gen_test

    @gen_test
    async def test_future_set_exception_unless_cancelled_impl():
        from tornado import gen

        future1 = gen.Future()
        future2 = gen.Future()

        @gen.coroutine
        def helper():
            future_set_exception_unless_cancelled(future1, Exception("test"))
            raise gen.Return(1)

        @gen.coroutine
        def helper2():
            future_set_exception_unless_cancelled(future2, Exception("test"))
        # Testing that set_exception_unless_cancelled works even if the
        # Future is cancelled in 

# Generated at 2022-06-14 11:59:12.864265
# Unit test for function run_on_executor
def test_run_on_executor():

    class Foo(object):
        executor = dummy_executor

        @run_on_executor
        def func(self, arg):
            return arg

    f = Foo()
    x = f.func(42)
    assert isinstance(x, Future)
    assert x.result() == 42

    y = f.func('hello')
    assert y.result() == 'hello'



# Generated at 2022-06-14 11:59:17.099997
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    a = Future()
    future_set_result_unless_cancelled(a, 42)
    assert a.result() == 42
    a = Future()
    a.cancel()
    future_set_result_unless_cancelled(a, 42)
    assert a.cancelled() == True

# Generated at 2022-06-14 11:59:21.561360
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():

    # Arrange
    from typing import Callable
    from concurrent import futures
    from tornado.concurrent import Future

    # Act
    d = dummy_executor.submit(print, "test")

    # Assert
    assert isinstance(d, Future)

# Generated at 2022-06-14 11:59:57.674217
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.util import raise_exc_info
    import asyncio

    class CustomException(Exception):
        """A custom exception class"""

    def cancel_future(future):
        future.cancel()

    exception_raised = False
    exception = CustomException("custom exception")
    conc_future = futures.Future()
    async_future = asyncio.Future()

    # Test cancellation with a `concurrent.futures.Future`
    conc_future.add_done_callback(cancel_future)
    future_set_exception_unless_cancelled(conc_future, exception)
    try:
        conc_future.result()
    except futures.CancelledError:
        # make sure that we went through the cancellation branch on our test
        assert not conc_future.cancelled()

# Generated at 2022-06-14 12:00:09.941234
# Unit test for function chain_future
def test_chain_future():
    def error_callback(future):
        raise future.result()

    f1 = Future()
    io_loop = IOLoop()

    f2 = Future()
    chain_future(f1, f2)
    f2.add_done_callback(error_callback)

    # Success case:
    f1.set_result('foo')
    io_loop.add_future(f2, lambda f: f.result())
    f2.done()

    # Failure case:
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f2.add_done_callback(error_callback)
    f1.set_exception(Exception('foo'))
    io_loop.add_future(f2, lambda f: f.result())
    f2.done()