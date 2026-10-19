

# Generated at 2022-06-14 11:50:18.346994
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    ioloop = IOLoop.current()
    # Try using both types of futures
    for f in [Future(), futures.Future()]:
        f2 = Future()
        chain_future(f, f2)
        f2.done()
        f.set_result(42)
        ioloop.run_sync(lambda: f2)
        assert f2.result() == 42

# Generated at 2022-06-14 11:50:29.796732
# Unit test for function chain_future
def test_chain_future():  # type: ignore
    import logging
    import unittest

    # Set up custom log handler since we use logging in the tests
    logging.basicConfig(level=logging.DEBUG, datefmt="%H:%M:%S")
    logger = logging.getLogger()

    class CallableFuture(futures.Future):
        """A Future subclass that has a callback function."""

        def __init__(self, callback: Optional[Callable] = None) -> None:
            super(CallableFuture, self).__init__()
            self.callback = callback

        def add_done_callback(self, fn: Callable) -> None:
            if self.callback is not None:
                raise ValueError("Callback already defined.")
            self.callback = fn


# Generated at 2022-06-14 11:50:42.062928
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()
    f2 = Future()

    # Chain f1 -> f2
    chain_future(f1, f2)

    # Complete f1 successfully
    f1.set_result(42)
    assert f2.result() == 42

    # f1 -> f2, f1 is already done
    chain_future(f1, f2)
    assert f2.result() == 42

    # f1 -> f2, f2 is already done
    f2.set_result(None)
    chain_future(f1, f2)
    assert f2.result() == None

    # f1 -> f2, f1 completed with an exception
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

# Generated at 2022-06-14 11:50:50.940680
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    future = Future()

    # The exception should be able to be added to the future
    future_set_exception_unless_cancelled(future, ValueError())
    future_exc = future.exception()
    assert isinstance(future_exc, ValueError)

    # The exception should not be added to the future if it was cancelled
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError())
    future_exc = future.exception()
    assert future_exc is None

# Generated at 2022-06-14 11:50:57.856427
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    class Handler(object):
        executor = dummy_executor

        @run_on_executor
        def f(self):
            # type: () -> int
            return 42

        @run_on_executor()
        def f_empty(self):
            # type: () -> int
            return 42

        @run_on_executor
        def fail(self):
            # type: () -> int
            raise Exception()

        @run_on_executor
        def argument(self, x):
            # type: (int) -> int
            return x

        @run_on_executor(executor="_executor")
        def alternate_executor(self, x):
            # type: (int) -> int
            return x * 2


# Generated at 2022-06-14 11:51:00.972269
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    class TestException(Exception):
        pass

    f = Future()
    f.set_exception(TestException())
    future_set_exception_unless_cancelled(f, TestException())

# Generated at 2022-06-14 11:51:13.311362
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import logging
    import time

    def wait_and_set_result(f, result):
        time.sleep(1)
        f.set_result(result)

    def wait_and_set_exception(f, result):
        time.sleep(1)
        f.set_exception(result)

    class TestFuture(Future):
        def __init__(self):
            super(TestFuture, self).__init__()
            self._callbacks = []

        def add_done_callback(self, callback):
            self._callbacks.append(callback)

        def set_result(self, result):
            super(TestFuture, self).set_result(result)
            for callback in self._callbacks:
                callback(self)


# Generated at 2022-06-14 11:51:17.335174
# Unit test for function chain_future
def test_chain_future():
    def cb(f):
        l.append(f.result())
    l = []
    f = Future()
    g = Future()
    chain_future(f, g)
    f.add_done_callback(cb)
    g.add_done_callback(cb)
    f.set_result(42)
    assert l == [42, 42]



# Generated at 2022-06-14 11:51:25.851657
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    future = Future()
    future_set_exception_unless_cancelled(future, Exception("test"))
    assert not future.cancelled()
    assert isinstance(future.result(), Exception)
    assert future.result().__str__() == "test"

    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception("test"))
    assert future.cancelled()

# Generated at 2022-06-14 11:51:31.842154
# Unit test for function chain_future
def test_chain_future():
    f = asyncio.Future()
    g = futures.Future()

    # Verify correct operation when g is not ready.
    chain_future(f, g)
    f.set_result(None)
    assert g.result() is None

    # Verify correct operation when g is already done.
    f = asyncio.Future()
    g.set_result(None)
    chain_future(f, g)
    f.set_result(None)
    assert g.result() is None

    # Verify correct operation when f is already done.
    f = futures.Future()
    f.set_result(None)
    g = asyncio.Future()
    chain_future(f, g)
    assert g.result() is None
    f.set_result(None)
    assert g.result() is None

    # Verify correct

# Generated at 2022-06-14 11:51:37.091956
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    result = dummy_executor.submit(lambda: 1)
    assert isinstance(result, futures.Future)
    assert result.result() == 1

# Generated at 2022-06-14 11:51:45.927047
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    assert not future.done()
    future_set_exception_unless_cancelled(future, ZeroDivisionError())
    assert future.done()
    assert not future.cancelled()
    assert isinstance(future.exception(), ZeroDivisionError)

    future = Future()
    future.cancel()
    assert future.done()
    assert future.cancelled()
    future_set_exception_unless_cancelled(future, ZeroDivisionError())
    assert future.done()
    assert future.cancelled()
    assert future.exception() is None

# Generated at 2022-06-14 11:51:50.554752
# Unit test for function run_on_executor
def test_run_on_executor():
    class MyObject:
        def __init__(self):
            self.io_loop = None
            self.executor = dummy_executor

        @run_on_executor
        def foo(self):
            return "bar"

    obj = MyObject()
    future = obj.foo()
    assert is_future(future)  # type: ignore
    assert future.result() == "bar"



# Generated at 2022-06-14 11:51:57.771559
# Unit test for function chain_future
def test_chain_future():
    a_future = Future()
    b_future = Future()
    chain_future(a_future, b_future)

    a_future.set_result('test_chain_future')
    assert b_future.result() == 'test_chain_future'

    # Check that cancelling b_future doesn't prevent a_future from
    # completing it.
    b_future = Future()
    b_future.cancel()
    assert b_future.cancelled()
    chain_future(a_future, b_future)
    assert b_future.result() == 'test_chain_future'

# Generated at 2022-06-14 11:52:05.447158
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class TestChaining(AsyncTestCase):
        @gen_test
        def test(self):
            from tornado.concurrent import Future

            a = Future()
            b = Future()

            self.assertFalse(a.done())
            self.assertFalse(b.done())

            chain_future(a, b)
            self.assertFalse(b.done())

            a.set_result(42)
            self.assertTrue(a.done())
            self.assertTrue(b.done())
            self.assertEqual(b.result(), 42)

    test = TestChaining()
    test.test()

# Generated at 2022-06-14 11:52:14.220245
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_result(None)
    assert future2.done()
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_exception(RuntimeError())
    assert future2.done()
    assert future2.exception() is not None
    assert isinstance(future2.exception(), RuntimeError)



# Generated at 2022-06-14 11:52:17.705094
# Unit test for function chain_future
def test_chain_future():
    f = Future()  # type: Future[int]
    f2 = Future()
    chain_future(f, f2)
    f.set_result(42)
    assert f2.result() == 42



# Generated at 2022-06-14 11:52:19.292379
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def f1():
        # type: () -> None
        pass



# Generated at 2022-06-14 11:52:28.082015
# Unit test for function chain_future
def test_chain_future():
    loop = tornado.ioloop.IOLoop()
    loop.make_current()
    async_fut = Future()
    fut = futures.Future()
    chain_future(fut, async_fut)
    callback = _MockCallback()
    async_fut.add_done_callback(callback)
    fut.set_result(None)
    loop.add_future(fut, lambda f: None)
    assert callback.result is True
    loop.close()



# Generated at 2022-06-14 11:52:37.931083
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    async_future = Future()
    done = [False]

    def done_callback(fut):
        assert f is async_future
        done[0] = True

    IOLoop.current().add_future(async_future, done_callback)

    f = futures.Future()
    chain_future(f, async_future)
    assert not f.done()
    assert not async_future.done()
    f.set_result(42)
    assert f.done()
    assert async_future.done()
    assert async_future.result() == 42
    IOLoop.current().start()
    # IOLoop.add_future calls the callback immediately if the future is done
    assert done[0]

# Generated at 2022-06-14 11:52:53.652649
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    class O(object):
        def __init__(self, executor):
            # type: (concurrent.futures.Executor) -> None
            self.executor = executor

        @run_on_executor
        def func(self, a, b, key=None):
            # type: (int, int, Optional[str]) -> int
            return a + b

        @run_on_executor(executor="executor2")
        def func2(self, a, b):
            # type: (int, int) -> int
            return a - b

    executor = futures.ThreadPoolExecutor(1)
    executor2 = futures.ThreadPoolExecutor(1)
    o = O(executor)
    o.executor2 = executor2


# Generated at 2022-06-14 11:53:03.562193
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(42)
    assert f2.done()
    assert 42 == f2.result()
    f3 = Future()
    f4 = Future()
    chain_future(f3, f4)
    assert not f4.done()
    f3.set_exception(ValueError())
    assert f4.done()
    try:
        f4.result()
    except ValueError as e:
        caught = e

    assert caught

# Generated at 2022-06-14 11:53:15.476480
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    assert isinstance(Future(), Future)
    assert isinstance(futures.Future(), futures.Future)
    f1, f2 = Future(), Future()
    chain_future(f1, f2)
    assert not f1.done()
    assert not f2.done()
    chain_future(f2, f1)
    f1.set_result(1)
    assert f1.result() == 1
    assert f2.result() == 1
    assert f1.done()
    assert f2.done()
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f2.cancel()
    f1.set_result(1)
    assert f1.result() == 1
    assert f1.done()
   

# Generated at 2022-06-14 11:53:25.159554
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing
    import tornado.ioloop
    import unittest

    @tornado.testing.gen_test
    def test_gen_chain_future():
        a = Future()
        b = Future()
        chain_future(a, b)
        a.set_result(None)
        yield b

    def test_chain_future_callback():
        a = Future()
        b = Future()
        chain_future(a, b)
        a.set_result(None)

        @tornado.testing.gen_test
        def _test():
            yield b

        return _test()

    @tornado.testing.gen_test
    def test_chain_future_py34_await():
        a = Future()
        b = Future()
        chain_future(a, b)
        a.set

# Generated at 2022-06-14 11:53:37.578584
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest.mock

    # The test uses patch to replace the future.result() call with
    # a callable
    future_result = unittest.mock.Mock()
    with unittest.mock.patch('tornado.concurrent.future.result', future_result):
        class Foo(object):
            # executor must be a class attribute to survive patch
            executor = dummy_executor

            @run_on_executor
            def func(self, arg1, arg2, kwarg1=None):
                return arg1, arg2, kwarg1

            @run_on_executor
            def func_exception(self):
                raise Exception('error')


# Generated at 2022-06-14 11:53:43.547756
# Unit test for function chain_future
def test_chain_future():
    def function_a(result: Any, argument: Any) -> None:
        pass

    def function_b(result: Any, argument: Any) -> None:
        pass

    class DummyFuture(object):
        def __init__(self) -> None:
            self.done_callbacks = []  # type: List[Callable]
            self.added_callback = None  # type: Optional[Callable]

        def add_done_callback(self, callback: Callable) -> None:
            self.done_callbacks.append(callback)
            self.added_callback = callback

        def set_result(self, result: Any) -> None:
            self.result = result

        def result(self) -> Any:
            return self.result

        def set_exception(self, exception: Any) -> None:
            self

# Generated at 2022-06-14 11:53:55.346945
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    f1.set_result(42)
    chain_future(f1, f2)
    assert f2.result() == 42
    f1 = Future()
    f1.set_exception(ValueError("foo"))
    chain_future(f1, f2)
    assert f2.exception() == ValueError("foo")
    f1 = Future()
    f1.cancel()
    chain_future(f1, f2)
    assert f2.cancelled()
    f1 = futures.Future()
    f1.set_result(42)
    chain_future(f1, f2)
    assert f2.result() == 42
    f1 = futures.Future()
    f1.set_exception(ValueError("foo"))


# Generated at 2022-06-14 11:54:08.300978
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test

    @gen_test
    def check(a_tuple, b_tuple):
        a = Future()
        b = Future()
        chain_future(a, b)
        a_result, a_exc = a_tuple
        b_result, b_exc = b_tuple
        if a_exc:
            future_set_exc_info(a, a_exc)
        else:
            a.set_result(a_result)
        if not b_exc and b.done():
            assert b.result() == b_result
        try:
            b_result = yield b
            assert not b_exc
            assert b_result == b_result
        except Exception:
            assert b_exc
            exc_info = sys.exc_info()
            assert exc_

# Generated at 2022-06-14 11:54:15.339512
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    chain_future_called = [False]

    def mark_called(arg):
        # type: (Any) -> None
        chain_future_called[0] = True

    future2 = Future()
    chain_future(future2, future1)
    future2.set_result(42)
    assert chain_future_called == [False]
    future1.add_done_callback(mark_called)
    assert chain_future_called == [True]
    assert future1.result() == 42
    assert future1 is not future2

    future2 = Future()
    chain_future(future1, future2)
    assert future2.result() == 42
    assert future1 is not future2

    future1 = Future()
    future2 = Future()

# Generated at 2022-06-14 11:54:21.785148
# Unit test for function chain_future
def test_chain_future():
    def callback(fut: Future) -> None:
        callback.called = True

    async_future = Future()
    callback.called = False
    chain_future(async_future, Future())
    async_future.set_result(42)
    assert callback.called

    callback.called = False
    chain_future(async_future, Future())
    assert callback.called



# Generated at 2022-06-14 11:54:37.655045
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 'Future result')
    assert future.result() == 'Future result'
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 'Future result')
    assert future.cancelled()

# Generated at 2022-06-14 11:54:47.871594
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import unittest
    import logging
    import sys

    class FutureException(Exception):
        pass

    class FutureSetExceptionUnlessCancelTestCase(unittest.TestCase):
        def setUp(self):
            self.log = logging.Logger(self.__class__.__name__)
            handler = logging.StreamHandler(sys.stderr)
            self.log.addHandler(handler)


        def test_future_exception_not_set(self):
            future = Future()
            exc = FutureException()
            future_set_exception_unless_cancelled(future, exc)
            self.assertEqual(exc, future.exception())


        def test_future_exception_set(self):
            future = Future()
            future.set_exception(FutureException())

# Generated at 2022-06-14 11:54:59.243667
# Unit test for function chain_future
def test_chain_future():
    def cb(f):
        assert f.result() == 10
        called[0] = True

    f1 = Future()
    called = [False]
    chain_future(f1, Future())
    chain_future(f1, Future())
    chain_future(f1, Future())
    f1.result()

    f2 = Future()
    chain_future(f2, Future())
    f2.set_result(10)
    f2.add_done_callback(cb)
    f2.result()
    assert called[0]

    f3 = Future()
    chain_future(f3, Future())
    f3.set_result(10)
    f3.result()

    f4 = Future()
    chain_future(f4, Future())
    assert not f4.done()
   

# Generated at 2022-06-14 11:55:09.240793
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    future_set_result_unless_cancelled(f, 10)
    assert f.result() == 10
    f = Future()
    f.cancel()
    try:
        future_set_result_unless_cancelled(f, 10)
    except asyncio.CancelledError:
        pass
    else:
        raise Exception('Expected to raise asyncio.CancelledError')
    assert not f.cancelled()
    assert f.exception() == None
    assert f.result() == None

# Generated at 2022-06-14 11:55:13.887431
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.ioloop import IOLoop
    import tornado.testing

    f1 = Future()  # type: Future
    f2 = Future()  # type: Future
    chain_future(f1, f2)
    IOLoop.current().add_callback(f1.set_result, None)
    tornado.testing.gen_test(f2)

# Generated at 2022-06-14 11:55:21.939724
# Unit test for function chain_future
def test_chain_future():
    import unittest.mock

    a = Future()
    b = Future()

    with unittest.mock.patch.object(b, "set_result") as m_set_result:
        chain_future(a, b)
        assert not m_set_result.called
        a.set_result(42)
        assert m_set_result.called

    a = Future()
    b = Future()

    with unittest.mock.patch.object(b, "set_exception") as m_set_exception:
        chain_future(a, b)
        assert not m_set_exception.called
        a.set_exception(ValueError)
        assert m_set_exception.called

    a = Future()

# Generated at 2022-06-14 11:55:34.662226
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.platform.asyncio import to_asyncio_future

    # Note that this test uses both futures from tornado.concurrent and
    # asyncio. This is intended to show that chain_future can support
    # both interchangeably, although it is preferable to not mix them
    # in real code.
    class ChainFutureTest(AsyncTestCase):
        def test_future_success(self):
            a = Future()
            b = Future()
            chain_future(a, b)
            a.set_result(42)
            self.assertEqual(b.result(), 42)

        def test_future_exception(self):
            a = Future()
            b = Future()
            chain_future(a, b)

# Generated at 2022-06-14 11:55:47.384456
# Unit test for function chain_future
def test_chain_future():  # type: ignore
    def future_done(future):  # type: ignore
        raise Exception("should not get here")

    future1 = Future()  # type: Future
    future2 = Future()  # type: Future
    chain_future(future1, future2)
    future1.set_result(42)
    future2.set_result(24)
    future_add_done_callback(future1, future_done)
    future_add_done_callback(future2, future_done)

    future1 = Future()  # type: Future
    future2 = Future()  # type: Future
    chain_future(future1, future2)
    future1.set_exception(RuntimeError())
    try:
        future2.result()
    except RuntimeError:
        pass

# Generated at 2022-06-14 11:56:00.683414
# Unit test for function chain_future
def test_chain_future():

    async def async_main():
        f1 = Future()
        f2 = Future()

        chain_future(f1, f2)

        f1.set_result(None)
        assert f2.done()

        f3 = Future()
        f4 = Future()

        chain_future(f3, f4)

        f3.set_exception(ValueError())
        assert f4.done()

        try:
            f4.result()
        except ValueError:
            pass
        else:
            raise Exception("should have raised ValueError")

    import tornado.testing

    def _threaded_chain_future():
        try:
            tornado.testing.run_sync(async_main)
        except Exception:
            import traceback

            traceback.print_exc()

    from concurrent.futures import Thread

# Generated at 2022-06-14 11:56:11.057471
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing
    import tornado.gen

    class AsyncFuture(Future):
        def __init__(self, io_loop=None):
            super(AsyncFuture, self).__init__()
            self.io_loop = io_loop or tornado.ioloop.IOLoop.current()

        def set_result(self, result):
            self.io_loop.add_callback(super(AsyncFuture, self).set_result, result)

        def set_exception(self, exception):
            self.io_loop.add_callback(super(AsyncFuture, self).set_exception, exception)

    class SyncFuture(futures.Future):
        def set_result(self, result):
            super(SyncFuture, self).set_result(result)


# Generated at 2022-06-14 11:56:39.144401
# Unit test for function chain_future
def test_chain_future():
    # Success case
    f1 = Future()  # type: Future[int]
    f2 = Future()  # type: Future[int]
    chain_future(f1, f2)
    f1.set_result(42)
    f2.result()

    # Exception case
    f3 = Future()  # type: Future[int]
    f4 = Future()  # type: Future[int]
    chain_future(f3, f4)
    f3.set_exception(ValueError())
    with pytest.raises(ValueError):
        f4.result()

# Generated at 2022-06-14 11:56:55.584832
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    class A(object):
        def __init__(self, *args, **kwargs):
            assert len(args) == 0
            assert len(kwargs) == 0
            self.executor = dummy_executor

        def foo(self, *args, **kwargs):
            assert args == ("a", 2)
            assert kwargs == {"b": 3}
            return "bar"

        foo = run_on_executor()(foo)

    a = A()
    f = a.foo("a", b=3, c=5)
    assert isinstance(f, Future)
    assert f.result() == "bar"

    # args/kwargs are put at the end, too:
    a.foo("a", b=3, c=5)


# Generated at 2022-06-14 11:57:03.077274
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    from tornado.escape import native_str
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado import gen

    class TestCase(AsyncTestCase):
        @staticmethod
        def setUpModule():
            super(TestCase, TestCase).setUpModule()
            AsyncIOMainLoop().install()

        def test_set_result_unless_cancelled(self):
            future = Future()
            future_set_result_unless_cancelled(future, 42)
            self.assertEqual(future.result(), 42)
            future_set_result_unless_cancelled(future, 43)
            self.assertEqual(future.result(), 42)


# Generated at 2022-06-14 11:57:11.025567
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    assert b.result() == 42

    a = Future()
    b = Future()
    a.set_exception(ZeroDivisionError)
    with pytest.raises(ZeroDivisionError):
        chain_future(a, b)
        b.result()

    a = concurrent.futures.Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    assert b.result() == 42

    a = concurrent.futures.Future()
    b = Future()
    a.set_exception(ZeroDivisionError)

# Generated at 2022-06-14 11:57:15.127814
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    class X(object):
        executor = futures.ThreadPoolExecutor(1)

    x = X()

    @run_on_executor
    def my_method(self, x, y):
        # type: (X, int, int) -> int
        assert self is x
        return x.foo + y

    x.foo = 5

    fut = my_method(x, 6)
    assert fut.result() == 11



# Generated at 2022-06-14 11:57:21.791902
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from tornado.log import app_log
    from tornado.ioloop import IOLoop
    from tornado.httpserver import HTTPServer
    from tornado.concurrent import run_on_executor
    import asyncio
    import logging
    import time
    import sys
    import threading
    import concurrent.futures
    import logging
    import traceback
    import time

    app_log.setLevel(logging.DEBUG)
    server = HTTPServer(RequestHandler)
    server.listen(8000, address='127.0.0.1')
    app_log.info("{} started at {}:{}".format(sys.argv[0], "127.0.0.1", 8000))
    # get the loop
    ioloop = IOLoop.current()
    # add a task to process requests

# Generated at 2022-06-14 11:57:35.697810
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    ioloop = IOLoop.current()

    def test(source, dest):
        def assert_chain(future, exc):
            assert source.result() is future.result()
            if exc is not None:
                assert future.exception()[1] is source.exception()[1]

        source.add_done_callback(assert_chain)
        chain_future(source, dest)

    f1 = Future()
    f2 = futures.Future()
    f3 = Future()
    f4 = futures.Future()
    f5 = Future()
    f6 = futures.Future()

    f1.set_result(True)
    f2.set_result(True)
    f3.set_exception(ZeroDivisionError())
    f4.set_ex

# Generated at 2022-06-14 11:57:41.367480
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(3)
    assert f2.done()
    assert f2.result() == 3

# Generated at 2022-06-14 11:57:53.427154
# Unit test for function chain_future
def test_chain_future():
    io_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(io_loop)

    # Test a -> b
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(1)
    assert b.result() == 1

    # Test a -> b where b is already finished
    a = Future()
    b = Future()
    b.set_result(2)
    chain_future(a, b)
    a.set_result(3)
    assert b.result() == 2

    # b should get the exception from a
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_exception(KeyError())
    assert len(b.exception().args) == 1



# Generated at 2022-06-14 11:57:57.823473
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()  # type: Future[int]
    future_set_exception_unless_cancelled(f, ValueError())
    assert f.exception()

    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, ValueError())

# Generated at 2022-06-14 11:58:27.591639
# Unit test for function run_on_executor
def test_run_on_executor():

    class Example(object):
        executor = FuturesExecutor(max_workers=5)

        @run_on_executor
        def test(self, arg_1, arg_2, kwarg_1="kwarg_1", kwarg_2="kwarg_2"):
            assert arg_1 == "arg_1"
            assert arg_2 == "arg_2"
            assert kwarg_1 == "kwarg_1"
            assert kwarg_2 == "kwarg_2"
            return arg_1, arg_2, kwarg_1, kwarg_2

    ex = Example()
    future = ex.test("arg_1", "arg_2", "kwarg_1", "kwarg_2")


# Generated at 2022-06-14 11:58:38.197884
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    from concurrent import futures
    from tornado.platform.asyncio import AsyncIOMainLoop

    class RunOnExecutor(unittest.TestCase):
        def setUp(self):
            self.loop = AsyncIOMainLoop()
            self.loop.make_current()
            self.io_loop = self.loop._wrapper
            self.executor = futures.ThreadPoolExecutor(1)

        def tearDown(self):
            self.executor.shutdown()
            self.loop.close(all_fds=True)

        @run_on_executor
        def func(self):
            return 42

        @run_on_executor(executor="executor")
        def func2(self):
            return 42


# Generated at 2022-06-14 11:58:51.785548
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    assert future.done()
    assert future.result() == 1

    future = Future()
    future_set_result_unless_cancelled(future, None)
    assert future.done()
    assert future.result() is None

    future = Future()
    future_set_result_unless_cancelled(future, True)
    assert future.done()
    assert future.result() == True

    future = Future()
    future_set_result_unless_cancelled(future, "hello")
    assert future.done()
    assert future.result() == "hello"

    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 1)
    assert future.done

# Generated at 2022-06-14 11:58:58.819810
# Unit test for function chain_future
def test_chain_future():
    from unittest.mock import Mock

    arg1 = object()
    arg2 = object()
    kwarg1 = object()
    kwarg2 = object()

    a = Future()
    b = Future()

    fn = Mock()
    chain_future(a, b)

    fn.return_value = arg1
    future_set_result_unless_cancelled(a, arg1)
    assert fn.mock_calls == []
    assert b.result() is arg1

    fn.return_value = arg2
    a = Future()
    b = Future()
    chain_future(a, b)
    future_set_result_unless_cancelled(b, arg2)
    assert fn.mock_calls == []

# Generated at 2022-06-14 11:59:12.331020
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class TestChainFuture(AsyncTestCase):
        def setUp(self) -> None:
            super().setUp()
            self.executor = futures.ThreadPoolExecutor(1)

        @run_on_executor
        def divide(self, dividend: float, divisor: float) -> float:
            return dividend / divisor

        @gen_test
        async def test_chain_future(self) -> None:
            a = self.divide(1, 2)
            b = self.divide(1, 0)
            c = self.divide(4, 2)
            chain_future(b, c)
            with self.assertRaises(ZeroDivisionError):
                await c
            self.assertEqual(0.5, await a)

# Generated at 2022-06-14 11:59:23.126885
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado import gen
    from tornado import testing
    from tornado import httpserver
    from tornado.web import RequestHandler, Application

    test_future = Future()

    class MainHandler(RequestHandler):
        executor = dummy_executor

        @run_on_executor
        def get(self):
            yield test_future
            self.write("OK")

    @gen.coroutine
    def f():
        assert not test_future.done()
        response = yield AsyncHTTPClient().fetch(
            http_server.get_url("/"), raise_error=False
        )
        assert response.code == 200
        test_future.set_result(None)

    AsyncIOMainLoop().install()

# Generated at 2022-06-14 11:59:30.910274
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    def test_set(future, value):
        future_set_result_unless_cancelled(future, value)

    future = Future()
    future.set_result(999)
    future_set_result_unless_cancelled(future, 0)
    assert future.result() == 999
    
    future = Future()
    future.set_exception(ValueError)
    future_set_result_unless_cancelled(future, 0)
    assert isinstance(future.exception(), ValueError)
    
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 0)
    assert future.cancelled()

# Generated at 2022-06-14 11:59:43.041313
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.testing import AsyncTestCase, gen_test

    class Dummy(object):

        @run_on_executor
        def dummy_method(self) -> int:
            return 42

    @gen_test
    def test_function(io_loop):
        # type: (IOLoop) -> None
        dummy_instance = Dummy()
        dummy_instance.executor = dummy_executor
        future_1 = Future()
        future_2 = dummy_instance.dummy_method()
        chain_future(future_1, future_2)
        future_1.set_result("foo")
        self.assertEqual(io_loop.run_sync(future_2.result), 42)

    AsyncTestCase().run_test(test_function)

# Generated at 2022-06-14 11:59:45.002921
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    future = dummy_executor.submit(lambda : 'test')
    print(future.result())

if __name__ == '__main__':
    test_DummyExecutor_submit()

# Generated at 2022-06-14 11:59:57.409009
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    g = Future()

    chain_future(f, g)
    assert f.done() and g.done()

    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_result(None)
    assert g.done()

    f = Future()
    g = Future()
    chain_future(f, g)
    g.set_result(None)
    assert g.done()

    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_exception(ValueError)
    assert g.done()
    assert isinstance(g.exception(), ValueError)

    # This test is slightly nonsensical: Future doesn't support
    # cancelling.
    f = Future()
    g = Future()
   