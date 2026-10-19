

# Generated at 2022-06-14 11:50:44.889142
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    result1 = dummy_executor.submit(lambda: 4)
    result2 = dummy_executor.submit(lambda x: x * 2, 2)
    result3 = dummy_executor.submit(lambda x, y: x + y, 2, 3)
    result4 = dummy_executor.submit(lambda x, y, z: x + y + z, 2, 3, 5)

    assert result1.result() == 4
    assert result2.result() == 4
    assert result3.result() == 5
    assert result4.result() == 10

# Generated at 2022-06-14 11:50:59.265093
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import time

    from tornado.testing import AsyncTestCase, gen_test

    class MyTestCase(AsyncTestCase):
        def setUp(self):
            super(MyTestCase, self).setUp()
            if hasattr(self, "executor"):
                # Use an executor that is not the global thread pool; a
                # real program using this interface would likely have one
                # executor per object (or per object type).
                self.executor = futures.ThreadPoolExecutor(1)
            else:
                self.executor = None

        def tearDown(self):
            if self.executor:
                self.executor.shutdown()
            super(MyTestCase, self).tearDown()


# Generated at 2022-06-14 11:51:06.742759
# Unit test for function chain_future
def test_chain_future():
    import unittest

    from tornado.testing import AsyncTestCase, gen_test

    # Set up a Future that will be passed to chain_future
    def func():
        f = Future()
        f.set_result(42)
        return f

    @gen_test
    def test_chain_future(self):
        # This simply tests that chain_future does not raise an exception.
        # The Future that chain_future is called with has already been set
        # to finished, so the Future that is passed to chain_future
        # should already be set to finished when the callback is called.
        f = Future()
        chain_future(func(), f)
        self.assertEqual(f.result(), 42)

    unittest.main()

# Generated at 2022-06-14 11:51:16.837203
# Unit test for function chain_future
def test_chain_future():
    _inner = None
    _outer = None

    def inner_done(future):
        nonlocal _inner
        _inner = future

    def outer_done(future):
        nonlocal _outer
        _outer = future

    def blow_up():
        raise Exception("should not be called")

    inner = Future()
    outer = Future()

    chain_future(inner, outer)
    inner.set_result(42)
    assert inner.result() == outer.result() == 42
    assert inner.done() is outer.done() is True
    assert inner is _inner is _outer is outer

    _inner = _outer = None
    inner = Future()
    outer = Future()
    chain_future(inner, outer)
    # Test that setting the inner future's exception also sets the outer's.

# Generated at 2022-06-14 11:51:27.274186
# Unit test for function chain_future
def test_chain_future():
    from concurrent import futures

    loop = asyncio.get_event_loop()
    executor = futures.ThreadPoolExecutor(1)

    def thread_func(future):
        time.sleep(1)
        future.set_result(42)
        return 42

    def loop_func(future):
        a = future
        b = asyncio.Future()
        chain_future(a, b)
        return b

    a = executor.submit(thread_func, futures.Future())
    b = loop.run_until_complete(loop_func(a))
    assert b.result() == 42

# Generated at 2022-06-14 11:51:31.387182
# Unit test for function chain_future
def test_chain_future():
    @run_on_executor()
    def func():
        return "abc"

    def callback(f):
        callback.result = f.result()

    callback.result = _NO_RESULT
    f = Future()
    chain_future(func(), f)
    assert f.result() == "abc"

    chain_future(func(), f)
    assert f.result() == "abc"

    chain_future(func(), f)
    future_add_done_callback(f, callback)
    assert callback.result == "abc"

# Generated at 2022-06-14 11:51:37.600982
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    def f():
        try:
            raise Exception('exception')
        except:
            exc_info = sys.exc_info()
            future_set_exc_info(future, exc_info)


    future = Future()
    f()
    future.result()

    future = Future()
    future.set_result('foo')
    f()
    assert future.result() == 'foo'

    future = Future()
    future.cancel()
    f()
    assert future.cancelled(), future.cancelled()


if __name__ == "__main__":
    import unittest
    unittest.main()

# Generated at 2022-06-14 11:51:42.841287
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.ioloop import IOLoop

    io_loop = IOLoop()
    orig = Future()
    f = Future()
    chain_future(orig, f)
    io_loop.add_future(orig, lambda future: future.set_result(1))
    io_loop.add_future(f, lambda future: io_loop.stop())
    io_loop.start()
    assert f.result() == 1
    orig = Future()
    f = Future()
    chain_future(orig, f)
    io_loop.add_callback(orig.set_exception, ZeroDivisionError())
    io_loop.add_future(f, lambda future: io_loop.stop())
    io_loop.start()
    assert f.exception().__class__ == ZeroDivision

# Generated at 2022-06-14 11:51:43.951247
# Unit test for function chain_future
def test_chain_future():
    pass  # todo



# Generated at 2022-06-14 11:51:51.321327
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    from tornado.concurrent import Future
    from tornado.test.util import unittest

    class FutureTestCase(unittest.TestCase):
        def test_future_set_result_unless_cancelled(self):
            f = Future()
            future_set_result_unless_cancelled(f, 10)
            self.assertEqual(f.result(), 10)
            f = Future()
            f.cancel()
            future_set_result_unless_cancelled(f, 20)
            self.assertEqual(f.result(), 20)

    test_future_set_result_unless_cancelled()

# Generated at 2022-06-14 11:52:20.872965
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    async def f():
        future = Future()
        assert not future.done()
        future_set_result_unless_cancelled(future, None)
        assert future.done()
        future.cancel()
        # Setting the result on a cancelled future should raise
        # an exception
        try:
            future.set_result(None)
        except asyncio.InvalidStateError:
            pass
        else:
            assert False, "Setting result on cancelled future should raise an exception"
        future_set_result_unless_cancelled(future, None)
        assert future.done()

    asyncio.get_event_loop().run_until_complete(f())

# Generated at 2022-06-14 11:52:32.609882
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from . import ioloop
    from . import gen
    from . import coroutines

    ioloop.IOLoop.clear_instance()
    loop = ioloop.IOLoop.current()

    @gen.coroutine
    def test_method():
        yield dummy_executor.submit(id, 42)
        yield dummy_executor.submit(lambda: (yield 42))

    def test_method2():
        yield dummy_executor.submit(id, 42)
        yield dummy_executor.submit(lambda: (yield 42))

    loop.run_sync(test_method)

    # Python 3.5:
    loop.run_sync(coroutines.as_coroutine(test_method2))


# Generated at 2022-06-14 11:52:36.544111
# Unit test for function chain_future
def test_chain_future():
    # Using Future, not tornado.concurrent.Future
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result("1")
    assert f2.result() == "1"



# Generated at 2022-06-14 11:52:48.933187
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()
    a.set_result(42)
    assert b.done()
    assert b.result() == 42
    b = Future()
    chain_future(a, b)
    assert b.done()
    assert b.result() == 42
    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()
    a.set_exception(ZeroDivisionError)
    assert b.done()
    try:
        b.result()
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("did not propagate exception")

# Generated at 2022-06-14 11:52:56.322776
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def test_foo(a, b):
        return a+b

    dummy_executor = DummyExecutor()
    future = dummy_executor.submit(test_foo, 1, 2)
    assert future.done()
    assert future.result() == 3

    future = dummy_executor.submit(test_foo, 1, b=2)
    assert future.done()
    assert future.result() == 3

    def test_bar():
        raise Exception()
    future = dummy_executor.submit(test_bar)
    assert future.done()
    try:
        future.result()
    except Exception:
        pass
    else:
        assert False, "This should fail to get here"


# Generated at 2022-06-14 11:52:59.013513
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.cancel()

    future_set_exception_unless_cancelled(future, ValueError())

# Generated at 2022-06-14 11:53:09.074292
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class FutureTestCase(AsyncTestCase):
        def setUp(self):
            super(FutureTestCase, self).setUp()
            self.executor = futures.ThreadPoolExecutor(1)

        def tearDown(self):
            self.executor.shutdown()
            super(FutureTestCase, self).tearDown()

        @gen_test
        def test_chain(self):
            future1 = Future()
            future2 = Future()
            chain_future(future1, future2)
            future1.set_result(42)
            self.assertEqual(future2.result(), 42)

        @gen_test
        def test_chain_concurrent_futures(self):
            future1 = self.executor.submit(lambda: 42)

# Generated at 2022-06-14 11:53:09.679295
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    pass

# Generated at 2022-06-14 11:53:13.290472
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(None)
    assert f2.done()

# Generated at 2022-06-14 11:53:22.322082
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42
    f1 = Future()
    f2 = Future()
    f1.set_result(42)
    chain_future(f1, f2)
    assert f2.result() == 42
    f1 = Future()
    f2 = Future()
    f2.set_result(42)
    chain_future(f1, f2)
    f1.set_result(24)
    assert f2.result() == 42

# Generated at 2022-06-14 11:53:51.207775
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import tornado.testing

    # Use a real IOLoop.
    class MyTestCase(tornado.testing.AsyncTestCase):
        def test_chain(self):
            # type: () -> None
            a = Future()
            b = Future()
            chain_future(a, b)
            c = Future()
            chain_future(b, c)

            # Finish a, check b
            a.set_result(42)
            self.assertEqual(a.result(), 42)
            self.assertTrue(b.done())
            self.assertEqual(b.result(), 42)

            # Finish b, check c
            b.set_result(24)
            self.assertEqual(b.result(), 24)
            self.assertTrue(c.done())
            self.assertEqual

# Generated at 2022-06-14 11:54:01.239339
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import unittest
    import asyncio

    async def async_test():
        # type: () -> None
        loop = asyncio.get_event_loop()
        a = loop.create_future()
        b = loop.create_future()
        chain_future(a, b)
        loop.call_soon(a.set_result, 42)
        assert await b == 42
        a = loop.create_future()
        b = loop.create_future()
        chain_future(a, b)
        loop.call_soon(a.set_exception, ValueError())
        try:
            await b
        except ValueError:
            pass
        else:
            raise unittest.case.SkipTest("set_exception did not propagate")

    loop = asyncio.get_event

# Generated at 2022-06-14 11:54:12.239231
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from concurrent.futures import ThreadPoolExecutor
    from tornado.platform.asyncio import to_asyncio_future

    executor = ThreadPoolExecutor(1)

    class Foo(object):
        executor = executor

        @run_on_executor
        def func(self, arg):
            return arg + 1

    foo = Foo()

    @gen.coroutine
    def f():
        assert (yield foo.func(1)) == 2

    IOLoop.current().run_sync(f)
    # Also test compatibility with concurrent.futures.Future
    asyncio_future = to_asyncio_future(executor.submit(lambda: 1))
    assert asyncio_future.result() == 1

# Generated at 2022-06-14 11:54:25.276725
# Unit test for method submit of class DummyExecutor

# Generated at 2022-06-14 11:54:37.798254
# Unit test for function chain_future
def test_chain_future():
    """
    test :func:`chain_future`
    """
    import asyncio
    from tornado.testing import AsyncTestCase, gen_test

    def foo():pass
    async def bar():pass
    class UnitTest(AsyncTestCase):
        @gen_test(timeout=1)
        def test_func(self):
            """
            test :func:`chain_future`
            """
            f1 = Future()
            f2 = Future()
            f3 = Future()
            f4 = Future()
            f5 = Future()
            f6 = Future()
            f7 = Future()
            f8 = Future()
            chain_future(f1,f2);chain_future(f1,f3);chain_future(f1,f4)
            chain_future(f2,f5);chain_future

# Generated at 2022-06-14 11:54:48.288732
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase
    from tornado.ioloop import IOLoop

    io_loop = IOLoop()
    io_loop.make_current()

    class TestCase(AsyncTestCase):
        def test_chain_future(self):
            a = Future()
            b = Future()

            chain_future(a, b)
            chain_future(b, a)

            def f():
                self.assertFalse(a.done())
                self.assertFalse(b.done())

                a.set_result(42)
                self.assertEqual(a.result(), 42)
                self.assertEqual(b.result(), 42)

                b.set_exception(ValueError)
                self.assertTrue(isinstance(a.exception(), ValueError))

# Generated at 2022-06-14 11:54:51.043491
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = asyncio.Future()
    exc = RuntimeError()
    future_set_exception_unless_cancelled(future, exc)
    assert future.exception() is exc

    future = asyncio.Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, exc)
    assert future.exception() is None

# Generated at 2022-06-14 11:55:00.875152
# Unit test for function chain_future
def test_chain_future():

    def f():
        return 3

    def fail():
        raise Exception("oh noes")

    a = Future()
    b = Future()
    c = Future()
    chain_future(a, b)
    chain_future(a, c)
    a.set_result(None)
    assert b.result() is None
    assert c.result() is None
    a = Future()
    b = Future()
    c = Future()
    chain_future(a, b)
    chain_future(a, c)
    a.set_exception(RuntimeError())
    assert not b.result() is None
    assert b.exception() is not None
    assert not c.result() is None
    assert c.exception() is not None
    a = Future()
    b = Future()
    c = Future()


# Generated at 2022-06-14 11:55:14.133337
# Unit test for function chain_future
def test_chain_future():
    def run_test(future_class: Any) -> None:
        f1 = future_class()
        f2 = future_class()
        chain_future(f1, f2)
        assert not f2.done()
        f1.set_result(42)
        assert f2.done()
        assert f2.result() == 42
        f3 = future_class()
        f4 = future_class()
        chain_future(f3, f4)
        f3.set_exception(ZeroDivisionError())
        assert f4.exception() is not None

    yield run_test, Future
    yield run_test, futures.Future


if __name__ == "__main__":
    import unittest
    import test_future

    unittest.main()

# Generated at 2022-06-14 11:55:18.118003
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, "test")
    assert future.result() == "test"
    future.set_result(None)
    future.cancel()
    future_set_result_unless_cancelled(future, "test")
    assert future.cancelled()


# Generated at 2022-06-14 11:56:10.561921
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import unittest
    from tornado.testing import AsyncTestCase

    if sys.version_info >= (3, 7):
        # asyncio.ensure_future() not defined in 3.5
        return

    class ChainFutureTest(AsyncTestCase):
        def setUp(self):
            super().setUp()
            self.executor = concurrent.futures.ThreadPoolExecutor(2)
            self.loop = asyncio.new_event_loop()
            self.addCleanup(lambda: self.loop.close())

        def test_sync(self):
            future = futures.Future()
            chain_future(future, self.loop.create_future())
            self.assertEqual(self.loop.run_until_complete(future), None)


# Generated at 2022-06-14 11:56:16.677748
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.ioloop import IOLoop

    loop = IOLoop.current()
    f = Future()

    def fb():
        f.set_result(1)

    def fa():
        future_set_exception_unless_cancelled(f, Exception())

    loop.spawn_callback(fb)
    loop.spawn_callback(fa)
    loop.run_sync(lambda: f)

# Generated at 2022-06-14 11:56:23.135235
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    executor = DummyExecutor()

    def foo(a: int, b: int) -> int:
        return a + b

    future = executor.submit(foo, 1, 2)
    future_set_result_unless_cancelled(future, 3)
    assert future.result() == 3


# Generated at 2022-06-14 11:56:36.437799
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.ioloop import IOLoop

    class TestChainFuture(AsyncTestCase):
        def test_chain_future_aio_aio(self):
            ioloop = IOLoop.current()  # type: IOLoop
            a = Future()
            b = Future()
            chain_future(a, b)
            ioloop.add_callback(a.set_result, 42)
            self.assertEqual(42, ioloop.run_sync(b.result))

        @gen_test
        def test_chain_future_aio_cf(self):
            ioloop = IOLoop.current()  # type: IOLoop
            a = Future()
            b = futures.Future()
            chain_future(a, b)

# Generated at 2022-06-14 11:56:43.717219
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def late_fail(future):
        # type: (Future) -> None
        io_loop.call_later(0.01, functools.partial(future_set_exception_unless_cancelled, future, ValueError()))

    def late_success(future):
        # type: (Future) -> None
        io_loop.call_later(0.01, functools.partial(future_set_result_unless_cancelled, future, 1))

    def late_result(future):
        # type: (Future) -> None
        io_loop.call_later(0.01, functools.partial(future_set_result_unless_cancelled, future, 1))

    io_loop = IOLoop.current()

    # First test that cancellation of the first future stops

# Generated at 2022-06-14 11:56:52.118559
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()

    chain_future(a, b)

    def cb(future):
        raise Exception("should not be called")

    b.add_done_callback(cb)

    IOLoop.current().add_timeout(timedelta(seconds=0.01), a.set_result, "foo")

    IOLoop.current().add_timeout(timedelta(seconds=0.02), IOLoop.current().stop)
    IOLoop.current().start()

    assert not b.done()
    b.cancel()
    assert b.cancelled()
    assert not b.done()
    a.cancel()
    assert a.cancelled()
    assert b.cancelled()
    assert b.done()



# Generated at 2022-06-14 11:57:00.033480
# Unit test for function run_on_executor
def test_run_on_executor():
    class Example(object):
        def __init__(self, executor):
            self.executor = executor

        @run_on_executor(executor="executor")
        def sync_function(self):
            return 42

        @run_on_executor(executor="executor")
        def sync_function_exception(self):
            raise Exception("xxxx")

    def f(future):
        assert future.result() == 42

    def f_exception(future):
        try:
            future.result()
            assert False
        except Exception as e:
            assert str(e) == "xxxx"

    try:
        asyncio.get_event_loop().run_until_complete(main())
    except RuntimeError as e:
        print("RuntimeError: %s" % e)
        assert False

   

# Generated at 2022-06-14 11:57:08.054137
# Unit test for function chain_future
def test_chain_future():  # pragma: no cover
    # This test requires the tornado.platform.asyncio event loop
    from tornado.platform.asyncio import AsyncIOMainLoop

    loop = AsyncIOMainLoop()
    loop.make_current()
    done = False

    def callback(f):
        assert f.done()
        assert f.result() == 5
        nonlocal done
        done = True

    f = Future()
    chain_future(f, Future())
    f.set_result(42)
    f2 = Future()
    chain_future(f, f2)
    chain_future(f, Future())
    chain_future(f2, Future())
    f2.add_done_callback(callback)
    f2.set_result(5)
    assert done

    done = False


# Generated at 2022-06-14 11:57:14.729958
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    assert future.result() == 1
    future.cancel()
    future_set_result_unless_cancelled(future, 2)
    assert future.result() == 1
    assert future.cancelled()

# Generated at 2022-06-14 11:57:21.628673
# Unit test for function chain_future
def test_chain_future():
    # yes, this is a terrible way to unit test...

    f1 = Future()
    f2 = Future()

    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(42)
    assert f2.done()
    assert f2.result() == 42

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    tb = None
    try:
        raise Exception()
    except Exception:
        tb = sys.exc_info()
    f1.set_exc_info(tb)
    assert f2.done()
    assert f2.exception() is not None

    f1 = Future()
    f2 = Future()

# Generated at 2022-06-14 11:59:10.119594
# Unit test for function chain_future
def test_chain_future():
    import random
    import time

    # Test the chain_future function by having thread B sleep for some
    # random time and then return the current time.  Since B will be
    # waiting for a while and A is not, A's future should return
    # before B's does.

    # The thread pool used by the executor.  Using a pool of one thread
    # guarantees that the two futures are handled sequentially instead
    # of concurrently.  (At least on Python 2.)
    executor = futures.ThreadPoolExecutor(max_workers=1)

    # Time that the first thread slept before completing
    a_time = None
    # Time that the second thread slept before completing
    b_time = None

    def a_done(future):
        nonlocal a_time
        a_time = time.time()


# Generated at 2022-06-14 11:59:20.104533
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
    f2.set_result(42)
    g2.set_result(24)
    assert f2.result() == 42
    assert g2.result() == 24



# Generated at 2022-06-14 11:59:26.387364
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    def handle(future):
        future_set_exception_unless_cancelled(current, exc)

    loop = asyncio.get_event_loop()
    current = Future()
    exc = Exception()
    loop.call_soon(handle, current)
    current.cancel()
    loop.run_until_complete(current)
    loop.close()

# Generated at 2022-06-14 11:59:33.307541
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest.mock
    import tornado

    class MockIOLoop:
        def add_future(self, future, callback):
            future.add_done_callback(callback)

    class MockExecutor:
        def submit(self, fn, *args, **kwargs):
            fn(*args, **kwargs)

        def shutdown(self, wait=True):
            pass

    def callback(fut):
        pass

    def fn(self):
        pass

    class Foo:
        executor = MockExecutor()
        io_loop = MockIOLoop()

    foo = Foo()

# Generated at 2022-06-14 11:59:41.467299
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    c = Future()
    chain_future(b, c)

    a.set_result(42)
    assert b.result() == 42
    assert c.result() == 42

    a = Future()
    b = Future()
    chain_future(a, b)
    c = Future()
    chain_future(b, c)

    a.set_exception(Exception("test"))
    assert b.exception()
    assert c.exception()

# Generated at 2022-06-14 11:59:48.680758
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    result: Optional[Exception] = None
    inner = Future()
    outer = Future()

    def outer_handler(future: "Future[_T]") -> None:
        nonlocal result
        result = inner.exception()

    outer.add_done_callback(outer_handler)
    future_set_exception_unless_cancelled(inner, RuntimeError("foo"))
    future_set_exc_info(inner, (RuntimeError, RuntimeError("foo"), None))

    assert result.args == ("foo",)

    inner = Future()
    outer = Future()
    outer.cancel()
    future_set_exception_unless_cancelled(inner, RuntimeError("bar"))
    future_set_exc_info(inner, (RuntimeError, RuntimeError("bar"), None))
    assert inner.exception() is None

# Generated at 2022-06-14 11:59:52.409111
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42



# Generated at 2022-06-14 11:59:58.462670
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()

    # Should not log if future is not cancelled
    f.set_exception(ValueError())
    assert f.exception() is not None

    # Should not log if future is cancelled
    f = Future()
    f.cancel()
    f.set_exception(ValueError())
    assert f.exception() is None



# Generated at 2022-06-14 12:00:03.938936
# Unit test for function chain_future
def test_chain_future():
    from tornado import testing

    @testing.gen_test
    def test_chain_future():
        a = Future()
        b = Future()
        chain_future(a, b)
        a.set_result(42)
        self.assertEqual(42, (yield b))

    # Unit test for function future_set_exc_info

# Generated at 2022-06-14 12:00:15.542702
# Unit test for function chain_future
def test_chain_future():
    '''
        Test the function chain_future
    '''
    def fn(a):
        return a

    async def async_fn(x):
        return await async_future(fn(x))

    def callback(fut):
        f1.set_result(fut.result())
        try:
            print('f1:', f1.result())
        except Exception as e:
            f1.set_exception(e)

    # Test for loop run_until_complete
    f = async_fn(10)
    # f = future_wrap(fn(10))
    # f = fn(10)
    # f = future_wrap(fn(10))
    f1 = Future()
    print('f1', f1)
    chain_future(f, f1)