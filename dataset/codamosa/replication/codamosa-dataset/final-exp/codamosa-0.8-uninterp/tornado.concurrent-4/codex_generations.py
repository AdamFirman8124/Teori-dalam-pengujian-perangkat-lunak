

# Generated at 2022-06-14 11:50:21.396947
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def copy_future(a: "Future[bool]", b: "Future[bool]") -> None:
        # type: (Future[_T], Future[_T]) -> None
        assert a is not b
        if a.exception() is not None:
            b.set_exception(a.exception())
            return
        if a.cancelled():
            b.cancel()
            return
        assert a.done()
        assert b.done()
        b.set_result(a.result())

    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(None)
    assert a.done()
    assert b.done()

    a = Future()
    b = Future()
    chain_future(a, b)


# Generated at 2022-06-14 11:50:23.052957
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    class TestException(Exception):
        pass

    test_exception = TestException()

    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, test_exception)

# Generated at 2022-06-14 11:50:32.503157
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class TestChainFutureTest(AsyncTestCase):
        def test_chain_future(self):
            a, b = Future(), Future()
            chain_future(a, b)
            a.set_result("foo")
            self.assertEqual(b.result(), "foo")

        # Old-style Future does not have *_nowait functions;
        # can't test them.

        @gen_test
        def test_chain_future_exc(self):
            a, b = Future(), Future()
            chain_future(a, b)
            a.set_exception(RuntimeError("foo"))
            with self.assertRaises(RuntimeError) as cm:
                yield b
            self.assertEqual(str(cm.exception), "foo")


# Generated at 2022-06-14 11:50:44.254693
# Unit test for function chain_future
def test_chain_future():
    io_loop = asyncio.get_event_loop()
    f = Future()
    f2 = Future()
    chain_future(f, f2)
    assert not f2.done()
    f.set_result(5)
    yield gen_test_timeout(0.1)
    assert f2.done()
    assert f2.result() == 5

    f = Future()
    f2 = Future()
    f.set_result(5)
    chain_future(f, f2)
    assert f2.done()
    assert f2.result() == 5

    f = Future()
    f2 = Future()
    f2.set_result(6)
    chain_future(f, f2)
    assert f2.done()
    assert f2.result() == 6

    # This test fails

# Generated at 2022-06-14 11:50:50.430055
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():

    def _helper(fut):
        future_set_result_unless_cancelled(fut, True)
        assert fut.result() is True

    # Test both Tornado Future and asyncio Future
    _helper(Future())

    try:
        # Test concurrent.futures.Future
        from concurrent.futures import Future

        _helper(Future())
    except ImportError:
        # concurrent.futures is not available in Python 2.7
        pass

# Generated at 2022-06-14 11:50:56.562492
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception("foo"))
    assert str(future.exception()) == "foo"
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception("foo"))

# Generated at 2022-06-14 11:51:05.773981
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import time

    a, b = Future(), Future()
    chain_future(a, b)
    a.set_result(42)
    assert b.result() == 42
    assert b.done()
    a, b = Future(), Future()
    chain_future(a, b)
    a.set_exception(RuntimeError("test"))
    with pytest.raises(RuntimeError, match="test"):
        b.result()
    assert b.done()


@pytest.mark.asyncio
async def test_future_set_result_unless_cancelled():
    # type: () -> None
    future = Future()
    future_set_result_unless_cancelled(future, None)
    assert future.done()
    future.cancel()
    future

# Generated at 2022-06-14 11:51:10.275484
# Unit test for function chain_future
def test_chain_future():
    pass
    # unfinished_future = Future()
    # finished_future = Future()
    # finished_future.set_result(None)
    # chain_future(unfinished_future, finished_future)
    # chain_future(finished_future, unfinished_future)



# Generated at 2022-06-14 11:51:16.277160
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 'foo')
    assert future.result() == 'foo'

    future = Future()
    future.set_result('bar')
    future_set_result_unless_cancelled(future, 'foo')
    assert future.result() == 'bar'

    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 'foo')
    assert future.cancelled()



# Generated at 2022-06-14 11:51:19.733358
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 42)
    assert future.result() == 42
    assert not future.cancelled()

    future = Future()
    future_set_result_unless_cancelled(future, 666)
    future.cancel()
    assert future.cancelled()
    assert future.result() is None

# Generated at 2022-06-14 11:51:33.798186
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    class TestException(Exception):

        def __init__(self, *args, **kwargs):
            self.msg = "test"

    exception = TestException()
    future: Future = Future()
    future_set_exception_unless_cancelled(future, exception)
    assert future.exception() is not None
    assert future.exception().msg == "test"
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, exception)

# Generated at 2022-06-14 11:51:45.978917
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    def raise_exception():
        raise Exception()

    def cancel_future():
        future.cancel()

    future = Future()

    # test that exception is raised when future is not canceled
    future_set_exception_unless_cancelled(future, raise_exception)
    assert future.exception()

    # test that future is not updated when canceled
    future = Future()
    future.add_done_callback(cancel_future)
    future_set_exception_unless_cancelled(future, raise_exception)
    assert future.cancelled()



# Generated at 2022-06-14 11:51:55.286848
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    future = Future()  # type: Future[int]
    chained = Future()  # type: Future[int]
    chain_future(future, chained)
    future.set_result(42)
    assert chained.result() == 42

    chained = Future()
    chain_future(future, chained)
    assert chained.result() == 42

    future = Future()
    chained = Future()
    future.set_result(42)
    chain_future(future, chained)
    assert chained.result() == 42

    future = Future()
    chained = Future()
    future.set_exception(RuntimeError("foo"))
    chain_future(future, chained)
    try:
        chained.result()
    except RuntimeError:
        pass

    future = Future()
    chained = Future()
   

# Generated at 2022-06-14 11:51:59.374082
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    f = Future()
    f.cancel()
    # set_exception_unless_cancelled should not raise an exception
    future_set_exception_unless_cancelled(f, Exception("error"))

# Generated at 2022-06-14 11:52:06.356528
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing

    @gen_test
    def test_chain_future():
        f = Future()
        t = timed_call(0.1, f.set_result, 42)
        f2 = Future()
        chain_future(f, f2)
        result = yield f2
        t.cancel()
        self.assertEqual(result, 42)

    # Unit test for function wait_for_future
    @gen_test
    def test_wait_for_future():
        f = Future()
        t = timed_call(0.1, f.set_result, 42)
        result = yield wait_for_future(f)
        t.cancel()
        self.assertEqual(result, 42)

    @gen_test
    def test_wait_for_future_error():
        f

# Generated at 2022-06-14 11:52:09.265296
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def func():
        return 1
    future = dummy_executor.submit(func)
    assert future.result() == 1

# Generated at 2022-06-14 11:52:15.987526
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop()
    io_loop.make_current()
    try:

        def callback(future: Future[str]) -> None:
            io_loop.stop()
        f = Future()
        g = Future()
        chain_future(f, g)
        future_add_done_callback(g, callback)
        f.set_result(42)
        io_loop.start()
        assert g.result() == 42
    finally:
        io_loop.clear_current()



# Generated at 2022-06-14 11:52:23.546400
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def my_async_func(arg1: int, arg2: int, arg3: int):
        # type: (int, int, int) -> int
        return arg1 + arg2 + arg3

    class ReturnFuture(object):
        executor = dummy_executor

        @run_on_executor
        def my_method(self, x, y, z):
            return my_async_func(x, y, z)

    a = ReturnFuture()
    b = ReturnFuture()

    c = a.my_method(1, 2, z=3)
    d = b.my_method(4, 5, z=6)

    e = Future()
    f = Future()
    chain_future(c, e)
    chain_future(d, f)


# Generated at 2022-06-14 11:52:31.693680
# Unit test for function run_on_executor
def test_run_on_executor():  # pragma: no cover
    import unittest  # type: ignore

    class MyTest(unittest.TestCase):
        def test_chain(self):
            @gen.coroutine
            def go():
                ioloop = IOLoop.current()
                executor = ThreadPoolExecutor(1)
                self.executor = executor
                self.f1 = Future()
                self.f2 = Future()
                self.f3 = Future()
                self.result = None
                self.exception = None
                self.exc_info = None

                ioloop.add_future(self.f1, lambda f: self.f2.set_result(f.result()))
                ioloop.add_future(self.f2, lambda f: self.f3.set_result(f.result()))

# Generated at 2022-06-14 11:52:39.432037
# Unit test for function chain_future
def test_chain_future():
    import time

    @gen.coroutine
    def f():
        yield gen.sleep(0.01)
        raise Exception()

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    def error(f):
        1 / 0

    f1.add_done_callback(error)
    time.sleep(0.001)
    f1.set_exception(Exception())
    with ExpectLog(app_log, "Exception in callback.*ZeroDivisionError"):
        test_utils.run_until_complete(test_utils.wait_for_exception(f1))

    @gen.coroutine
    def use_f2():
        yield f2

    g = use_f2()

# Generated at 2022-06-14 11:53:00.676540
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from tornado.concurrent import Future
    from tornado.ioloop import IOLoop

    def foo() -> None:
        future.set_result(42)

    future = Future()
    IOLoop.current().run_sync(lambda: dummy_executor.submit(foo))
    assert future.result() == 42

# Generated at 2022-06-14 11:53:10.198512
# Unit test for function chain_future
def test_chain_future():
    from tornado import gen
    from tornado.testing import AsyncTestCase, bind_unused_port

    class ChainFutureTest(AsyncTestCase):
        @gen.coroutine
        def test_chain_future(self):
            # Test both Tornado Future and asyncio Future
            yield self.wait_for_future(
                gen.convert_yielded(gen.coroutine(lambda: 7))(),
                lambda gen_result: self.assertEqual(gen_result.result(), 7),
            )
            # Test both Tornado Future and asyncio Future

# Generated at 2022-06-14 11:53:21.734882
# Unit test for function chain_future
def test_chain_future():
    @typing.no_type_check
    def f(result, exc_info):
        test_chain_future.result = result
        test_chain_future.exc_info = exc_info

    a = Future()
    b = Future()
    chain_future(a, b)
    b.result()
    with pytest.raises(Exception):
        b.exception()
    assert b.exception() is None
    a.set_result(42)
    assert b.result() == 42
    b.exception()
    assert b.exception() is None
    exc = ValueError()
    a = Future()
    chain_future(a, b)
    a.set_exception(exc)
    assert b.exception() is exc
    b.set_exception(ZeroDivisionError())
   

# Generated at 2022-06-14 11:53:26.957643
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    assert future.result() == 1
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 1)
    assert future.cancelled()


# Generated at 2022-06-14 11:53:29.835136
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception("test exception"))
    if not future.cancelled():
        assert future.exception() is not None
        assert str(future.exception()) == "test exception"

# Generated at 2022-06-14 11:53:40.685370
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import threading
    import time
    import traceback
    import concurrent.futures

    class MyThreadPoolExecutor(concurrent.futures.ThreadPoolExecutor):
        def shutdown(self, wait=True):
            # ThreadPoolExecutor.shutdown() is not compatible with
            # unittest.TestCase.tearDown(), which has a `wait` argument
            # too.
            concurrent.futures.ThreadPoolExecutor.shutdown(self, wait=wait)

    class RunOnExecutorTest(unittest.TestCase):
        def setUp(self) -> None:
            self.executor = MyThreadPoolExecutor(1)

        def tearDown(self) -> None:
            self.executor.shutdown(wait=True)


# Generated at 2022-06-14 11:53:48.027183
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase

    class ChainFutureTest(AsyncTestCase):
        def test_chain(self) -> None:
            f1 = Future()
            f2 = Future()
            chain_future(f1, f2)
            f1.set_result('test')
            self.assertEqual(f2.result(), 'test')

    test = ChainFutureTest()
    test.test_chain()

# Generated at 2022-06-14 11:53:57.013224
# Unit test for function chain_future
def test_chain_future():
    import unittest

    from tornado.ioloop import IOLoop

    ioloop = IOLoop.current()

    class TestChainFuture(unittest.TestCase):
        @unittest.expectedFailure
        def test_chain_future_invalid_type(self):
            a = object()
            b = object()
            chain_future(a, b)

        def test_chain_future_order(self):
            a = Future()
            b = Future()
            chain_future(a, b)
            a.set_result(1)
            self.assertEqual(b.result(), 1)

        def test_chain_future_order_2(self):
            a = futures.Future()
            b = Future()
            chain_future(a, b)
            a.set_result(1)
           

# Generated at 2022-06-14 11:54:01.170728
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42



# Generated at 2022-06-14 11:54:08.356689
# Unit test for function chain_future
def test_chain_future():
    io_loop = asyncio.get_event_loop()
    future1 = io_loop.create_future()
    future2 = io_loop.create_future()
    chain_future(future1, future2)

    # Simulate the completion of future1 in another thread
    future1.set_result(42)
    io_loop.run_until_complete(future2)
    assert future2.result() == 42



# Generated at 2022-06-14 11:54:49.116838
# Unit test for function chain_future
def test_chain_future():
    import time
    import unittest

    from tornado.gen import Future, Task, coroutine
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import AnyThreadEventLoopPolicy


    asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())


    class AsyncioFuture(Future):
        def __init__(self):
            super(AsyncioFuture, self).__init__()
            self._asyncio_future = asyncio.Future()


        def cancel(self):
            self._asyncio_future.cancel()


        def cancelled(self):
            return self._asyncio_future.cancelled()


        def result(self):
            # type: () -> _T
            return self._asyncio_future.result()



# Generated at 2022-06-14 11:54:54.683959
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase

    # First test: Test that chain_future copies results
    # of the first Future to the second, unless second already done.
    a = Future()
    b = Future()
    chain_future(a, b)
    b.cancel()
    try:
        a.set_result(42)
    except futures.CancelledError:
        pass
    else:
        assert False
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    assert b.done()
    assert b.result() == 42

    # Second test: same as first, but using asyncio.Future
    class Future2(asyncio.Future):
        def result(self) -> int:
            return cast(int, super().result())

    a = Future

# Generated at 2022-06-14 11:55:02.525817
# Unit test for function chain_future
def test_chain_future():
    def do_future(result, exception=None):
        f = Future()
        if exception is not None:
            f.set_exception(exception)
        else:
            f.set_result(result)
        return f

    # test chaining of futures
    a, b, c, d, e = [Future() for i in range(5)]
    chain_future(a, b)
    chain_future(b, c)
    chain_future(c, d)
    chain_future(d, e)
    a.set_result("a")
    assert e.result() == "a"

    # test that chaining a future to a cancelled one sets the result
    chain_future(Future(), a)
    chain_future(a, b)
    assert b.result() is None

    # test that chaining

# Generated at 2022-06-14 11:55:12.362654
# Unit test for function chain_future
def test_chain_future():
    # This test is here because as of Python 3.4.6, concurrent.futures.Future
    # and asyncio.Future are two incompatible types, so you need a custom
    # function call to chain from one to the other.
    io_loop = IOLoop()
    f1 = Future()
    f2 = Future()
    f1.set_result(42)
    chain_future(f1, f2)
    io_loop.add_future(f2, lambda f: io_loop.stop())
    io_loop.start()
    assert f2.result() == 42



# Generated at 2022-06-14 11:55:17.012490
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.set_exception(RuntimeError('hello'))
    assert f.exception() is not None
    f = Future()
    f.cancel()
    assert f.cancelled() is True
    assert f.exception() is None

    future_set_exception_unless_cancelled(f, RuntimeError('any'))
    assert f.exception() is None



# Generated at 2022-06-14 11:55:20.778189
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    try:
        future.cancel()
        future_set_result_unless_cancelled(future, "foo")
    except asyncio.InvalidStateError:
        pass
    assert not future.cancelled()



# Generated at 2022-06-14 11:55:31.240507
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.ioloop import IOLoop

    class TestCase(AsyncTestCase):
        def test_chain_future(self):
            future1 = Future()
            future2 = Future()

            chain_future(future1, future2)

            future1.set_result(42)
            self.assertEqual(future2.result(), 42)

            future1 = Future()
            future2 = Future()
            future1.set_result(42)

            chain_future(future1, future2)

            self.assertEqual(future2.result(), 42)

        def test_exc_info(self):
            future = Future()
            try:
                raise Exception("foo")
            except Exception:
                exc_info = sys.exc_info()


# Generated at 2022-06-14 11:55:45.228224
# Unit test for function chain_future
def test_chain_future():
    # Check that the target is not called prematurely
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(1)
    assert f2.result() == 1

    # Check that the target gets the right result
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42

    # Check that the target gets the right exception
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(IOError())
    try:
        f2.result()
    except IOError:
        pass

# Generated at 2022-06-14 11:55:52.416240
# Unit test for function chain_future
def test_chain_future():
    import functools
    import time
    import unittest
    import warnings

    from tornado import gen

    if hasattr(unittest, "mock"):
        # python >= 3.3
        import unittest.mock as mock
    else:
        import mock

    try:
        from concurrent import futures
    except ImportError:
        futures = None

    if futures:

        @gen.coroutine
        def f():
            yield gen.sleep(0.01)
            raise gen.Return(42)

        def use_future(f):
            @gen.coroutine
            def wrapper():
                # type: () -> int
                raise gen.Return((yield f))

            return wrapper


# Generated at 2022-06-14 11:55:55.451091
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, Exception("foo"))

# Generated at 2022-06-14 11:56:57.855242
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, RuntimeError("test"))

# Generated at 2022-06-14 11:57:16.451898
# Unit test for function chain_future
def test_chain_future():
    def f(x: Any) -> None:
        pass

    if hasattr(futures, "Future"):
        # concurrent.futures.Future is only available in python 3
        f = futures.Future()
        g = futures.Future()
        chain_future(f, g)
        f.set_result(42)
        assert g.result() == 42

        f = futures.Future()
        g = futures.Future()
        chain_future(f, g)
        f.set_exception(ZeroDivisionError())
        assert g.exception() is not None

        f = futures.Future()
        g = futures.Future()
        chain_future(f, g)
        f.cancel()
        assert g.cancelled()

    f = Future()
    g = Future()
    chain_future

# Generated at 2022-06-14 11:57:27.860127
# Unit test for function chain_future
def test_chain_future():
    from concurrent import futures
    from tornado import gen

    f = Future()

    def callback(fut):
        f.set_result(None)

    chain_future(f, Future())
    future_add_done_callback(f, callback)
    chain_future(f, Future())

    # This test verifies that chain_future doesn't trigger the callback
    # prematurely.
    f = Future()
    chain_future(f, Future())
    future_add_done_callback(f, callback)
    chain_future(f, Future())

    c = futures.Future()
    a = Future()
    chain_future(c, a)

    @gen.coroutine
    def get_a():
        raise gen.Return(a)

    gen.coroutine(get_a)()



# Generated at 2022-06-14 11:57:33.688777
# Unit test for function chain_future
def test_chain_future():

    future1 = Future()
    future2 = Future()
    future3 = Future()
    chain_future(future1, future2)
    chain_future(future2, future3)
    assert not future1.done()
    assert not future2.done()
    assert not future3.done()

    future1.set_result(42)
    assert future2.result() == 42
    assert future3.result() == 42

    future1 = Future()
    future2 = Future()
    future3 = Future()
    chain_future(future1, future2)
    chain_future(future2, future3)
    assert not future1.done()
    assert not future2.done()
    assert not future3.done()

    future1.set_exception(ZeroDivisionError())

# Generated at 2022-06-14 11:57:41.013489
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    @run_on_executor
    def func(a, b):
        # type: (int, int) -> int
        return a + b

    @gen.coroutine
    def main():
        # type: () -> None
        # This future will succeed when the other one fails.
        f1 = func(1, 2)  # type: Future[int]
        # This future will complete when the other one succeeds.
        f2 = func(3, 4)  # type: Future[int]
        # When the first future finishes, its result or exception should be
        # copied to the second future.
        chain_future(f1, f2)
        try:
            result = yield f2
        except Exception as e:
            result = str(e)

# Generated at 2022-06-14 11:57:53.267097
# Unit test for function chain_future
def test_chain_future():
    import time
    import unittest

    from tornado.ioloop import IOLoop

    async def test_async_future():
        future_1 = Future()
        future_1.set_result(None)
        future_2 = Future()
        chain_future(future_1, future_2)
        # future_2 should have the same state as future_1
        assert future_2.done()
        assert not future_2.cancelled()
        assert not future_2.exception()

        future_3 = Future()
        # Cancel future_3 to check that future_2 isn't overwritten
        future_3.cancel()
        chain_future(future_1, future_3)
        assert future_3.done()
        assert not future_3.cancelled()
        assert not future_3.exception

# Generated at 2022-06-14 11:58:00.658512
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = asyncio.Future()
    assert not future.cancelled()
    future_set_result_unless_cancelled(future, 42)
    assert not future.cancelled()
    assert future.done()
    assert future.result() == 42

    future = asyncio.Future()
    future.cancel()
    assert future.cancelled()
    assert future.done()
    future_set_result_unless_cancelled(future, 42)
    assert future.cancelled()
    assert future.done()

# Generated at 2022-06-14 11:58:08.319040
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import AsyncIOLoop

    class Foo(object):
        def __init__(self):
            self._executor = dummy_executor

        @run_on_executor()
        def f(self):
            return 5

        @run_on_executor(executor="_executor")
        def g(self):
            return 5

    class Bar(object):
        def __init__(self):
            self._executor = dummy_executor

        @run_on_executor(executor="_executor")
        def h(self):
            return 5

    class FutureTest(unittest.TestCase):
        def test_foo(self):
            foo = Foo()

# Generated at 2022-06-14 11:58:14.755762
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    result = None

    def get_result():
        # type: () -> None
        nonlocal result
        result = "my result"

    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future_add_done_callback(future1, get_result)
    future2.result()
    assert result == "my result"

# Generated at 2022-06-14 11:58:23.405632
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.testing import AsyncTestCase, gen_test

    class Test:
        executor = dummy_executor

        @run_on_executor
        def func(self, arg):
            return arg

    class TestNoExecutor:
        @run_on_executor
        def func(self, arg):
            return arg

    class TestAttr:
        _thread_pool = dummy_executor

        @run_on_executor(executor="_thread_pool")
        def func(self, arg):
            return arg

    class RunOnExecutorTest(AsyncTestCase):
        @gen_test
        def test(self):
            obj = Test()
            self.assertEqual(
                (yield obj.func(42)), 42
            )  # type: ignore