

# Generated at 2022-06-14 11:50:14.981959
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, RuntimeError("testing"))

# Generated at 2022-06-14 11:50:17.305846
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop.current()
    io_loop.run_sync(lambda: chain_future(Future(), Future()))

# Generated at 2022-06-14 11:50:29.575331
# Unit test for function run_on_executor
def test_run_on_executor():
    import asyncio
    from tornado.ioloop import IOLoop
    import unittest

    class Foo(object):
        def __init__(self) -> None:
            self.executor = dummy_executor

        @run_on_executor
        def bar(self, a: int, b: int) -> int:
            return a + b

        @run_on_executor
        def baz(self, a: int, b: int, callback: Callable[[int], None]) -> None:
            callback(a + b)

    class TestRunOnExecutor(unittest.TestCase):
        def test_run_on_executor(self) -> None:
            io_loop = IOLoop()
            io_loop.make_current()
            future = Future()  # type: Future[int]
            foo

# Generated at 2022-06-14 11:50:39.732941
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def f(x):
        # type: (int) -> int
        return x + 1

    @chain_future
    def chain_future_func(future):
        # type: (Future) -> Future
        return future

    f1 = Future()
    f2 = Future()
    chain_future_func(f1, f2)
    f1.set_result(3)
    assert f2.result() == 4
    f1 = Future()
    f2 = Future()
    chain_future_func(f2, f1)
    f1.set_result(3)
    assert f2.result() == 4

# Generated at 2022-06-14 11:50:44.146588
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_result(42)
    assert f.result() == 42
    assert g.result() == 42
    h = Future()
    chain_future(f, h)
    assert h.result() == 42

# Generated at 2022-06-14 11:50:58.061286
# Unit test for function run_on_executor
def test_run_on_executor():

    import concurrent.futures
    import functools
    import time

    @run_on_executor
    def test_async_function(self):
        time.sleep(0.1)
        return "hello world"

    @run_on_executor
    def test_async_function_exception(self):
        time.sleep(0.1)
        raise Exception("pop")

    class TestClass(object):
        def __init__(self, pool: concurrent.futures.Executor) -> None:
            self.executor = pool

    pool = concurrent.futures.ThreadPoolExecutor(4)
    test_class = TestClass(pool)


# Generated at 2022-06-14 11:51:06.679008
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    """Tests the chain_future() method"""
    if hasattr(asyncio, "get_running_loop"):
        use_running_loop = asyncio.get_running_loop() is not None
    else:
        use_running_loop = (
            sys.version_info >= (3, 7)
            and asyncio.get_event_loop() is not None
            and asyncio.get_event_loop().is_running()
        )
    for loop in [None, asyncio.new_event_loop()]:
        if loop is None and use_running_loop:
            continue

# Generated at 2022-06-14 11:51:16.799960
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result("foo")
    assert b.result() == "foo"

    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_exception(Exception("foo"))
    # In Python 3, exceptions are not implicitly chained between Futures,
    # but in Python 2 the chain_future function does this for us to
    # avoid the thundering herd problem.
    assert not isinstance(b.exception(), Exception)

    a = futures.Future()
    b = Future()
    chain_future(a, b)
    a.set_exception(Exception("foo"))
    assert isinstance(b.exception(), Exception)

    a = Future()
    b = Future()
    chain

# Generated at 2022-06-14 11:51:29.993442
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.testing import AsyncTestCase, gen_test

    class FutureTests(AsyncTestCase):
        def setUp(self):
            super().setUp()
            self.io_loop.make_current()
            self.executor = futures.ThreadPoolExecutor(1)

        @run_on_executor
        def func(self, a, b):
            return a + b

        @run_on_executor(executor="executor")
        def keyword(self, a, b):
            return a + b

        def tearDown(self):
            self.executor.shutdown()
            self.io_loop.clear_current()
            super().tearDown()


# Generated at 2022-06-14 11:51:38.081240
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    io_loop = asyncio.get_event_loop()
    f = Future()
    f2 = Future()
    chain_future(f, f2)
    f.set_result(42)
    assert f2.result() == 42

    f = Future()
    f2 = Future()
    f.add_done_callback(lambda future: future_set_result_unless_cancelled(f2, 43))
    f.set_result(None)
    assert f2.result() == 43

    thread_pool = futures.ThreadPoolExecutor(1)
    f = Future()
    f2 = Future()
    chain_future(f, f2)
    thread_pool.submit(lambda: f.set_result(42)).result()
    assert f2.result() == 42



# Generated at 2022-06-14 11:51:50.134283
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    assert f.cancelled() is False
    future_set_result_unless_cancelled(f, 1)
    assert f.result() == 1
    f = Future()
    f.cancel()
    assert f.cancelled() is True
    future_set_result_unless_cancelled(f, 1)
    assert f.result() is None


# Generated at 2022-06-14 11:51:55.347863
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    future_set_exception_unless_cancelled(f, RuntimeError())
    assert isinstance(f.exception(), RuntimeError)

    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, RuntimeError())
    assert not f.cancelled()
    assert isinstance(f.exception(), RuntimeError)



# Generated at 2022-06-14 11:52:05.181995
# Unit test for function chain_future
def test_chain_future():

    class DummyFuture:
        def __init__(self, *args, **kwargs):
            self._result = _NO_RESULT
            self._exception = None
            self._done = False
            self._triggered_callbacks = []
            super().__init__(*args, **kwargs)

        def done(self):
            return self._done

        def result(self):
            return self._result

        def exception(self):
            return self._exception

        def set_result(self, result):
            self._result = result
            self._done = True
            self._trigger_callbacks()

        def set_exception(self, exception):
            self._exception = exception
            self._done = True
            self._trigger_callbacks()


# Generated at 2022-06-14 11:52:12.443071
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    if sys.version_info >= (3, 5, 2):
        # asyncio in 3.5.2 raises RecursionError instead of
        # RuntimeError.
        with pytest.raises(RecursionError):
            future_chain_future(Future(), Future())
    else:
        with pytest.raises(RuntimeError):
            future_chain_future(Future(), Future())

# Generated at 2022-06-14 11:52:21.045155
# Unit test for function run_on_executor
def test_run_on_executor():  # noqa
    class Foo(object):
        executor = dummy_executor

        def __init__(self):
            self.res = None  # type: Optional[int]
            self.exc_info = None  # type: Optional[Tuple[Optional[type], BaseException, Optional[types.TracebackType]]]

        @run_on_executor
        def synchronous(self, a, b, key=None):
            return key and a or b

        @run_on_executor
        def set_result(self, a):
            self.res = a

        @run_on_executor
        def set_exception(self):
            x = 1 / 0


# Generated at 2022-06-14 11:52:25.623778
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_result(42)
    assert future2.result() == 42



# Generated at 2022-06-14 11:52:36.895549
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import tornado.testing
    import tornado.test.util

    class Foo:
        @run_on_executor
        def bar(self):
            return 42

    foo = Foo()
    # Needs real executor, dummy_executor doesn't call callback
    foo.executor = tornado.test.util.UIModuleTest.executor
    # Also test all combinations of arg specs
    test = tornado.testing.gen_test(lambda self: None)
    test.maxDiff = None  # show full diff on error

    @gen.coroutine
    def check(x, y):
        future = foo.bar(x, y=y)
        self.assertIsInstance(future, Future)
        result = yield future
        self.assertEqual(result, 42)


# Generated at 2022-06-14 11:52:47.839859
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado import gen
    from tornado import ioloop

    @gen.coroutine
    def f():
        # type: () -> None
        yield gen.sleep(0.01)
        raise gen.Return(42)

    f2 = Future()  # type: Future[int]
    chain_future(f(), f2)
    assert f2.done()

    f3 = Future()  # type: Future[int]
    chain_future(f2, f3)
    ioloop.IOLoop.current().run_sync(lambda: f3)
    assert f3.result() == 42

# Generated at 2022-06-14 11:52:56.555844
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing

    def f(i, callback):
        callback(i)

    def g(r):
        return r * 2

    # Test a callback chain that ends with a synchronous function.
    # (The Future.chain_future documentation promises that this will work,
    # but this is not in the interface of Future itself.)
    tornado.testing.gen_test(lambda : (yield chain_future(
        dummy_executor.submit(f, 6, g),
        dummy_executor.submit(f, 7, g),
    ))).wait(timeout=1)
    # Test a callback chain that ends with an asynchronous function.

# Generated at 2022-06-14 11:53:03.887037
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    async def f_future(value):
        future = Future()
        future_set_result_unless_cancelled(future, value)
        return future
    async def f_concurrent(value):
        future = futures.Future()
        future_set_result_unless_cancelled(future, value)
        return future

    value = "value"
    assert (await f_future(value)).result() == value
    assert (await f_concurrent(value)).result() == value

# Generated at 2022-06-14 11:53:27.710447
# Unit test for function chain_future
def test_chain_future():
    loop = asyncio.get_event_loop()
    from tornado.platform.asyncio import AsyncIOLoop
    from tornado.platform.asyncio import to_asyncio_future  # type: ignore
    from tornado.platform.asyncio import to_tornado_future  # type: ignore
    from tornado.platform.asyncio import AsyncIOMainLoop  # type: ignore
    ioloop = AsyncIOLoop(loop)
    ioloop.make_current()

    futures = []  # type: typing.List[Union[futures.Future, Future]]
    for future_type in (futures.Future, Future):
        a = future_type()
        b = future_type()
        chain_future(a, b)
        futures.append((a, b))
    # Check that

# Generated at 2022-06-14 11:53:32.279464
# Unit test for function chain_future
def test_chain_future():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    @asyncio.coroutine
    def f():
        a = Future()
        b = Future()
        chain_future(a, b)
        a.set_result(42)
        assert 42 == (yield from b)
        a = Future()
        b = Future()
        loop.call_soon(a.set_result, 84)
        chain_future(a, b)
        assert 84 == (yield from b)

    loop.run_until_complete(f())

    loop.close()

# Generated at 2022-06-14 11:53:41.755547
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class TestFutureChaining(AsyncTestCase):
        def setUp(self):
            super(TestFutureChaining, self).setUp()
            self.result = None
            self.exception = None
            self.finished = False

        def _setResult(self, future):
            self.finished = True
            self.result = future.result()

        def _setException(self, future):
            self.finished = True
            self.exception = future.exception()

        @gen_test
        def test_chain(self):
            f = Future()
            g = Future()
            chain_future(f, g)
            f.set_result(42)
            result = yield g
            self.assertEqual(result, 42)


# Generated at 2022-06-14 11:53:47.201843
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    assert 1 == future.result()
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 1)
    assert future.cancelled()

# Generated at 2022-06-14 11:53:56.749985
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase, main

    class ChainFutureTest(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            f1 = Future()
            f2 = Future()
            f3 = Future()
            f4 = Future()

            chain_future(f1, f2)
            chain_future(f2, f3)
            chain_future(f3, f4)

            f1.set_result(None)
            yield f4
            self.assertTrue(f4.done())

        @gen_test
        def test_chain_future_exception(self):
            f1 = Future()
            f2 = Future()
            f3 = Future()
            f4 = Future()

            chain_future(f1, f2)
            chain

# Generated at 2022-06-14 11:54:09.593944
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    done_callback_args = []
    success_result = object()

    def done_callback(f):
        # type: (Future) -> None
        done_callback_args.append(f)

    async_future = Future()
    conc_future = futures.Future()
    chain_future(conc_future, async_future)

    assert not async_future.done()
    conc_future.set_result(success_result)
    assert async_future.done()
    assert async_future.result() is success_result

    async_future = Future()
    conc_future = futures.Future()
    chain_future(conc_future, async_future)

    assert not async_future.done()
    future_add_done_callback(async_future, done_callback)
    conc

# Generated at 2022-06-14 11:54:16.902936
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import unittest.mock
    import tornado.platform.asyncio
    import tornado.testing

    async def f():
        # type: () -> None
        fut = asyncio.Future()
        with unittest.mock.patch.object(fut, 'set_result') as set_result:
            chain_future(fut, async_future)

        assert not set_result.called, set_result.call_args_list
        async_future.set_result(42)
        assert set_result.call_args_list == [unittest.mock.call(42)]

    if asyncio is not tornado.platform.asyncio:
        # tornado.platform.asyncio is always available, even if it's overridden
        # by the system version.
        return

   

# Generated at 2022-06-14 11:54:23.538818
# Unit test for function chain_future
def test_chain_future():
    import time

    def f():
        time.sleep(0.1)
        return 1

    def f2():
        time.sleep(0.1)
        return 2

    executor = futures.ThreadPoolExecutor(2)
    f1 = Future()
    f3 = Future()
    executor.submit(f).add_done_callback(lambda future: future_set_result_unless_cancelled(f1, future.result()))
    f1.add_done_callback(lambda future: f3.set_result(future.result()))
    assert f3.result() == 1

    f1 = Future()
    f3 = Future()
    executor.submit(f2).add_done_callback(lambda future: f1.set_result(future.result()))

# Generated at 2022-06-14 11:54:29.841747
# Unit test for function chain_future
def test_chain_future():
    def f():
        future_set_result_unless_cancelled(future2, 1234)

    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_result(None)
    assert future2.result() is None
    chain_future(future1, future2)
    future1.set_exception(ReturnValueIgnoredError())
    future2.result()
    chain_future(future1, future2)
    future2.cancel()
    chain_future(future1, future2)
    future_add_done_callback(future1, f)
    assert future2.result() == 1234

# Generated at 2022-06-14 11:54:33.115865
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, RuntimeError("foo"))
    assert future.cancelled()

# Generated at 2022-06-14 11:55:00.048549
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    class DummyException(Exception):
        pass

    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, DummyException())

# Generated at 2022-06-14 11:55:13.813350
# Unit test for function run_on_executor
def test_run_on_executor():  # noqa: F811
    import unittest.mock
    from tornado.ioloop import IOLoop

    class FakeFuture(Future):
        def __init__(self) -> None:
            self.done_callbacks = []  # type: typing.List[Callable[[], None]]

        def add_done_callback(self, callback: Callable[["Future[_T]"], None]) -> None:
            self.done_callbacks.append(callback)

        def set_result(self, result: _T) -> None:
            for cb in self.done_callbacks:
                cb(self)

    class Test(object):
        def __init__(self) -> None:
            self.executor = unittest.mock.Mock()

# Generated at 2022-06-14 11:55:21.909972
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class DummyFuture(Future):
        def cancel(self) -> bool:
            return False

    class TestChaining(AsyncTestCase):
        def test_chain(self):
            f1 = DummyFuture()
            f2 = DummyFuture()
            chain_future(f1, f2)
            self.assertFalse(f2.done())

            f1.set_result(42)
            self.assertEqual(f2.result(), 42)

        def test_chain_exception(self):
            f1 = DummyFuture()
            f2 = DummyFuture()
            chain_future(f1, f2)
            self.assertFalse(f2.done())

            f1.set_exception(RuntimeError())

# Generated at 2022-06-14 11:55:34.637852
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import unittest
    from unittest.mock import Mock

    from tornado.util import timedelta_to_seconds

    from .platform.asyncio import AsyncIOMock, AsyncIOSelftest

    class FutureTest(unittest.TestCase):
        def test_chain_future(self):
            # type: () -> None
            loop = AsyncIOMock()
            loop.time = Mock(return_value=5)
            loop.call_later = Mock()
            future1 = Future()
            future1.add_done_callback = Mock()
            future1.set_result = Mock()
            future1.set_exception = Mock()
            future2 = Future()
            future2.add_done_callback = Mock()
            future2.set_result = Mock

# Generated at 2022-06-14 11:55:45.451380
# Unit test for function chain_future
def test_chain_future():
    import unittest

    class FutureTest(unittest.TestCase):
        def test_chain_future(self):
            io_loop = IOLoop.current()

            def f():
                return 42

            f1 = Future()
            f2 = Future()
            chain_future(f1, f2)
            self.assertFalse(f2.done())
            f1.set_result(f())
            io_loop.add_future(f2, lambda f: self.assertEqual(f.result(), 42))
            io_loop.start()

    unittest.main()

# Generated at 2022-06-14 11:55:47.482042
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    x = 1
    y = 2
    async_future = dummy_executor.submit(lambda a, b: a + b, x, y)
    assert async_future.result() == 3

# Generated at 2022-06-14 11:55:52.305754
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()

    class MyError(Exception):
        pass

    try:
        future_set_exception_unless_cancelled(f, MyError("error message"))
    except MyError:
        raise Exception("should log and ignore exception")

# Generated at 2022-06-14 11:56:05.240637
# Unit test for function chain_future
def test_chain_future():

    from tornado.testing import gen_test, AsyncTestCase

    class TestChainFuture(AsyncTestCase):
        @gen_test
        async def test_chain_future_make_sure_this_future_is_done(self):
            a = Future()
            b = Future()
            chain_future(a, b)
            a.set_result(None)
            await b

    test = TestChainFuture()
    test.test_chain_future_make_sure_this_future_is_done()
    test.test_chain_future_make_sure_this_future_is_done()
    test.test_chain_future_make_sure_this_future_is_done()
    for i in range(100):
        test.test_chain_future_make_sure_this_future_is_done()
    test

# Generated at 2022-06-14 11:56:16.893515
# Unit test for function chain_future
def test_chain_future():
    result = []  # type: List[str]
    f1, f2 = Future(), Future()
    chain_future(f1, f2)
    f2.add_done_callback(lambda f: result.append("f2 done"))
    f1.set_result(42)
    assert result == ["f2 done"]
    f3 = Future()
    chain_future(f2, f3)
    f3.add_done_callback(lambda f: result.append("f3 done"))
    assert result == ["f2 done", "f3 done"]

    # Test return values of former Future.chain()
    assert f1.result() == 42
    assert f2.result() == 42
    assert f3.result() == 42



# Generated at 2022-06-14 11:56:23.263566
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    assert not f.cancelled()
    future_set_result_unless_cancelled(f, 1)
    f.cancel()
    future_set_result_unless_cancelled(f, 2)
    assert f.result() == 1



# Generated at 2022-06-14 11:57:19.896028
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()  # type: Future
    f2 = Future()  # type: Future
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42
    f1 = Future()  # type: Future
    f2 = Future()  # type: Future
    chain_future(f1, f2)
    f1.set_exception(RuntimeError())
    f2.exception()  # re-raises the exception
    f1 = Future()  # type: Future
    f2 = Future()  # type: Future
    chain_future(f1, f2)
    f2.set_result(40)
    f1.set_result(2)
    assert f2.result() == 40

# Generated at 2022-06-14 11:57:25.490493
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 10)
    assert 10 == future.result()

    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 10)
    assert future.cancelled()

# Generated at 2022-06-14 11:57:28.675555
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    # type: () -> None
    import pytest
    future = dummy_executor.submit( sum, (1,2,3) )
    assert future.result() == 6

# Generated at 2022-06-14 11:57:39.077531
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    # f1 completed before chain_future
    f1.set_result('f1.result')
    assert f2.result() == 'f1.result'

    # f1 completed after chain_future
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result('f1.result')
    assert f2.result() == 'f1.result'

    # f1 get result from f2
    f1 = Future()
    f2 = Future()
    chain_future(f2, f1)
    f2.set_result('f2.result')
    assert f1.result() == 'f2.result'

    # f1

# Generated at 2022-06-14 11:57:44.016775
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, ValueError("test"))
    assert isinstance(f.exception(), ValueError)
    assert f.exception().args == ("test",)

# Generated at 2022-06-14 11:57:55.292298
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase, gen_test
    import time
    import unittest

    class DummyExecutorTest(AsyncTestCase):
        @gen_test
        def test_submit(self):
            async_future = DummyExecutor().submit(lambda: 'replace_me')
            self.assertEqual((yield async_future), 'replace_me')

        @gen_test
        def test_submit_exception(self):
            async_future = DummyExecutor().submit(lambda: 1 / 0)
            with self.assertRaises(ZeroDivisionError):
                yield async_future

        @gen_test
        def test_submit_asyncio_future(self):
            async_future = DummyExecutor().submit(asyncio.Future)

# Generated at 2022-06-14 11:58:05.772002
# Unit test for function chain_future
def test_chain_future():
    import unittest

    from tornado import ioloop
    from tornado import testing

    class TestChainFuture(testing.AsyncTestCase):
        def test_main(self):
            f1 = Future()
            f2 = Future()
            f1.set_result(1)
            chain_future(f1, f2)
            self.assertEqual(1, f2.result())

            f1 = Future()
            f2 = Future()
            f1.set_exception(ValueError())
            chain_future(f1, f2)
            try:
                f2.result()
            except ValueError:
                pass
            else:
                self.fail("did not propagate exception")

            f1 = Future()
            f2 = Future()
            f3 = Future()

# Generated at 2022-06-14 11:58:17.680262
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import concurrent.futures
    import tornado.ioloop
    import tornado.testing
    import tornado.platform.asyncio

    class TestRunOnExecutor(tornado.testing.AsyncTestCase):
        def test_without_instance(self):
            with self.assertRaises(ValueError):
                run_on_executor(executor="_pool")
        def test_with_method(self):
            # TODO: should this test be allowed?
            def fn():
                pass
            self.assertRaises(AttributeError, run_on_executor, fn)
        def test_no_executor(self):
            class Foo(object):
                @run_on_executor
                def foo(self):
                    return 42
            f = Foo()
            f.foo().add_done_callback

# Generated at 2022-06-14 11:58:28.042459
# Unit test for function chain_future
def test_chain_future():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.Future()
    assert not future.done()
    future2 = asyncio.Future()
    assert not future2.done()
    chain_future(future, future2)
    assert not future.done()
    assert not future2.done()

    future.set_result(42)
    assert future.done()
    assert future2.done()
    assert future2.result() == 42

    future = asyncio.Future()
    assert not future.done()
    future2 = asyncio.Future()
    assert not future2.done()
    chain_future(future, future2)
    assert not future.done()
    assert not future2.done()


# Generated at 2022-06-14 11:58:34.531541
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # Test case for tornado.ioloop.IOLoop
    try:
        from tornado.ioloop import IOLoop
    except ImportError:
        pass
    else:
        future = Future()
        future.cancel()
        future_set_exception_unless_cancelled(future, ValueError())