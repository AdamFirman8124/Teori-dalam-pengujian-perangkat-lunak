

# Generated at 2022-06-14 11:50:11.296213
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, ValueError())
    assert(future.exception() is not None)

# Generated at 2022-06-14 11:50:20.050306
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    f.set_result('f set_result')
    assert f.cancelled() == False
    future_set_result_unless_cancelled(f, 'future_set_result_unless_cancelled')
    assert f.result() == 'f set_result'
    f2 = Future()
    assert f2.cancelled() == False
    assert f2.done() == False
    future_set_result_unless_cancelled(f2, 'future_set_result_unless_cancelled')
    assert f2.result() == 'future_set_result_unless_cancelled'


# Generated at 2022-06-14 11:50:30.514098
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    future3 = Future()

    exception = None
    try:
        raise ValueError()
    except ValueError:
        exception = sys.exc_info()

    chain_future(future1, future2)
    chain_future(future1, future3)

    future1.set_result(42)
    assert future2.result() == 42
    assert future3.result() == 42

    future1 = Future()
    chain_future(future1, future2)
    future1.set_exception(ZeroDivisionError)
    assert future2.exception() == ZeroDivisionError

    future1 = Future()
    chain_future(future1, future2)
    future1.set_exc_info(exception)
    assert future2.exception() == ValueError

# Generated at 2022-06-14 11:50:42.804103
# Unit test for function chain_future
def test_chain_future():
    import unittest

    class TestFuture(Future):
        def __init__(self) -> None:
            super(TestFuture, self).__init__()
            self.exception = None
            self.result = None

        def done(self) -> bool:
            return self.exception is not None or self.result is not None

        def set_result(self, result: _T) -> None:
            self.result = result

        def set_exception(self, exception: BaseException) -> None:
            self.exception = exception

        def result(self) -> _T:
            if self.exception is not None:
                raise self.exception
            else:
                return typing.cast(_T, self.result)


# Generated at 2022-06-14 11:50:50.731190
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.testing import AsyncTestCase, gen_test

    class TestChain(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            # type: () -> None
            a = Future()
            b = Future()
            chain_future(a, b)
            self.assertFalse(b.done())
            a.set_result(None)
            self.assertTrue(b.done())

    test = TestChain()
    test.test_chain_future()



# Generated at 2022-06-14 11:50:55.401635
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def expect_result(future, result):
        # type: (Future[_T], Any) -> None
        try:
            assert future.result() == result
        except Exception:
            future.set_exc_info(sys.exc_info())

    async_future = Future()
    conc_future = futures.Future()
    chain_future(conc_future, async_future)
    conc_future.set_result(42)
    async_future.add_done_callback(functools.partial(expect_result, result=42))
    assert chain_future.__name__ == "chain_future"



# Generated at 2022-06-14 11:51:05.119462
# Unit test for function run_on_executor
def test_run_on_executor():
    import tornado.concurrent
    import tornado.ioloop
    import unittest

    @run_on_executor
    def foo(a):
        return a

    class TestRunOnExecutor(unittest.TestCase):
        def test_run_on_executor(self):
            @run_on_executor
            def bar(a):
                return a

            class Test(object):
                executor = dummy_executor

                def test_method(self):
                    return bar(1)

            y = Test().test_method()
            self.assertTrue(isinstance(y, tornado.concurrent.Future))
            self.assertEqual(y.result(), 1)

            ioloop = tornado.ioloop.IOLoop.current()


# Generated at 2022-06-14 11:51:15.971551
# Unit test for function chain_future
def test_chain_future():
    import tornado.platform.asyncio

    @tornado.platform.asyncio.to_asyncio_future
    def f():
        return "foo"

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(42)
    assert f2.result() == 42
    f1 = f()
    f2 = Future()
    chain_future(f1, f2)
    assert f2.result() == "foo"
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f2.set_result(42)
    assert not f1.done()
    f1.set_result(37)

# Generated at 2022-06-14 11:51:18.558051
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    dummy_executor.submit(test_DummyExecutor_submit)
    assert 1 == 1

# Generated at 2022-06-14 11:51:31.592436
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing
    from tornado import gen
    from tornado.ioloop import IOLoop

    ioloop = IOLoop()

    @gen.coroutine
    def test_future():
        f = Future()
        g = Future()
        chain_future(f, g)
        f.set_result(42)
        assert g.done()
        assert g.result() == 42
        # Make sure original exception and traceback are preserved.
        exc = RuntimeError()
        f2 = Future()
        g2 = Future()
        chain_future(f2, g2)
        f2.set_exception(exc)
        assert g2.exception() is exc
        # If a is already done, b should be called immediately.
        h = Future()
        h.set_result(None)
        i = Future

# Generated at 2022-06-14 11:51:44.302408
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.ioloop import IOLoop
    from tornado.concurrent import Future

    class Foo:
        def __init__(self, loop):
            self.loop = loop
            self.executor = dummy_executor

        @run_on_executor()
        def sleep(self, arg):
            self.loop.add_callback(self.sleep_done)
            return arg

        def sleep_done(self):
            self.loop.stop()

    loop = IOLoop(make_current=False)

    f = Foo(loop)
    future = f.sleep(5)
    self.assertEqual(5, future.result())
    loop.start()



# Generated at 2022-06-14 11:51:50.302519
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing

    future1 = Future()

    @gen.coroutine
    def test_chain():
        future2 = Future()
        chain_future(future1, future2)
        assert not future2.done()
        future1.set_result(42)
        result = yield future2
        assert result == 42
        future3 = Future()
        chain_future(future1, future3)
        result = yield future3
        assert result == 42

    tornado.testing.gen_test(test_chain)()

# Generated at 2022-06-14 11:51:51.114034
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    pass # TODO




# Generated at 2022-06-14 11:51:58.233517
# Unit test for function run_on_executor
def test_run_on_executor():
    def f(self, a, b):
        pass

    class A(object):
        def __init__(self, executor):
            self.executor = executor
    self = A(executor=dummy_executor)
    ret = run_on_executor(f)
    assert isinstance(ret, types.FunctionType)
    assert ret.__name__ == "f"
    wrapped = ret(self)
    assert isinstance(wrapped, Future)
    wrapped.result()
    with pytest.raises(TypeError):
        ret = run_on_executor(f, executor=1)

# Generated at 2022-06-14 11:52:06.518442
# Unit test for function chain_future
def test_chain_future():
    import logging
    import unittest
    from tornado.test.util import multi_async

    logging.getLogger().setLevel(logging.DEBUG)

    @multi_asyncio_test
    def test_asyncio_future(self, io_loop):
        a = Future()
        b = Future()
        chain_future(a, b)
        io_loop.add_future(a, self.stop)
        io_loop.add_future(b, self.stop)
        io_loop.call_later(0.1, a.set_result, 42)
        self.wait()
        self.assertEqual(42, b.result())
        a = Future()
        b = Future()
        chain_future(a, b)
        io_loop.add_future(a, self.stop)

# Generated at 2022-06-14 11:52:17.767044
# Unit test for function chain_future
def test_chain_future():
    def callback(arg):
        pass

    # Test with Future
    f = Future()
    test_f = Future()
    chain_future(f, test_f)
    assert test_f.done() is False
    f.set_result(42)
    assert test_f.done() is True
    assert test_f.result() == 42

    # Test with concurrent.futures.Future
    f = futures.Future()
    test_f = Future()
    chain_future(f, test_f)
    assert test_f.done() is False
    f.set_result(42)
    assert test_f.done() is True
    assert test_f.result() == 42

    # Test that exceptions propagate
    f = Future()
    test_f = Future()

# Generated at 2022-06-14 11:52:24.813162
# Unit test for function chain_future
def test_chain_future():
    a = Future()  # type: Future[_T]
    b = Future()  # type: Future[_T]
    a.set_result(1)
    chain_future(a, b)
    assert b.result() == 1
    a = Future()  # type: Future[_T]
    b = Future()  # type: Future[_T]
    b.set_result(2)
    chain_future(a, b)
    assert b.result() == 2
    a = Future()  # type: Future[_T]
    b = Future()  # type: Future[_T]
    a.set_exception(ValueError())
    chain_future(a, b)
    assert not b.cancelled()
    assert isinstance(b.exception(), ValueError)
    a = Future()  # type: Future[_

# Generated at 2022-06-14 11:52:36.399708
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    exception = Exception("example")
    async_future = asyncio.Future()
    future_set_exception_unless_cancelled(async_future, exception)
    result = async_future.exception()
    assert result is exception

    conc_future = futures.Future()
    future_set_exception_unless_cancelled(conc_future, exception)
    result = conc_future.exception()
    assert result is exception

    async_future = asyncio.Future()
    async_future.cancel()
    future_set_exception_unless_cancelled(async_future, exception)

    conc_future = futures.Future()
    conc_future.cancel()
    future_set_exception_unless_cancelled(conc_future, exception)



# Generated at 2022-06-14 11:52:49.641547
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import time
    from tornado.platform.asyncio import AsyncIOMainLoop

    @unittest.skipUnless(sys.version_info >= (3, 5), "requires python3.5")
    class TestChainFuture(unittest.TestCase):
        def setUp(self):
            self.io_loop = AsyncIOMainLoop()
            self.io_loop.make_current()
            self.executor = dummy_executor
            # self.executor = ThreadPoolExecutor(1)

        def tearDown(self):
            # self.executor.shutdown()
            self.io_loop.close()

        def test_chain_future(self):
            res_a = None
            res_b = None
            res_c = None
            res_d = None

           

# Generated at 2022-06-14 11:52:57.367036
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42

    # Verify that an exception is transferred.  Although the second
    # future should never actually complete with an exception, there's
    # no harm in being robust against that.
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ZeroDivisionError())
    assert f2.exception() is not None
    f3 = Future()
    f1.add_done_callback(lambda f: chain_future(f, f3))
    f1.set_result(42)
    assert f3.result() == 42

    # Verify that an exception is not transferred

# Generated at 2022-06-14 11:53:08.427037
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.set_result(None)
    future_set_exception_unless_cancelled(future, RuntimeError())
    assert future.exception() is not None

    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, RuntimeError())
    assert future.exception() is None

# Generated at 2022-06-14 11:53:15.808302
# Unit test for function chain_future
def test_chain_future():
    io_loop = tornado.ioloop.IOLoop()
    io_loop.make_current()

    def obj_pass(o):
        return o

    @run_on_executor
    def exception():
        raise Exception()

    @run_on_executor
    def data(value):
        return value

    @tornado.gen.coroutine
    def test_on_success():
        f1 = tornado.gen.maybe_future(obj_pass(1))
        f2 = tornado.gen.maybe_future(obj_pass(2))
        f3 = tornado.gen.maybe_future(obj_pass(3))
        f4 = tornado.gen.maybe_future(obj_pass(4))
        f5 = tornado.gen.maybe_future(obj_pass(5))


# Generated at 2022-06-14 11:53:22.441283
# Unit test for function chain_future
def test_chain_future():
    from tornado.queues import Queue
    from tornado import gen

    async def main() -> None:
        q = Queue()
        for i in range(4):
            await q.put(i)
        for i in range(4):
            await q.put(i)
        for i in range(4):
            assert await q.get() == i

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# Generated at 2022-06-14 11:53:27.683158
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    g = Future()

    def f_done(future):
        g.set_result(future.result() + 1)

    chain_future(f, g)
    f.add_done_callback(f_done)
    f.set_result(5)
    assert g.result() == 6

# Generated at 2022-06-14 11:53:36.201775
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    exc = RuntimeError()
    future_set_exception_unless_cancelled(future, exc)
    assert not future.cancelled()
    assert future.done()
    assert future.exception() == exc

    future = Future()
    future.cancel()
    exc = RuntimeError()
    future_set_exception_unless_cancelled(future, exc)
    assert future.cancelled()
    assert future.done()
    assert future.exception() is None



# Generated at 2022-06-14 11:53:38.411901
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future_set_result_unless_cancelled(Future(), 5)
    future_set_result_unless_cancelled(Future(), 2)

# Generated at 2022-06-14 11:53:50.053297
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop()
    async_future = Future()
    conc_future = None
    called = [0]

    def mark_done(future):
        called[0] += 1

    def finalize():
        future_set_result_unless_cancelled(async_future, 42)
        io_loop.stop()

    io_loop.add_callback(finalize)
    future_add_done_callback(async_future, mark_done)
    chain_future(conc_future, async_future)
    io_loop.start()
    assert called[0] == 1
    assert async_future.result() == 42

# Generated at 2022-06-14 11:53:55.166421
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = asyncio.Future()
    future_set_exception_unless_cancelled(future, Exception("test"))
    assert future.exception()
    assert not future.cancelled()

    future = asyncio.Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception("test"))
    assert future.cancelled()

# Generated at 2022-06-14 11:54:03.994178
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    try:
        raise RuntimeError("test")
    except Exception as e:
        future_set_exception_unless_cancelled(future, e)
        assert future.exception() is e
    future.cancel()
    try:
        raise RuntimeError("test")
    except Exception as e:
        future_set_exception_unless_cancelled(future, e)
        assert future.cancelled()
    assert_raises(asyncio.InvalidStateError, future.exception)

# Generated at 2022-06-14 11:54:13.539486
# Unit test for function chain_future
def test_chain_future():
    # Create a future object for testing.
    future = Future()

    # Create a RunLoop for the tests.
    from tornado.ioloop import IOLoop

    loop = IOLoop.current()

    # Create the callback to be called when the future is done.
    def callback(future_obj):
        assert future_obj is future
        loop.stop()

    # Chain the future.
    chain_future(future, callback)

    # Test the callback is called when the chained future is complete.
    future.set_result(42)
    loop.start()
    assert future.result() == 42

    # Create another future object for testing.
    future = Future()

    # Create the callback to be called when the future is done.
    def callback(future_obj):
        assert future_obj is future
        # Set another result for the future

# Generated at 2022-06-14 11:54:44.905141
# Unit test for function chain_future
def test_chain_future():
    import time
    import unittest
    import weakref
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase, ExpectLog

    from tornado.platform.asyncio import to_asyncio_future
    from concurrent.futures import Future as ConcFuture

    class FutureTestMixin:
        def test_done_callback(self):
            IOLoop.current().add_callback(self._test_done_callback)
            self.wait()

        def _make_future(self) -> "Future":
            raise NotImplementedError()

        def _test_done_callback(self):
            future = self._make_future()
            results = []
            future_add_done_callback(future, results.append)
            self.assertFalse(results)
            future_set_result_unless

# Generated at 2022-06-14 11:54:50.004587
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    assert future.result() == 1
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 1)
    assert future.result() is None


# Generated at 2022-06-14 11:55:00.415887
# Unit test for function chain_future
def test_chain_future():
    import functools
    import logging
    import time
    import unittest

    from tornado.log import enable_pretty_logging
    from tornado.testing import AsyncTestCase, gen_test

    enable_pretty_logging()
    logging.getLogger().setLevel(logging.DEBUG)


    class TestFuture(AsyncTestCase):
        def setUp(self):
            super(TestFuture, self).setUp()
            self.values = []  # type: typing.List[Any]

        def callback(self, future: Future) -> None:
            self.values.append(future.result())

        def test_chain_future_asynchronous(self):
            """Tests that the result of a is copied to b."""
            a = Future()  # type: Future[int]
            b = Future()  # type

# Generated at 2022-06-14 11:55:06.026530
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    def test(future):
        assert future.done()
        assert future.result() == 1
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    future.add_done_callback(test)

# Generated at 2022-06-14 11:55:17.359143
# Unit test for function chain_future
def test_chain_future():
    import asyncio
    import concurrent.futures
    import functools
    import time
    import unittest

    f1 = Future()
    f2 = concurrent.futures.Future()
    f3 = Future()
    f4 = concurrent.futures.Future()
    chain_future(f1, f2)
    chain_future(f2, f3)
    chain_future(f3, f4)
    f1.set_result(1)
    assert f1.result() == 1
    assert f2.result() == 1
    assert f3.result() == 1
    assert f4.result() == 1

    f1 = Future()
    f2 = concurrent.futures.Future()
    chain_future(f1, f2)
    f1.set_result(2)


# Generated at 2022-06-14 11:55:28.365615
# Unit test for function chain_future
def test_chain_future():  # pragma: no cover
    import logging
    import functools
    import unittest
    from tornado.ioloop import IOLoop

    class MyFuture(Future):
        pass

    class TestChainFuture(unittest.TestCase):
        def setUp(self):
            self.io_loop = IOLoop()

        def test_chain_future_asyncio(self):
            future1 = MyFuture()
            future2 = MyFuture()

            # create a new MyFuture object and chain it with future1.
            chain_future(future1, future2)
            future1.set_result(42)
            self.assertEqual(future2.result(), 42)

        def test_chain_future_concurrent(self):
            future1 = futures.Future()
            future2 = MyFuture()
            chain_future

# Generated at 2022-06-14 11:55:33.162911
# Unit test for function chain_future
def test_chain_future():  # pragma: no cover
    # type: () -> None
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase, gen_test

    class TestChainFuture(AsyncTestCase):
        def test_chain_future(self):
            # type: () -> None
                f1 = Future()
                f2 = Future()
                chain_future(f1, f2)
                f1.set_result(42)
                self.assertEqual(f2.result(), 42)

        @gen_test
        def test_chain_future_exc(self):
            # type: () -> None
                f1 = Future()
                f2 = Future()
                chain_future(f1, f2)
                f1.set_exception(ZeroDivisionError)

# Generated at 2022-06-14 11:55:40.762497
# Unit test for function chain_future
def test_chain_future():
    loop = asyncio.get_event_loop()
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert f2.done() == False
    f1.set_result(1)
    assert f2.done() == False
    loop.run_until_complete(f2)
    assert f2.result() == 1
    loop.close()



# Generated at 2022-06-14 11:55:50.257582
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    future3 = Future()
    chain_future(future1, future2)
    chain_future(future1, future3)
    future1.set_result(42)
    assert future2.result() == 42
    assert future3.result() == 42

    # An error on the first future should propagate to all the rest.
    future1 = Future()
    future2 = Future()
    future3 = Future()
    chain_future(future1, future2)
    chain_future(future1, future3)
    future1.set_exception(ZeroDivisionError())
    assert future2.exception() is not None
    assert future2.exc_info()[1].__class__ == ZeroDivisionError
    assert future3.exception() is not None

# Generated at 2022-06-14 11:56:04.140381
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    if a.done():
        raise Exception("expected a to be pending, not done")
    if b.done():
        raise Exception("expected b to be pending, not done")
    b.set_result(None)
    if not a.done():
        raise Exception("expected a to be done")
    if not b.done():
        raise Exception("expected b to be done")
    try:
        a.result()
    except futures.CancelledError:
        pass
    else:
        raise Exception("expected a to be cancelled")

    a = Future()
    b = Future()
    chain_future(a, b)
    if a.done():
        raise Exception("expected a to be pending, not done")

# Generated at 2022-06-14 11:56:42.279860
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class TestChainFuture(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            @gen.coroutine
            def get_future() -> Future:
                f = Future()  # type: Future[int]
                f.set_result(1)
                raise gen.Return(f)

            @gen.coroutine
            def func() -> int:
                f1 = yield get_future()
                f2 = Future()  # type: Future[int]
                chain_future(f1, f2)
                result = yield f2
                self.assertEqual(result, 1)

            yield func()

# Generated at 2022-06-14 11:56:56.885782
# Unit test for function chain_future
def test_chain_future():
    import time
    import unittest.mock
    import concurrent.futures
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase, gen_test

    f1 = Future()
    f2 = Future()
    f3 = concurrent.futures.Future()

    chain_future(f1, f2)
    IOLoop.current().add_future(f1, lambda f: f2.set_result(None))
    chain_future(f1, f3)
    IOLoop.current().add_future(f3, lambda f: f2.set_result(None))

    m1 = unittest.mock.Mock()
    m2 = unittest.mock.Mock()
    m3 = unittest.mock.Mock()
    f

# Generated at 2022-06-14 11:57:05.089163
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f1 = Future()
    f2 = Future()
    f2.cancel()
    future_set_exception_unless_cancelled(f1, ValueError())
    future_set_exception_unless_cancelled(f2, ValueError())

# Generated at 2022-06-14 11:57:17.755608
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, RuntimeError("boom"))
    assert future.exception() is not None
    future_set_exception_unless_cancelled(future, ValueError("also boom"))
    assert isinstance(future.exception(), RuntimeError)
    assert str(future.exception()) == 'boom'
    future.cancel()
    future_set_exception_unless_cancelled(future, RuntimeError("not called"))
    assert isinstance(future.exception(), RuntimeError)
    assert str(future.exception()) == 'boom'
    assert future.cancelled()

# Generated at 2022-06-14 11:57:23.995412
# Unit test for function chain_future
def test_chain_future():
    async def test_coroutine():
        # type: () -> None
        f1 = Future()
        f2 = Future()
        f3 = Future()
        chain_future(f1, f2)
        chain_future(f2, f3)
        f1.set_result("foo")
        assert (await f3) == "foo"
    return test_coroutine()

# Generated at 2022-06-14 11:57:27.690587
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    # type: () -> None
    exec = DummyExecutor()
    future = exec.submit(lambda x: x, 1)
    value = future.result()
    assert value == 1


# Generated at 2022-06-14 11:57:38.614751
# Unit test for function chain_future
def test_chain_future():
    import unittest

    class TestChainFuture(unittest.TestCase):
        def test_success(self):
            f1 = concurrent.futures.Future()
            f2 = Future()
            chain_future(f1, f2)
            self.assertFalse(f1.done())
            self.assertFalse(f2.done())
            f1.set_result(42)
            self.assertTrue(f1.done())
            self.assertTrue(f2.done())
            self.assertEqual(f2.result(), 42)
            f1 = Future()
            f2 = concurrent.futures.Future()
            chain_future(f1, f2)
            self.assertFalse(f1.done())
            self.assertFalse(f2.done())

# Generated at 2022-06-14 11:57:51.854633
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase, bind_unused_port

    class Test(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            s, port = bind_unused_port()
            f = Future()
            f2 = Future()
            chain_future(f2, f)

            def set1(arg):
                self.io_loop.add_timeout(self.io_loop.time() + 0.05, lambda: set2(arg))

            def set2(arg):
                f.set_result(arg)

            async def a1():
                f2.set_result(5)
                return await f

            self.assertEqual(self.io_loop.run_sync(a1), 5)
            s.close()

    test = Test

# Generated at 2022-06-14 11:58:02.774493
# Unit test for function chain_future
def test_chain_future():
    class SomeError(Exception):
        pass

    def callback(fut):
        assert not fut.cancelled()
        assert not fut.done()

    def callback2(fut):
        raise SomeError()

    def callback3(fut):
        assert not fut.cancelled()
        assert fut.done()
        assert fut.exception() is not None
        assert isinstance(fut.exception(), SomeError)

    fut1 = Future()
    fut2 = Future()
    chain_future(fut1, fut2)
    future_add_done_callback(fut2, callback)
    fut1.set_exception(SomeError())
    future_add_done_callback(fut2, callback2)
    future_add_done_callback(fut2, callback3)

# Generated at 2022-06-14 11:58:09.174332
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import time
    from tornado import ioloop

    class Test(unittest.TestCase):
        def setUp(self):
            self.io_loop = ioloop.IOLoop()
            self.io_loop.make_current()

        def test_chain_future(self):
            a = Future()
            b = Future()
            self.assertFalse(b.done())
            chain_future(a, b)
            self.assertFalse(b.done())
            a.set_result(42)
            self.assertEqual(b.result(), 42)

        def test_chain_future_cancelled(self):
            a = Future()
            b = Future()
            self.assertFalse(b.done())
            chain_future(a, b)

# Generated at 2022-06-14 11:59:24.243678
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    def cb():
        future_set_exception_unless_cancelled(future, ValueError())
    future.add_done_callback(cb)
    return future


# Generated at 2022-06-14 11:59:29.293238
# Unit test for function chain_future
def test_chain_future():
    @return_future
    def f(future):
        future.set_result(42)

    @return_future
    def g(future, inner_future):
        x = yield inner_future
        future.set_result(x)

    h = g(f())
    i = g(h)

    assert h.result() == 42
    assert i.result() == 42



# Generated at 2022-06-14 11:59:41.573237
# Unit test for function chain_future
def test_chain_future():
    def set_result(x, fut):
        fut.set_result(x)

    def set_exception(x, fut):
        fut.set_exception(Exception(x))

    async def async_test():
        for f in (futures.Future(), Future()):
            f1 = f()
            f2 = f()
            chain_future(f1, f2)
            set_result("result", f1)
            await f2
            try:
                assert False
            except:  # noqa: E722
                # Ensure that the exception is raised after chain_future returns
                pass

            f1 = f()
            f2 = f()
            chain_future(f1, f2)
            set_exception("exception", f1)

# Generated at 2022-06-14 11:59:46.529352
# Unit test for function run_on_executor
def test_run_on_executor():
    class Foo(object):
        def __init__(self, io_loop):
            self.io_loop = io_loop
            self.executor = dummy_executor

    foo = Foo(None)

    @run_on_executor
    def blocking_method(self):
        pass

    @run_on_executor(executor='_thread_pool')
    def blocking_method_2(self):
        pass

    blocking_method(foo)
    blocking_method_2(foo)

# Generated at 2022-06-14 11:59:53.023121
# Unit test for function chain_future
def test_chain_future():
    def f_a():
        return "a"

    def f_b():
        return "b"

    f_future = Future()
    future = Future()
    chain_future(f_future, future)
    f = future_add_done_callback(future, f_b)
    f_future.set_result(f_a)
    assert f_future.result() == "a"
    f is not None

# Generated at 2022-06-14 12:00:02.270148
# Unit test for function chain_future
def test_chain_future():
    from tornado import gen
    import unittest

    result = [None]

    async def f():
        await gen.moment
        result[0] = 1

    def f_result(f: Future) -> None:
        result[0] += 2

    chain_future(f(), f_result)
    assert result[0] == 1

    chain_future(f().result(), f_result)
    assert result[0] == 4

    chain_future(f().result(), f_result)
    assert result[0] == 4

    async def f_err():
        raise Exception

    chain_future(f_err(), f_result)
    assert result[0] == 4

    chain_future(f_err().result(), f_result)
    assert result[0] == 4


# Generated at 2022-06-14 12:00:14.813103
# Unit test for function run_on_executor
def test_run_on_executor():
    _result = object()
    _exc_info = (Exception, Exception("foo"), None)

    class _FakeThreadPoolExecutor(object):
        def __init__(self):
            self.future = None  # type: Optional[futures.Future[_T]]

        def submit(self, fn, *args, **kwargs):
            self.future = futures.Future()  # type: futures.Future[_T]
            # Simulate a common failure mode of a thread pool executor
            # that throws when the thread is started rather than when
            # the function is run.
            if fn is _error_task:
                self.future.set_exception(_exc_info[1])
            return self.future

    executor = _FakeThreadPoolExecutor()

    class _Test(object):
        executor = executor
