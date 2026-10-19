

# Generated at 2022-06-14 11:50:13.203556
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    assert b.result() == 42
    assert a.result() == 42

    a = Future()
    b = Future()
    a.set_exception(RuntimeError())
    chain_future(a, b)
    with b:
        pass  # b should already be finished

    a = Future()
    b = Future()
    b.set_result(42)
    chain_future(a, b)
    assert b.result() == 42
    a.set_result(84)
    assert b.result() == 42
    assert a.result() == 84

# Generated at 2022-06-14 11:50:21.676485
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import time

    from tornado import gen
    from tornado.concurrent import Future
    from tornado.ioloop import IOLoop

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.executor = dummy_executor
            self.executor_result_value = None
            self.executor_result_future = Future()

            def executor_result_func():
                # simulate some long-running computation
                time.sleep(0.001)
                if isinstance(self.executor_result_value, Exception):
                    raise self.executor_result_value
                else:
                    return self.executor_result_value

            self.executor_result_func = executor_result_func

        def tearDown(self):
            self.executor.shutdown()

# Generated at 2022-06-14 11:50:31.114951
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    def foo():
        yield gen.moment

    @gen.coroutine
    def baz(x: int) -> int:
        yield gen.moment
        raise gen.Return(x)

    class MyAsyncTestCase(AsyncTestCase):
        def setUp(self):
            super().setUp()
            self.executor = futures.ThreadPoolExecutor(1)

        def tearDown(self):
            super().tearDown()
            self.executor.shutdown()

        @run_on_executor(executor="executor")
        def bar(self, x: int) -> int:
            self.assertIn("test_chain_future", sys._getframe(1).f_code.co_name)
            return x


# Generated at 2022-06-14 11:50:37.025639
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    import asyncio

    def test_method(value):
        return value

    async def test_method2(value):
        return value

    dummy = DummyExecutor()
    future = dummy.submit(test_method, "test")
    # The test_method raises no exception
    assert future.exception() == None

    future2 = dummy.submit(test_method2, asyncio.sleep(1.0))
    # The test_method2 raises an exception
    assert future2.exception() != None

# Generated at 2022-06-14 11:50:43.233949
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    assert not future.cancelled()
    future_set_result_unless_cancelled(future, True)
    assert future.result() is True

    future = Future()
    future.cancel()
    assert future.cancelled()
    future_set_result_unless_cancelled(future, True)

# Generated at 2022-06-14 11:50:52.619980
# Unit test for function chain_future
def test_chain_future():

    def pick_result(fut: "Union[futures.Future[_T], Future[_T]]") -> str:
        if hasattr(fut, "exc_info") and fut.exc_info() is not None:  # type: ignore
            exc, out, _ = fut.exc_info()  # type: ignore
            if hasattr(out, "strerror") and out.strerror is not None:  # type: ignore
                return out.strerror  # type: ignore
            else:
                return str(exc)
        else:
            return str(fut.exception())

    def callback(fut: "Future[str]") -> None:
        assert isinstance(fut, Future)
        assert fut.exception() is None
        assert fut.result() == "test"

    f1 = Future

# Generated at 2022-06-14 11:51:02.192352
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    # A function to use as the target of the chain_future call
    def async_function(arg):
        # type: (int) -> int
        return arg + 1

    # Create the future that will be passed to chain_future
    f = Future()  # type: Future[int]
    f.set_result(1)

    # Create the future that will be returned by chain_future
    result_future = Future()  # type: Future[int]

    # Call chain_future
    chain_future(f, result_future)

    # Confirm that the result_future has the same result as f
    assert result_future.result() == 2

# Generated at 2022-06-14 11:51:14.276970
# Unit test for function chain_future
def test_chain_future():
    result = None
    error = None

    def callback(future):
        nonlocal result, error
        if future.exception() is not None:
            error = future.exception()
        else:
            result = future.result()

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    future_add_done_callback(f2, callback)
    f1.set_result(42)
    assert result == 42

    result = error = None

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    future_add_done_callback(f2, callback)
    f1.set_exception(ValueError())
    assert isinstance(error, ValueError)

    result = error = None

    f2 = Future

# Generated at 2022-06-14 11:51:21.036283
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase

    class TestChainFuture(AsyncTestCase):
        def test_chain_future(self):
            f = Future()
            f2 = Future()
            chain_future(f, f2)
            self.assertTrue(f.done())
            self.assertTrue(f2.done())
            self.assertTrue(f2.exception())
            self.assertEqual(type(f2.exception()), RuntimeError)
            self.assertEqual(f2.exception().args[0], "exception")
            f = Future()
            f2 = Future()
            chain_future(f, f2)
            f.set_exception(RuntimeError("exception"))
            self.assertTrue(f.done())

# Generated at 2022-06-14 11:51:26.799624
# Unit test for function run_on_executor
def test_run_on_executor():
    class MyClass(object):
        def __init__(self):
            self.executor = dummy_executor

        @run_on_executor
        def method(self):
            return 12

    myobj = MyClass()
    myobj.method().result() == 12
    assert isinstance(myobj.method(), futures.Future)



# Generated at 2022-06-14 11:51:37.759058
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def fail(exc: BaseException) -> None:
        raise exc

    def check(test, f1, f2):
        # type: (Any, Future[int], Union[Future[int], Future[str]]) -> None
        if sys.version_info >= (3, 5):
            test.assertIs(f1, f2)  # type: ignore
        if isinstance(f1, Future):
            f1.add_done_callback(lambda f: f.result())
            f1.add_done_callback(lambda f: fail(f.exception()))
        else:
            f1.add_done_callback(lambda f: f.result())
            f1.add_done_callback(lambda f: fail(f.exception()))

    f1 = Future()  # type

# Generated at 2022-06-14 11:51:44.702946
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import concurrent.futures
    import tornado.testing
    import tornado.testing

    @tornado.testing.gen_test
    def test():
        executor = concurrent.futures.ThreadPoolExecutor(2)
        f = executor.submit(lambda: 1 + 1)
        f2 = Future()
        chain_future(f, f2)
        assert (yield f2) == 2

    unittest.main()


# Generated at 2022-06-14 11:51:48.171292
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future1 = Future()
    future2 = Future()
    future2.cancel()

    future_set_exception_unless_cancelled(future1, Exception())
    future_set_exception_unless_cancelled(future2, Exception())

# Generated at 2022-06-14 11:51:59.598646
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    @gen_test
    def _test(chain_future, func, a_class, b_class):
        a = a_class()
        b = b_class()

        chain_future(a, b)
        func(a)
        yield b
        self.assertEqual(b.result(), 42)

    class OldFuture(object):
        def __init__(self):
            self._callback = None
            self._result = None
            self._exc_info = None

        def add_done_callback(self, callback):
            self._callback = callback

        def set_result(self, result):
            self._result = result
            if self._callback is not None:
                self._callback(self)


# Generated at 2022-06-14 11:52:04.336901
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.testing import AsyncTestCase, gen_test

    class Foo:
        executor = dummy_executor

        @run_on_executor
        def bar(self, x: int, y: int) -> int:
            return x * y

    @gen_test
    def f() -> None:
        foo = Foo()
        result = yield foo.bar(3, 5)
        assert result == 15

    f()

# Generated at 2022-06-14 11:52:12.288450
# Unit test for function run_on_executor
def test_run_on_executor():
    class Foo(object):
        executor = dummy_executor

        @run_on_executor
        def callback(self, arg):
            return arg

        @run_on_executor(executor="_thread_pool")
        def callback_with_keywords(self, arg):
            return arg

    f = Foo()
    f.callback(42).result()
    f.callback_with_keywords(42).result()



# Generated at 2022-06-14 11:52:19.291958
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception())
    assert future.exception() is not None
    assert future.cancelled() is False
    future_set_result_unless_cancelled(future, 0)
    assert future.exception() is not None
    assert future.cancelled() is False

    future = Future()
    future_set_result_unless_cancelled(future, 0)
    assert future.exception() is None
    future_set_exception_unless_cancelled(future, Exception())
    assert future.exception() is None

# Generated at 2022-06-14 11:52:32.377356
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.platform.asyncio import AsyncIOMainLoop
    import logging
    import unittest

    asyncio.get_event_loop().close()

    class TestFutureSetExceptionUnlessCancelled(unittest.TestCase):
        def setUp(self):
            AsyncIOMainLoop().install()

            # Replace the root logger with a test logger
            root_logger = logging.getLogger()
            root_logger.handlers = []
            self.test_logger = logging.getLogger('test logger')
            self.test_logger.setLevel(logging.INFO)
            self.test_logger_handler = logging.StreamHandler()
            self.test_logger_handler.setLevel(logging.INFO)

# Generated at 2022-06-14 11:52:36.962158
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 'foo')
    assert future.result() == 'foo'

    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 'bar')
    assert future.cancelled()



# Generated at 2022-06-14 11:52:45.440851
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from unittest import mock
    from tornado import gen
    from tornado.concurrent import Future

    async def main():
        f = Future()
        future_set_exception_unless_cancelled(f, ValueError())
        assert f.exception() is not None

    mocked_log = mock.Mock()
    with mock.patch("tornado.log.app_log", mocked_log):
        gen.coroutine(main)()

    assert not mocked_log.called

# Generated at 2022-06-14 11:53:03.298903
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    from tornado.testing import AsyncTestCase, gen_test

    class Test(AsyncTestCase):
        @gen_test
        async def test_future_set_result_unless_cancelled(self) -> None:
            future1 = Future()
            self.assertFalse(future1.done())
            # simulate a cancelled future
            future1.cancel()
            self.assertTrue(future1.done())
            future_set_result_unless_cancelled(future1, "hello")
            with self.assertRaises(asyncio.CancelledError):
                result = await future1
            future2 = Future()
            future_set_result_unless_cancelled(future2, "hello")
            result = await future2
            self.assertEqual(result, "hello")

    test = Test()
    test

# Generated at 2022-06-14 11:53:11.374740
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def callback(future):
        # type: (futures.Future) -> None
        future.result()

    future = Future()
    b = Future()
    chain_future(future, b)
    future.set_result(None)
    assert b.done() is True
    # Test that chaining works even if the callback was added after the first
    # future was finished.
    future = Future()
    b = Future()
    future.set_result(None)
    chain_future(future, b)
    assert b.done() is True

    future = futures.Future()
    b = Future()
    chain_future(future, b)
    future.set_result(None)
    assert b.done() is True

    # Test that calling result() raises an exception on the chained future


# Generated at 2022-06-14 11:53:21.690630
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    f2 = Future()
    chain_future(f, f2)
    f.set_result(1)
    assert f.result() == 1
    assert f2.result() == 1

    f = Future()
    f2 = Future()
    chain_future(f, f2)
    f.set_exception(RuntimeError())
    assert f2.exception() is f.exception()  # type: ignore

    f = Future()
    f2 = Future()
    chain_future(f, f2)
    f.set_result(1)
    f2.cancel()
    assert f2.cancelled()
    assert f2.exception() is None

# Generated at 2022-06-14 11:53:28.734353
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(None)

    async def go():
        future = asyncio.Future()
        future_set_exception_unless_cancelled(future, ValueError('x'))
        assert future.done()
        try:
            future.result()
        except ValueError as e:
            assert str(e) == 'x'
        else:
            assert False, 'should not fail'

        future = asyncio.Future()
        future.cancel()
        future_set_exception_unless_cancelled(future, ValueError('x'))
        assert future.done()
        assert future.cancelled()

        future = asyncio.Future()
        future.set_exception(ValueError('y'))
        future_set_ex

# Generated at 2022-06-14 11:53:40.043388
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import time
    import threading

    from tornado.ioloop import IOLoop

    class SyncHandler(object):
        executor = dummy_executor

        @run_on_executor
        def sync_method(self):
            return 42

    class AsyncHandler(object):
        executor = dummy_executor

        @run_on_executor
        def async_method(self, callback):
            IOLoop.current().add_callback(lambda: callback(42))

        @run_on_executor
        def sync_method(self, callback):
            callback(42)

    class MyTestCase(unittest.TestCase):
        def setUp(self):
            self.io_loop = IOLoop()
            self.io_loop.make_current()


# Generated at 2022-06-14 11:53:48.326696
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def my_fun(x, y, z=3):
        return (x + y) * z

    fut = dummy_executor.submit(my_fun, 1, 2)
    print("my_fun(1, 2) done!")
    print("fut={}".format(fut))
    if fut.done() and not fut.cancelled():
        print("result={}".format(fut.result()))

test_DummyExecutor_submit()

# Generated at 2022-06-14 11:53:57.113472
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    class HelperError(Exception):
        pass

    class Helper:
        def __init__(self):
            self.f = Future()

        def test_set_exc(self):
            try:
                1/0
            except Exception:
                future_set_exception_unless_cancelled(self.f, HelperError())

        def test_set_exc_cancelled(self):
            self.f.cancel()
            future_set_exception_unless_cancelled(self.f, HelperError())

        def test_set_exc_traceback(self):
            try:
                self.test_set_exc()
            except Exception:
                future_set_exception_unless_cancelled(self.f, sys.exc_info())


# BEGIN backports from asyncio/f

# Generated at 2022-06-14 11:54:03.181994
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def fn(a, b):
        return a + b
    async def async_fn(a, b):
        return fn(a, b)
    assert dummy_executor.submit(fn, 1, 2).result() == 3
    assert dummy_executor.submit(async_fn, 1, 2).result() == 3


# Generated at 2022-06-14 11:54:10.243896
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        f1 = Future()
        f2 = Future()
        chain_future(f1, f2)
        f1.set_result(42)
        assert f2.result() == 42
    finally:
        loop.close()
        asyncio.set_event_loop(None)



# Generated at 2022-06-14 11:54:16.699167
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()
    f2 = Future()

    def copy(f):
        # type: (Future) -> None
        assert f is f1
        f2.set_result(f1.result())

    chain_future(f1, f2)
    f1.set_result(123)
    assert f2.result() == 123

    f3 = Future()
    f4 = Future()
    chain_future(f3, f4)
    f3.set_exception(ValueError('foo'))
    try:
        f4.result()
    except ValueError as e:
        assert str(e) == "foo"
    else:
        assert False, "should have raised"

# Generated at 2022-06-14 11:54:34.134881
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    async def f():
        # type: () -> None
        f1 = Future()  # type: Future[int]
        f2 = Future()  # type: Future[int]
        chain_future(f1, f2)
        f1.set_result(42)
        assert (await f2) == 42

    run_sync(f())

# Generated at 2022-06-14 11:54:42.528605
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_result(42)
    assert g.result() == 42

    f2 = Future()
    g2 = Future()
    chain_future(g2, f2)
    f2.set_result(24)
    assert g2.result() == 24

    f3 = Future()
    g3 = Future()
    chain_future(f3, g3)
    f3.set_result(10)
    g3.set_result(20)
    assert g3.result() == 20



# Generated at 2022-06-14 11:54:45.079836
# Unit test for function chain_future
def test_chain_future():
    loop = asyncio.get_event_loop()
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    loop.run_until_complete(f1)
    assert not f2.done()

    f1.set_result(42)
    loop.run_until_complete(f2)
    assert f2.result() == 42
    loop.close()

# Generated at 2022-06-14 11:54:57.423614
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import unittest
    import logging
    import tornado.log

    class HandlerMock(tornado.log.AppLogFormatter):
        def __init__(self):
            self.record = None

        def emit(self, record):
            self.record = record

    logger_name = 'tornado.test.test_util.test_future_set_exception_unless_cancelled'
    logger = logging.getLogger(logger_name)
    logger.propagate = 0
    handler = HandlerMock()
    logger.addHandler(handler)
    test_exception = RuntimeError('test_exception')

    # test with an asyncio Future that was not cancelled
    future = Future()
    future_set_exception_unless_cancelled(future, test_exception)

# Generated at 2022-06-14 11:55:01.279132
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def callback(f):
        # type: (Futures[_T]) -> None
        pass

    # Make sure the decorator doesn't raise exceptions
    run_on_executor()
    run_on_executor(callback)
    run_on_executor(executor='_thread_pool')

# Generated at 2022-06-14 11:55:09.479092
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    result = "result"

    async def a_future(future):
        future_set_result_unless_cancelled(future, result)
        return

    future = Future()
    future.cancel()
    try:
        future.set_result(result)
    except Exception:
        pass
    else:
        raise Exception("Future.set_result should fail if the future was cancelled")


# Generated at 2022-06-14 11:55:18.481198
# Unit test for function chain_future
def test_chain_future():
    def void_callback(_):
        pass

    # Test F1. result -> F2
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    f1.set_result(None)
    test_future(f1, done=True, result=None)
    test_future(f2, done=True, result=None)

    # Test F1. exception -> F2
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    e = Exception()
    f1.set_exception(e)
    test_future(f1, done=True, exception=e)
    test_future(f2, done=True, exception=e)

    # Test F1. done after chain -> F2

# Generated at 2022-06-14 11:55:23.238393
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    assert f.cancelled() == False
    f.cancel()
    assert f.cancelled() == True
    future_set_result_unless_cancelled(f, "result")
    assert f.cancelled() == True
    assert f.result() == None


# Generated at 2022-06-14 11:55:33.847693
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    future_set_result_unless_cancelled(f, 3)
    assert f.result() == 3

    future_set_result_unless_cancelled(f, 4)
    assert f.result() == 3

    f = Future()
    f.cancel()
    future_set_result_unless_cancelled(f, 3)
    assert f.cancelled()
    assert not f.done()

    future_set_result_unless_cancelled(f, 4)
    assert f.cancelled()
    assert not f.done()



# Generated at 2022-06-14 11:55:43.842754
# Unit test for function run_on_executor
def test_run_on_executor():
    class T:
        executor = dummy_executor

        @run_on_executor
        def f(self):
            return 1

        @run_on_executor(executor="thr")
        def g(self):
            return 2

        def __init__(self):
            self.thr = dummy_executor

    t = T()
    assert tornado.ioloop.IOLoop.current().run_sync(t.f) == 1
    assert tornado.ioloop.IOLoop.current().run_sync(t.g) == 2

# Generated at 2022-06-14 11:56:10.050219
# Unit test for function chain_future
def test_chain_future():
    # The chain_future method is tested by the test suite for
    # concurrent.futures.Future objects, and by the Future test suite.
    pass

# Generated at 2022-06-14 11:56:12.619266
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception())
    assert future.exception()

# Generated at 2022-06-14 11:56:15.485875
# Unit test for function chain_future
def test_chain_future():
    future = Future()
    future2 = Future()
    chain_future(future, future2)
    future.set_result(42)
    assert future2.result() == 42



# Generated at 2022-06-14 11:56:26.026581
# Unit test for function run_on_executor
def test_run_on_executor():
    import mock
    import time

    ioloop = mock.MagicMock()
    executor = mock.MagicMock()

    class Obj(object):
        def __init__(self, ioloop=ioloop, executor=executor):
            self.called = False
            self.io_loop = ioloop
            self.executor = executor

        @run_on_executor
        def sync(self):
            self.called = True

    obj = Obj()
    obj.sync()

    assert obj.called
    assert obj.executor.submit.called
    executor.submit.assert_called_with(obj.sync, obj)

    executor.submit.reset_mock()

    obj = Obj()
    future2 = obj.sync()
    assert isinstance(future2, Future)
    future2

# Generated at 2022-06-14 11:56:38.281640
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ValueError("foo"))
    with pytest.raises(ValueError, match="foo"):
        f2.result()
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)  # test that no exception is raised
    f1.cancel()
    assert f1.cancelled()
    assert f2.cancelled()


if __name__ == "__main__":
    import logging

   

# Generated at 2022-06-14 11:56:55.097999
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result("f1 result")
    assert f2.result() == "f1 result"

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ZeroDivisionError("f1 error"))
    assert f1.exception() is not None
    assert f2.exception() is not None
    assert type(f2.exception()) is ZeroDivisionError

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f2.set_result("f2 result")
    f1.set_result("f1 result")

# Generated at 2022-06-14 11:56:57.379010
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.cancel()
    with app_log.catch_logging():
        future_set_exception_unless_cancelled(future, RuntimeError("test"))

# Generated at 2022-06-14 11:57:13.868851
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)

    assert not future1.done()
    assert not future2.done()

    future1.set_result(None)
    assert future1.done()
    assert future2.done()

    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future2.cancel()
    assert future2.cancelled()

    future1.set_result(None)
    assert future1.done()
    assert future2.done()
    assert future2.cancelled()

# Generated at 2022-06-14 11:57:21.262539
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    g = Future()
    chain_future(f, g)

    g.result()

    assert g.done()
    assert not g.cancelled()
    assert g.exception() is None

    def callback():
        g.set_result(42)

    f.add_done_callback(callback)
    f.set_result(None)
    assert f.done()
    assert g.done()
    assert g.result() == 42

    f = Future()
    g = Future()
    chain_future(f, g)

    f.set_exception(ValueError())
    assert f.done()
    assert g.done()
    assert isinstance(g.exception(), ValueError)

    f = Future()
    g = Future()
    chain_future(f, g)



# Generated at 2022-06-14 11:57:35.193106
# Unit test for function chain_future
def test_chain_future():
    from concurrent.futures import Future as CFuture
    from asyncio import Future as AFuture
    from tornado.platform.asyncio import to_asyncio_future, to_tornado_future
    for f1 in (CFuture(), AFuture()):
        for f2 in (CFuture(), AFuture()):
            chain_future(f1, f2)
            f1.set_result("foo")
            assert f2.result() == "foo"
            if isinstance(f1, AFuture):
                assert to_tornado_future(f2).exception() is None
            else:
                assert to_asyncio_future(f2).exception() is None
            chain_future(f1, f2)
            f1.set_exception(Exception("foo"))
            assert f2.exception().args

# Generated at 2022-06-14 11:59:13.553236
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import concurrent.futures

    import tornado.ioloop
    from tornado.testing import gen_test

    executor = concurrent.futures.ThreadPoolExecutor(5)
    io_loop = tornado.ioloop.IOLoop.current()

    class AddOne(object):
        @tornado.gen.coroutine
        def add_one(self, x):
            return x + 1

        @tornado.gen.coroutine
        def add_one_executor(self, x):
            return (yield self._add_one(x))

        @run_on_executor
        def _add_one(self, x):
            return x + 1


# Generated at 2022-06-14 11:59:20.391666
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception)
    try:
        future.result()
    except Exception:
        pass
    else:
        assert False, "future_set_exception_unless_cancelled didn't work"
    # Cancel the future and make sure that the exception is discarded.
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception)
    assert future.cancelled()

# Generated at 2022-06-14 11:59:27.079268
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing

    f1 = Future()
    f2 = Future()

    def callback(f):
        assert f is f1
        assert f1.result() == 42
        f2.set_result(None)

    chain_future(f1, f2)
    f1.set_result(42)
    tornado.testing.gen_test(lambda: f2)()



# Generated at 2022-06-14 11:59:37.060498
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()

    # Reset the logger to ensure no messages are logged.
    app_log.handlers = []

    assert not future.cancelled()
    future_set_exception_unless_cancelled(future, Exception('bleh'))
    assert future.exception()
    assert not future.cancelled()

    future = Future()
    future.cancel()
    assert future.cancelled()
    future_set_exception_unless_cancelled(future, Exception('bleh'))
    assert not future.exception()
    assert future.cancelled()

# Generated at 2022-06-14 11:59:45.248525
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    future_set_exception_unless_cancelled(f, RuntimeError("foo"))
    assert f.exception() is not None, f.exception()
    # This function is called from the body of an except,
    # so we can't use unittest.TestCase.assertRaises
    old_value = f.exception()
    try:
        future_set_exception_unless_cancelled(f, RuntimeError("bar"))
    except Exception:
        pass
    else:
        raise Exception("expected cancel to suppress exception")
    assert f.exception() == old_value, f.exception()

# Generated at 2022-06-14 11:59:50.376056
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    # test if the exception is not raised when future is cancelled.
    future.cancel()
    try:
        future_set_exception_unless_cancelled(future, Exception("Hello"))
    except Exception:
        self.fail("Exception was raised even if the future was cancelled.")

# Generated at 2022-06-14 11:59:58.847097
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    future = Future()
    assert not future.done()

    exc = ValueError()
    future_set_exception_unless_cancelled(future, exc)
    assert future.done()
    assert isinstance(future.exception(), ValueError)

    future = Future()
    future.cancel()
    assert future.done()

    future_set_exception_unless_cancelled(future, exc)
    assert future.done()
    assert future.exception() is None

# Generated at 2022-06-14 12:00:11.593986
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    con = DummyExecutor()
    a = con.submit(lambda x: 2 * x, 2)  # a和b为Future类型的对象，代表计算结果的返回
    b = con.submit(lambda x: 2 * x, 3)  # 此处尝试测试DummyExecutor对submit的行为
    print(a.result())
    print(b.result())

# 此处尝试为了理解全部代码，所以自行输入调用函数，以便于测试