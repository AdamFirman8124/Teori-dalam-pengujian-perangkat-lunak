

# Generated at 2022-06-14 11:50:14.802711
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    loop = IOLoop.current()

    def error_callback(future):
        future_set_exc_info(future, sys.exc_info())

    def example_callback(future):
        future.set_result("result")

    def start_callback(future):
        # Test that a future can be chained to itself
        chain_future(future, future)
        # Test that a future can be chained to a second future, and
        # that the result can be modified in transit by an intervening
        # callback
        chain_future(future, second)
        future_add_done_callback(second, example_callback)


# Generated at 2022-06-14 11:50:22.224127
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import warnings

    from tornado.platform.asyncio import AsyncIOMainLoop

    try:
        from unittest import mock
    except ImportError:
        import mock

    from tornado import testing

    class ChainFutureTest(testing.AsyncTestCase):
        def setUp(self):
            super(ChainFutureTest, self).setUp()
            self.io_loop = self.new_ioloop()
            self.mock_callback = mock.Mock()
            AsyncIOMainLoop().install()

        def test_chaining(self):
            a = Future()
            b = Future()

            chain_future(a, b)
            b.add_done_callback(self.stop)

            self.assertFalse(b.done())
            a.set_result(42)

# Generated at 2022-06-14 11:50:25.235305
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future: Future[int] = Future()
    # cancelled Future could be safely added with exceptions
    future_set_exception_unless_cancelled(future, ZeroDivisionError(10, 0))
    if sys.version_info > (3, 5):
        # asyncio.InvalidStateError is only added since Python 3.5
        with future:
            pass


if __name__ == "__main__":
    test_future_set_exception_unless_cancelled()

# Generated at 2022-06-14 11:50:33.964396
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_result(42)
    assert g.result() == 42
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_exception(ValueError)
    try:
        g.result()
    except ValueError as e:
        assert e is not None


if hasattr(asyncio.Future, "__iter__"):
    FutureIter = typing.cast(
        Union[asyncio.Future[Any], futures.Future[Any]], asyncio.Future
    )

    FutureIter.__iter__ = typing.cast(
        Callable[[FutureIter], FutureIter], asyncio.Future.__iter__
    )



# Generated at 2022-06-14 11:50:37.742553
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop()
    io_loop.make_current()

    source = Future()
    dest = Future()
    chain_future(source, dest)

    source.set_result(42)
    io_loop.add_future(dest, lambda d: io_loop.stop())
    io_loop.start()
    assert dest.result() == 42



# Generated at 2022-06-14 11:50:45.859674
# Unit test for function run_on_executor
def test_run_on_executor():
    class Test:
        executor = dummy_executor

    @run_on_executor
    def f(self, x, y):
        assert self is test
        return x + y

    test = Test()
    result_future = f(test, 1, y=2)
    assert isinstance(result_future, Future)
    assert result_future.result() == 3

    @run_on_executor(executor="_other")
    def g(self):
        assert self is test
        return 42

    test._other = dummy_executor
    g_future = g(test)
    assert g_future.result() == 42



# Generated at 2022-06-14 11:51:00.007058
# Unit test for function run_on_executor
def test_run_on_executor():
    import tornado.ioloop

    class Example(object):
        def __init__(self):
            self.executor = dummy_executor
            self.running = False
            self.results = []  # type: List[str]

        @run_on_executor
        def run_something(self, x, y):
            self.running = True
            self.results.append(x)
            self.results.append(y)
            return "result " + x

        @run_on_executor(executor="_other_pool")
        def run_something_else(self, x, y):
            self.running = True
            self.results.append(x)
            self.results.append(y)
            return "result " + x

    example = Example()

# Generated at 2022-06-14 11:51:12.371011
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import unittest.mock
    import threading
    import concurrent.futures

    import tornado.ioloop
    import tornado.queues
    import tornado.platform.asyncio

    class Foo(object):
        def __init__(self):
            self.executor = concurrent.futures.ThreadPoolExecutor(2)

        @tornado.gen.coroutine
        def foo(self, x):
            return x + 1

        @run_on_executor
        def _blocking_foo(self, x):
            return x + 1

        @run_on_executor
        def _blocking_foo_exception(self, x):
            raise Exception("ouch")

        def _threaded_foo(self, x):
            self.t = threading.current_thread()
            raise

# Generated at 2022-06-14 11:51:14.869702
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = asyncio.Future()
    future.set_exception(RuntimeError())

    future_set_exception_unless_cancelled(future, ValueError())

# Generated at 2022-06-14 11:51:20.618201
# Unit test for function chain_future
def test_chain_future():
    # Issue #726
    # `chain_future` keeps a callback on the "a" future to set the result of
    # the "b" future. If the "b" future is cancelled, the callback should
    # be removed to avoid leaking the future.
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f2.cancel()
    del f2
    f1.set_result(None)
    # If chain_future is broken, the call above will produce a warning:
    # RuntimeWarning: coroutine was never awaited
    # See https://github.com/tornadoweb/tornado/issues/726 for more detail



# Generated at 2022-06-14 11:51:31.550855
# Unit test for function chain_future
def test_chain_future():
    f = Future()  # type: Future[int]
    g = Future()  # type: Future[int]
    chain_future(f, g)
    f.set_result(42)
    assert f.result() == g.result()

    h = Future()  # type: Future[int]
    chain_future(f, h)
    assert f.result() == h.result()

    f = Future()  # type: Future[int]
    g = Future()  # type: Future[int]
    chain_future(f, g)
    f.set_exception(ZeroDivisionError)
    try:
        f.result()
        assert False
    except ZeroDivisionError:
        pass
    try:
        g.result()
        assert False
    except ZeroDivisionError:
        pass




# Generated at 2022-06-14 11:51:38.900309
# Unit test for function chain_future
def test_chain_future():
    for CF in (concurrent.futures.Future, Future):
        f1 = CF()
        f2 = CF()
        chain_future(f1, f2)
        assert not f2.done()
        f1.set_result(42)
        assert f1.result() == 42 and f2.result() == 42
        f1 = CF()
        f2 = CF()
        chain_future(f1, f2)
        assert not f2.done()
        f1.set_exception(RuntimeError())
        assert f2.exception() is not None
        f1 = CF()
        f2 = CF()
        f2.set_result(42)
        chain_future(f1, f2)
        assert f2.result() == 42
        f1.set_result(24)


# Generated at 2022-06-14 11:51:42.813320
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    async def test_future_set_exception_unless_cancelled():
        future = Future()
        future.cancel()
        future_set_exc_info(future, sys.exc_info())
        assert future.exception() is None

# Generated at 2022-06-14 11:51:46.085322
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def f1(x):
        return x + 1
    with DummyExecutor() as x:
        assert x.submit(f1, 3).result() == 4

# Unit tests for function is_future

# Generated at 2022-06-14 11:51:51.572695
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.set_exception(ValueError('test'))
    assert future.exception() is not None
    assert future.cancelled() is False
    try:
        raise ValueError('other test')
    except:
        future_set_exc_info(future, sys.exc_info())
    assert future.exception() is not None
    assert isinstance(future.exception(), ValueError)
    assert future.exception().args == ('test',)


# Generated at 2022-06-14 11:52:03.042851
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase

    class TestChainFuture(AsyncTestCase):
        def setUp(self):
            super(TestChainFuture, self).setUp()
            self.executor = futures.ThreadPoolExecutor(1)

        @gen_test
        def test_chain_future(self):
            f1 = Future()
            f2 = Future()
            chain_future(f1, f2)
            f1.set_result(42)
            self.assertEqual(f2.result(), 42)

        @gen_test
        def test_chain_future_with_executor_callback(self):
            f1, f2 = yield [
                self.executor.submit(lambda: 42),
                self.executor.submit(lambda: 24),
            ]

# Generated at 2022-06-14 11:52:13.992305
# Unit test for function chain_future
def test_chain_future():
    import unittest

    from tornado.testing import AsyncTestCase

    class TestChainFuture(AsyncTestCase):
        def test(self):
            f1 = Future()
            f2 = Future()
            chain_future(f1, f2)
            f1.set_result(42)
            self.assertEqual(f2.result(), 42)
            f1 = Future()
            f2 = Future()
            chain_future(f1, f2)
            f1.set_exception(ValueError)
            self.assertRaises(ValueError, f2.result)

    unittest.main()



# Generated at 2022-06-14 11:52:18.065314
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    import time
    executor = DummyExecutor()
    future = executor.submit(time.sleep,1)
    # future.add_done_callback(lambda f: print(f.result()))
    # time.sleep(2)
    # print(future.done())


# Generated at 2022-06-14 11:52:31.767251
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase

    class TestFutureSetExceptionUnlessCancelled(AsyncTestCase):
        def test_future_set_exception_unless_cancelled(self):
            async_future_canceled = Future()
            async_future_canceled.cancel()

            future_set_exc_info(
                async_future_canceled,
                (None, Exception("Future was cancelled"), None),
            )

            future_set_exception_unless_cancelled(async_future_canceled, Exception())
            exc = self.assertRaises(Exception, async_future_canceled.result)
            self.assertIn("Future was cancelled", str(exc))

            f = Future()
            future_set_exception_unless_c

# Generated at 2022-06-14 11:52:34.568540
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future() # type: Future
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception())

# Generated at 2022-06-14 11:52:48.770087
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    with pytest.raises(RuntimeError):
        future.set_result(None)
    future_set_result_unless_cancelled(future, None)
    assert future.done()
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, None)
    assert future.cancelled()

# Generated at 2022-06-14 11:52:54.179587
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    class MyException(Exception):
        pass
    future = Future()
    try:
        raise MyException()
    except MyException:
        future_set_exception_unless_cancelled(future, sys.exc_info()[1])

    assert future.exception() is not None


if __name__ == "__main__":
    import unittest
    from tornado.log import enable_pretty_logging

    enable_pretty_logging()
    unittest.main()

# Generated at 2022-06-14 11:52:59.843368
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    future = Future()
    future_set_exception_unless_cancelled(future, RuntimeError())
    assert future.exception() is not None
    assert not future.cancelled()


# TODO: remove this once we no longer support Tornado <6.0

# Generated at 2022-06-14 11:53:09.553906
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class ChainFutureTest(AsyncTestCase):
        def setUp(self) -> None:
            super().setUp()
            self.executor = futures.ThreadPoolExecutor(1)

        def tearDown(self) -> None:
            self.executor.shutdown()
            super().tearDown()

        @run_on_executor()
        def blocking_func(self) -> int:
            return 42

        @gen_test
        def test_chain_future(self) -> None:
            # If a `concurrent.futures.Future` is returned from a
            # `.run_on_executor`-decorated method, it can be chained to an
            # `asyncio.Future`.
            cfut = self.blocking_func()


# Generated at 2022-06-14 11:53:11.473491
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def test_f():
        pass
    dummy = DummyExecutor()
    dummy.submit(test_f)

# Generated at 2022-06-14 11:53:17.820373
# Unit test for function chain_future
def test_chain_future():
    io_loop = asyncio.get_event_loop()

    def callback(future):
        assert result.result() == 42
        io_loop.stop()

    source = Future()
    source.set_result(42)
    result = Future()
    chain_future(source, result)
    future_add_done_callback(result, callback)
    io_loop.run_forever()



# Generated at 2022-06-14 11:53:26.123859
# Unit test for function chain_future
def test_chain_future():
    from tornado.platform.asyncio import to_asyncio_future
    from tornado import gen
    import asyncio

    @gen.coroutine
    def f(x: int) -> int:
        return x + 1

    def g(x: int) -> int:
        return x + 1

    @gen.coroutine
    def test_futures(loop: asyncio.AbstractEventLoop) -> None:
        c = Future()
        chain_future(c, c)
        c.set_result(1)
        v = yield c
        assert v == 1
        chain_future(to_asyncio_future(g(1), loop=loop), c)
        v = yield c
        assert v == 2


# Generated at 2022-06-14 11:53:35.275291
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.set_result(1)
    future_log = []

    def log(*args):
        future_log.extend(args)

    app_log.error = log
    future_set_exception_unless_cancelled(f, Exception())
    assert future_log == []
    f.cancel()
    future_set_exception_unless_cancelled(f, Exception())
    assert len(future_log) == 2
    assert "ERROR" in future_log[0]
    assert "Exception" in future_log[1]

# Generated at 2022-06-14 11:53:39.115012
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    future_set_result_unless_cancelled(f, 42)
    assert f.result() == 42
    f = Future()
    f.cancel()
    future_set_result_unless_cancelled(f, 42)

# Generated at 2022-06-14 11:53:52.698488
# Unit test for function chain_future
def test_chain_future():
    class TestException(Exception):
        pass

    def get_future(result):
        future = Future()
        future.set_result(result)
        return future

    def get_future_exc():
        future = Future()
        future.set_exception(TestException("exc"))
        return future

    def get_future_exc_info():
        future = Future()
        future.set_exc_info((TestException, TestException("exc"), None))
        return future

    # Test chaining 2 futures
    f1 = get_future(1)
    f2 = Future()
    chain_future(f1, f2)
    # f2 is chained to f1, so they should have the same result
    assert f1.result() == f2.result()

    # Test chaining 2 futures where f1 has an exception
   

# Generated at 2022-06-14 11:54:39.962023
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import tornado.ioloop
    import tornado.platform.asyncio

    io_loop = tornado.platform.asyncio.AsyncIOMainLoop()
    io_loop.make_current()
    tornado.ioloop.IOLoop.clear_current()

# Generated at 2022-06-14 11:54:52.269279
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.log import gen_log
    from tornado.ioloop import IOLoop

    def f1():
        future_set_exception_unless_cancelled(
            future_test, Exception("test")
        )

    def f2():
        future_set_exception_unless_cancelled(
            future_test, Exception("test2")
        )

    future_test = Future()
    ioloop = IOLoop.current()
    ioloop.add_callback(f1)
    ioloop.add_callback(f2)
    ioloop.run_sync(lambda: future_test)
    assert len(gen_log.error_logs) == 1
    assert gen_log.error_logs[0][2] == 'test'

    # The second exception is ignored as the future is

# Generated at 2022-06-14 11:54:54.857601
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    fut = Future()
    fut.cancel()
    future_set_exception_unless_cancelled(fut, Exception())

# Generated at 2022-06-14 11:54:58.201390
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    assert f.cancel()
    future_set_exception_unless_cancelled(f, Exception("test"))
    assert not f.cancelled()



# Generated at 2022-06-14 11:55:12.595120
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    # f1 -> f2
    f1.set_result(42)
    assert f2.result() == 42

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    # f1 -> f2
    f1.set_exception(ZeroDivisionError())
    assert f2.exception() is not None
    assert isinstance(f2.exception(), ZeroDivisionError)

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    # f1 -> f2
    f1.set_exception(ZeroDivisionError())

# Generated at 2022-06-14 11:55:21.021767
# Unit test for function chain_future
def test_chain_future():  # pragma: no cover
    import unittest2
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase, gen_test

    ioloop = IOLoop()

    @gen_test
    def test_future_chain():
        future1 = Future()
        future2 = Future()
        future3 = Future()

        chain_future(future1, future2)
        chain_future(future2, future3)

        future1.set_result(42)

        self.assertEqual(42, (yield future3))

    @gen_test
    def test_c_future_chain():
        future1 = futures.Future()
        future2 = Future()
        future3 = Future()

        chain_future(future1, future2)

# Generated at 2022-06-14 11:55:34.023667
# Unit test for function chain_future
def test_chain_future():
    # We can run this test without the IOLoop and without asyncio to
    # validate the fallback code path.
    try:
        from tornado.ioloop import IOLoop
        from asyncio import Future as AsyncioFuture  # type: ignore
    except ImportError:
        IOLoop = None
        AsyncioFuture = None

    # Check that the result of a is copied to b.
    for a, b in [
        (Future(), Future()),
        (asyncio.Future(), asyncio.Future()),
        (aiomultiprocess.Future(), aiomultiprocess.Future()),
    ]:
        chain_future(a, b)
        a.set_result(1)
        assert b.result() == 1

    # Check that exceptions are copied.

# Generated at 2022-06-14 11:55:40.705378
# Unit test for function chain_future
def test_chain_future():
    def func():
        return 1
    async_future = asyncio.Future()  # type: "Future[int]"
    conc_future = futures.Future()  # type: "futures.Future[int]"
    chain_future(conc_future, async_future)
    conc_future.set_result(func())
    assert async_future.result() == func()

# Generated at 2022-06-14 11:55:50.148617
# Unit test for function chain_future
def test_chain_future():
    import time

    f1 = Future()
    f2 = Future()

    f2.set_result(42)
    assert f2.result() == 42

    f1.set_result(42)
    assert f1.result() == 42
    assert f2.result() == 42

    f2 = Future()
    chain_future(f1, f2)
    assert not f1.done()
    assert not f2.done()
    f1.set_result(42)
    assert f1.result() == 42
    assert f2.result() == 42

    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f2.cancel()
    time.sleep(0.1)
    assert f1.done()
    assert f2.done()

# Generated at 2022-06-14 11:55:59.831803
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # The future should not raise an exception even if it was cancelled before
    future = Future()
    exc = Exception('test exception')
    future.cancel()
    future_set_exception_unless_cancelled(future, exc)

    # The future should raise an exception if it was not cancelled before
    future2 = Future()
    exc = Exception('test exception')
    try:
        future_set_exception_unless_cancelled(future2, exc)
        assert future2.exception() is exc
    except asyncio.InvalidStateError:
        assert False

# Generated at 2022-06-14 11:56:56.989100
# Unit test for function run_on_executor
def test_run_on_executor():
    import tornado.testing

    @run_on_executor
    def future_func():
        return 42

    @run_on_executor
    def future_func_with_self(self):
        return self.result

    class AnObject:
        executor = dummy_executor
        result = 43

        @run_on_executor
        def future_method(self):
            return self.result

    @run_on_executor(executor="_thread_pool")
    def future_func_with_arg(result):
        return result

    @run_on_executor(executor="_thread_pool")
    def future_func_with_kwarg(result=None):
        if result is None:
            return "DEFAULT"
        else:
            return result


# Generated at 2022-06-14 11:57:12.474688
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():

    future = Future()

    # Set result for an uncancelled future
    future_set_result_unless_cancelled(future, 0)
    assert future.done()

    # Set result for a cancelled future
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 0)
    assert future.cancelled()

    # Set result for an already done future
    future.set_result(0)
    future_set_result_unless_cancelled(future, 0)
    assert future.done()

# Generated at 2022-06-14 11:57:19.122959
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    # set_result should work if the Future is not cancelled
    future = Future()
    future_set_result_unless_cancelled(future, 42)
    assert future.result() == 42

    # set_result should not work if the Future is cancelled
    future = Future()
    future.cancel()
    with pytest.raises(asyncio.InvalidStateError):
        future.set_result(42)
    future_set_result_unless_cancelled(future, 42)
    assert future.cancelled()



# Generated at 2022-06-14 11:57:31.894278
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import tornado.testing
    import tornado.testing.gen_test

    future = Future()
    future.cancel()
    
    try:
        1/0
    except Exception:
        future_set_exception_unless_cancelled(future, sys.exc_info()[1])

    @tornado.testing.gen_test
    def test_gen():
        with tornado.testing.ExpectLog('ERROR','Exception after Future was cancelled'):
            try:
                yield future
            except Exception:
                pass
            
        future = Future()
        future.set_exception(Exception())
        
        with tornado.testing.ExpectLog('ERROR'):
            try:
                yield future
            except Exception:
                pass
        
if __name__ == "__main__":
    test_future_set_exception_

# Generated at 2022-06-14 11:57:37.072553
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    future_set_exception_unless_cancelled(f, Exception('test'))
    assert f.exception() is not None
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, Exception('test'))

# Generated at 2022-06-14 11:57:50.517287
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import time

    from tornado.platform.asyncio import AsyncIOMainLoop

    from tornado.testing import AsyncTestCase, gen_test

    class SomeClass:
        executor = dummy_executor

        @run_on_executor
        def func(self):
            return 42

    class SomeOtherClass:
        _thread_pool = dummy_executor

        @run_on_executor(executor='_thread_pool')
        def func(self):
            return 42

    class Foo(AsyncTestCase):
        def test_run_on_executor(self):
            obj = SomeClass()
            future = obj.func()
            self.assertEqual(42, future.result())

        def test_run_on_executor_keyword(self):
            obj = SomeOtherClass

# Generated at 2022-06-14 11:58:01.276997
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase, gen_test

    loop = IOLoop.current()

    f1 = Future()  # type: Future[str]
    f2 = Future()  # type: Future[None]
    chain_future(f1, f2)
    f1.set_result(42)
    self.assertTrue(f1.done())
    self.assertTrue(f2.done())
    self.assertTrue(f1.result() == 42)
    self.assertEqual(f1.result(), f2.result())
    self.assertEqual(f1.exception(), f2.exception())


# Generated at 2022-06-14 11:58:08.583092
# Unit test for function chain_future
def test_chain_future():
    from tornado.platform.asyncio import to_tornado_future
    from tornado.testing import gen_test

    @gen_test
    def test_chain_future():
        f = asyncio.Future()  # type: Future[str]
        f.set_result("future")

        tornado_f = to_tornado_future(f)
        chain_future(f, tornado_f)
        self.assertEqual("future", tornado_f.result())

    # Unit test for function future_add_done_callback
    @gen_test
    def test_future_add_done_callback():
        f = Future()
        f.set_result("future")

        future_add_done_callback(f, lambda f: setattr(self, "result", f.result()))

# Generated at 2022-06-14 11:58:18.644497
# Unit test for function chain_future
def test_chain_future():
    def handle_exception(typ, value, tb):
        if issubclass(typ, AssertionError):
            raise AssertionError("tornado.test.util_test.test_chain_future")
        print("caught %s: %s" % (typ.__name__, value))

    import sys
    sys.excepthook = handle_exception

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(None)
    assert f2.done()
    assert f2.result() is None



# Generated at 2022-06-14 11:58:29.503985
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
    try:
        1 / 0
    except ZeroDivisionError:
        f1.set_exc_info(sys.exc_info())
    assert f2.exc_info()[1].__class__ is ZeroDivisionError


# Unit tests for ``run_on_executor``.
#
# Note that many of these tests are commented out.  These tests are
# designed to only pass on CPython because of subtle differences in the
# timing of the stack frames containing local variables across different
# Python implementations (https://github.com/torn

# Generated at 2022-06-14 12:00:11.862089
# Unit test for function chain_future
def test_chain_future():
    def fail_future(future):
        future.set_exception(Exception("should never happen"))

    f1 = Future()
    f2 = Future()
    f1.add_done_callback(fail_future)
    chain_future(f1, f2)
    f2.add_done_callback(fail_future)
    f1.set_result(3)
    assert f2.result() == 3
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(KeyError)
    assert f2.exception() is not None
    assert isinstance(f2.exception(), KeyError)
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f2.cancel