

# Generated at 2022-06-14 11:50:18.382633
# Unit test for function chain_future
def test_chain_future():  # type: ignore
    if sys.version_info >= (3, 0):
        return
    from tornado.ioloop import IOLoop

    io_loop = IOLoop.current()

    f1, f2 = Future(), Future()
    chain_future(f1, f2)
    f1.set_result("f1")
    io_loop.add_callback(io_loop.stop)
    io_loop.start()
    assert f2.result() == "f1"

# Generated at 2022-06-14 11:50:23.470334
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():  # pragma: nocover
    f = Future()
    f.cancel() # cancel it so future.exception() is not None.
    future_set_exc_info(f, sys.exc_info()) # ignore exception



# Generated at 2022-06-14 11:50:27.654145
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from tornado import gen

    e = dummy_executor
    ioloop = asyncio.get_event_loop()

    @gen.coroutine
    def test_sync():
        f = e.submit(lambda x: x + 1, 1)
        assert f.done()
        assert f.result() == 2
        f = e.submit(lambda x: x + 1, 1)
        f.cancel()
        assert f.done()
        assert f.result() == 2
        assert f.cancelled()

    ioloop.run_sync(test_sync)
    e.shutdown()
    # The executor is singleton, so all tests share the same executor object.
    assert e.shutdown_called



# Generated at 2022-06-14 11:50:29.360085
# Unit test for function chain_future
def test_chain_future():
    async def f():
        ...
    f()

# Generated at 2022-06-14 11:50:41.534960
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.platform.asyncio import to_asyncio_future
    from tornado.ioloop import IOLoop
    import asyncio
    import types

    class MyClass:
        executor = dummy_executor

        def __init__(self, x):
            self.x = x

        @run_on_executor
        def f(self):
            return self.x

    with AsyncIOMainLoop() as loop:
        obj = MyClass(10)
        result = yield to_asyncio_future(obj.f())
        assert result == 10

    with IOLoop() as loop:
        obj = MyClass(12)
        result = yield obj.f()
        assert result == 12



# Generated at 2022-06-14 11:50:48.470722
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()

    chain_future(future1, future2)

    future1.set_result(42)

    assert future2.done()
    assert future2.result() == 42



# Generated at 2022-06-14 11:50:55.774003
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    f2 = Future()
    chain_future(f, f2)
    assert not f2.done()
    f.set_result(42)
    assert f2.result() == 42
    f3 = Future()
    chain_future(f, f3)
    assert f3.result() == 42

# Generated at 2022-06-14 11:51:05.327941
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import unittest.mock

    future = Future()
    chained_future = Future()
    chain_future(future, chained_future)

    future.set_result(1)
    assert chained_future.result() == 1

    future = Future()
    chained_future = Future()
    chain_future(future, chained_future)

    future.set_exception(ValueError())
    assert isinstance(chained_future.exception(), ValueError)

    future = Future()
    chained_future = Future()
    chained_future.cancel()

    chain_future(future, chained_future)
    with unittest.mock.patch("tornado.concurrent.chain_future") as mocked:
        future.set_result(1)
        assert not mocked.called


# Generated at 2022-06-14 11:51:10.381288
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    future_set_result_unless_cancelled(f, 42)

    def cb(future):
        future.set_result(42)

    future_add_done_callback(f, cb)

    assert (f.result() == 42)


# Generated at 2022-06-14 11:51:15.902775
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, ValueError())
    assert future.exception() is not None
    future_set_exception_unless_cancelled(future, ValueError())
    # the log handler catches this exception because it's been raised
    # from a thread
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError())

# Generated at 2022-06-14 11:51:32.541055
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    def f(x, y):
        # type: (int, int) -> int
        return x + y

    ioloop = IOLoop()

    f1 = Future()  # type: Future[int]
    f2 = Future()  # type: Future[int]
    chain_future(f1, f2)
    f1.set_result(2)
    f2.result()

    def cb(fut):
        assert not fut.cancelled()
        assert fut.result() == 6
        assert not f1.cancelled()
        assert f1.result() == 2
        ioloop.stop()

    f3 = f1.then(lambda x: f2.then(lambda y: f(x, y)))

# Generated at 2022-06-14 11:51:39.833052
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    class G(object):
        def foo(self, a):
            return a

        @run_on_executor
        def bar(self, a):
            return self.foo(a)

        @property
        def executor(self):
            return dummy_executor

    g = G()
    g.foo(1)
    res = g.bar(1).result()
    print(res)

# Generated at 2022-06-14 11:51:52.588799
# Unit test for function run_on_executor
def test_run_on_executor():
    class Foo(object):
        def __init__(self):
            self.executor = dummy_executor

        @run_on_executor
        def bar(self, arg1, arg2, kwarg=None):
            if kwarg is not None:
                return arg1, arg2, kwarg
            else:
                return arg1, arg2

        @run_on_executor(executor='_thread_pool')
        def grok(self, arg1, arg2, kwarg=None):
            if kwarg is not None:
                return arg1, arg2, kwarg
            else:
                return arg1, arg2


# Generated at 2022-06-14 11:52:03.740486
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    async def async_chain_future() -> None:
        a = Future()  # type: Any
        b = Future()  # type: Any
        chain_future(a, b)
        assert not b.done()
        a.set_result(42)
        assert b.done()
        assert b.result() == 42
        # No exception.
        b = Future()  # type: Any
        chain_future(a, b)
        assert not b.done()
        a.set_exception(RuntimeError())
        assert b.done()
        try:
            b.result()
        except RuntimeError:
            pass
        else:
            assert False
        # Exception already set.
        b = Future()  # type: Any
        chain_future(a, b)
        assert b

# Generated at 2022-06-14 11:52:16.212776
# Unit test for function chain_future
def test_chain_future():
    from tornado.platform.asyncio import to_asyncio_future
    from tornado.testing import AsyncTestCase, gen_test

    class TestChainFuture(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            # type: () -> None
            conc_future = futures.Future()  # type: futures.Future[int]
            async_future = to_asyncio_future(conc_future)  # type: Future[int]
            chain_future(conc_future, async_future)

            conc_future.set_result(42)
            self.assertTrue(conc_future.done())
            self.assertEqual(42, (yield async_future))


# Generated at 2022-06-14 11:52:19.984490
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    class DummyError(Exception):
        pass

    fut = Future()
    fut.set_exception(DummyError())
    # If the method is not robust to future.cancelled() being True, it will
    # raise.
    future_set_exception_unless_cancelled(fut, DummyError())

# Generated at 2022-06-14 11:52:32.706751
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, bind_unused_port, AsyncTestCase

    class Handler(AsyncTestCase):
        def setUp(self):
            super().setUp()
            bind_unused_port()

        @gen_test
        def test_chain(self):
            a = self.get_future()
            b = self.get_future()
            a.set_result(1)
            b.set_result(2)

            # These should not raise an exception.
            chain_future(a, b)
            chain_future(b, a)

# Generated at 2022-06-14 11:52:38.457566
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import BaseAsyncIOLoop
    if isinstance(IOLoop.current(), BaseAsyncIOLoop):
        raise Exception('AsyncIOLoop.current() needs to be an instance of BaseAsyncIOLoop')
    a = dummy_executor.submit(lambda x: 2*x, 2)
    def f(future):
        print(future.result())
        print('f is called')
    a.add_done_callback(f)
    IOLoop.current().start()

# Generated at 2022-06-14 11:52:48.653309
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # Test that deferred exceptions are preserved when cancelling futures.
    # See comments in the function future_set_exception_unless_cancelled.
    exc = ZeroDivisionError()
    err_future = Future()
    err_future.set_exception(exc)
    err_future.cancel()

    exc_info = err_future.exception()
    assert exc == exc_info
    assert exc_info.__traceback__ is not None # type: ignore


if __name__ == "__main__":
    import unittest

    test_future_set_exception_unless_cancelled()

# Generated at 2022-06-14 11:52:52.882909
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():  # noqa: E302
    future = Future()
    future_set_result_unless_cancelled(future, "value")
    assert future.result() == "value"
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, "value")
    assert not future.cancelled()

# Generated at 2022-06-14 11:52:57.219089
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    f.cancel()
    f.result()

# Generated at 2022-06-14 11:53:08.135231
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()
    a.set_result(42)
    assert b.result() == 42
    assert b.done()

    c = Future()
    d = Future()
    chain_future(c, d)
    assert not c.done()
    assert not d.done()
    c.set_exception(ZeroDivisionError())
    assert d.exception() is not None
    assert d.done()
    c.cancel()
    assert c.done()
    assert not c.cancelled()
    assert d.done()
    assert not d.cancelled()
    assert d.exception() is not None

    e = Future()
    f = Future()
    g = Future()
    chain_

# Generated at 2022-06-14 11:53:15.503928
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    try:
        future_set_exception_unless_cancelled(future, RuntimeError())
    except RuntimeError:
        assert False, "future_set_exception_unless_cancelled sets exception even if future is not cancelled"
    assert not future.done(), "future_set_exception_unless_cancelled sets the future's exception even if future is not cancelled"
    future.cancel()
    try:
        future_set_exception_unless_cancelled(future, RuntimeError())
    except RuntimeError:
        assert False, "future_set_exception_unless_cancelled sets exception even if future is cancelled"
    assert not future.done(), "future_set_exception_unless_cancelled sets the future's exception even if future is cancelled"


# Generated at 2022-06-14 11:53:23.940417
# Unit test for function chain_future
def test_chain_future():
    import unittest

    class Test_chain_future(unittest.TestCase):
        def test_chain_future(self):
            a = Future()
            b = Future()
            chain_future(a, b)

            a.set_result(None)
            self.assertTrue(b.done())

            a = Future()
            b = Future()
            chain_future(a, b)

            a.set_exception(Exception())
            self.assertTrue(b.done())
            self.assertTrue(b.exception())

            a = Future()
            b = Future()
            chain_future(a, b)

            b.cancel()
            self.assertTrue(b.done())
            a.set_result(None)
            self.assertTrue(b.done())


# Generated at 2022-06-14 11:53:28.874176
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    assert not future1.done()
    assert not future2.done()
    future1.set_result(42)
    assert future1.done()
    assert future2.done()
    assert future2.result() == 42

# Generated at 2022-06-14 11:53:36.567867
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    @run_on_executor
    def wait_some_time(time):
        import time
        time.sleep(time)

    loop = asyncio.new_event_loop()
    loop.set_debug(True)
    asyncio.set_event_loop(loop)
    f = wait_some_time(0.1)
    f.cancel()
    future_set_exception_unless_cancelled(f, ValueError("test"))

# Generated at 2022-06-14 11:53:43.143603
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import tornado.testing

    @tornado.testing.gen_test(timeout=10)
    def unit_test():
        class ObjectWithExecutor(object):
            executor = None

        @run_on_executor
        def foo(x):
            return x

        @run_on_executor(executor="_thread_pool")
        def bar(x):
            return x

        obj = ObjectWithExecutor()
        with unittest.mock.patch.object(
            ObjectWithExecutor, "executor", new_callable=futures.ThreadPoolExecutor
        ) as executor:
            executor.submit.return_value = futures.Future()
            executor.submit.return_value.result.return_value = 42
            ret = yield foo(obj, 1)
           

# Generated at 2022-06-14 11:53:49.311376
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()

    # This should not raise asyncio.InvalidStateError:
    future_set_exception_unless_cancelled(f, RuntimeError)
    assert f.exception() is not None


if __name__ == "__main__":
    import unittest

    unittest.main()

# Generated at 2022-06-14 11:53:55.288587
# Unit test for function chain_future
def test_chain_future():
    expected_result = object()

    f1 = Future()
    f2 = Future()

    def copy(future: "Future"):
        assert future is f1
        assert not f2.done()
        f2.set_result(f1.result())

    f1.add_done_callback(copy)
    f1.set_result(expected_result)
    result = f2.result()
    assert result is expected_result



# Generated at 2022-06-14 11:54:03.123356
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    run_callback(a)
    assert a.result() is None
    assert b.result() is None

    a.set_result(42)
    assert a.result() == 42
    assert b.result() == 42

    future_add_done_callback(b, lambda f: f.set_result(f.result() * 10))
    assert b.result() == 420



# Generated at 2022-06-14 11:54:17.147469
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = asyncio.Future()
    future_set_exception_unless_cancelled(future, ValueError)
    assert future.exception() == ValueError

    future = asyncio.Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError)
    with pytest.raises(asyncio.InvalidStateError):
        future.exception()

    future = futures.Future()
    future_set_exception_unless_cancelled(future, ValueError)
    assert future.exception() == ValueError

    future = futures.Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError)
    with pytest.raises(futures.CancelledError):
        future.exception()



# Generated at 2022-06-14 11:54:27.883613
# Unit test for function run_on_executor
def test_run_on_executor():
    import concurrent.futures
    import tornado.io_loop
    import tornado.testing

    executor = concurrent.futures.ThreadPoolExecutor(1)

    class MyTest:
        executor = executor

        @tornado.concurrent.run_on_executor
        def foo(self, a, b, c):
            self.result = a + b + c
            return 42

    class MyOtherTest:
        _thread_pool = executor

        @tornado.concurrent.run_on_executor(executor="_thread_pool")
        def bar(self, x, y):
            self.bar_result = x + y
            return 24

    @tornado.gen.coroutine
    def f():
        t1 = MyTest()

# Generated at 2022-06-14 11:54:40.263229
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import unittest
    from unittest import mock
    import sys
    import warnings

    class TestCase(unittest.TestCase):
        def test_future_set_exception_unless_cancelled(self):
            future = Future()
            # Check that future_set_exception_unless_cancelled raises no error
            # when it is called on a non-cancelled future.
            try:
                1 / 0
            except:
                future_set_exc_info(future, sys.exc_info())

            # Check that future_set_exception_unless_cancelled logs the error
            # when it is called on a cancelled future.
            future = Future()
            future.cancel()

# Generated at 2022-06-14 11:54:44.714253
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop, TimeoutError

    io_loop = IOLoop()
    io_loop.make_current()
    io_loop.run_sync(lambda: chain_future(io_loop.add_future(Future()), Future()))

# Generated at 2022-06-14 11:54:53.844001
# Unit test for function chain_future
def test_chain_future():
    import unittest.mock

    af = Future()
    bf = Future()
    af.set_result(1)
    unittest.mock.patch.object(
        af, "add_done_callback", wraps=af.add_done_callback
    ).start()
    unittest.mock.patch.object(
        bf, "set_result", wraps=bf.set_result
    ).start()
    chain_future(af, bf)
    assert bf.result() == 1
    assert af.add_done_callback.called

# Generated at 2022-06-14 11:55:02.180516
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing
    import concurrent.futures

    def run_future(future, fn, *args):
        future_set_result_unless_cancelled(future, fn(*args))

    def long_running_callback(future, callback, *args):
        run_future(future, callback, *args)

    def test_callback(future):
        future.result()

    class TestFuture(tornado.testing.AsyncTestCase):
        def setUp(self):
            super(TestFuture, self).setUp()
            self.thread_pool = concurrent.futures.ThreadPoolExecutor(1)

        def test_chain(self):
            async_future = Future()
            conc_future = self.thread_pool.submit(
                long_running_callback, self.thread_pool, test_callback
            )


# Generated at 2022-06-14 11:55:10.827195
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.platform.asyncio import AsyncIOLoop
    from tornado.testing import AsyncTestCase, gen_test

    class MyTestCase(AsyncTestCase):
        def setUp(self):
            super().setUp()
            self.io_loop = AsyncIOLoop()
            self.io_loop.make_current()

        def tearDown(self):
            self.io_loop.clear_current()
            super().tearDown()

        @gen_test
        def test_future_set_exception_unless_cancelled(self):
            future = Future()
            self.io_loop.call_later(1, future.cancel)
            # When cancelled, future.set_exception would throw
            # asyncio.InvalidStateError

# Generated at 2022-06-14 11:55:14.921204
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    fut = Future()
    future_set_result_unless_cancelled(fut, 42)
    assert fut.result() == 42
    fut.cancel()
    future_set_result_unless_cancelled(fut, 43)
    assert fut.result() == 42
test_future_set_result_unless_cancelled()

# Generated at 2022-06-14 11:55:21.864302
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.testing import AsyncTestCase

    class TestFuture(Future):
        def __init__(self) -> None:
            super().__init__()
            self.set_exception(RuntimeError("foo"))

    class TestCase(AsyncTestCase):
        def test_future(self):
            f = TestFuture()
            future_set_exception_unless_cancelled(f, RuntimeError("bar"))
            self.assertEqual(f.exception().args[0], "foo")

# Generated at 2022-06-14 11:55:24.680631
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    f2.result()

# Generated at 2022-06-14 11:55:51.648437
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)

    future1.set_result(42)
    assert future2.result() == 42

    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)

    future1.set_exception(RuntimeError("foo"))
    try:
        future2.result()
        assert False, "should have raised exception"
    except RuntimeError as e:
        assert str(e) == "foo"

    future1 = Future()
    future2 = Future()
    future3 = Future()
    chain_future(future1, future2)
    chain_future(future2, future3)

    future1.set_exception(RuntimeError("foo"))

# Generated at 2022-06-14 11:56:04.910500
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()
    a.set_result(42)
    assert b.result() == 42
    c = Future()
    chain_future(b, c)
    assert c.result() == 42
    d = Future()
    e = Future()
    chain_future(d, e)
    assert not e.done()
    d.set_exception(ZeroDivisionError())
    assert e.exception() is not None
    f = Future()
    g = Future()
    chain_future(f, g)
    f.cancel()
    assert g.cancelled()
    assert f.cancelled()
    assert not f.done() and not g.done()
    f = Future()

# Generated at 2022-06-14 11:56:17.485767
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.ioloop import IOLoop

    executor = futures.ThreadPoolExecutor(2)
    ioloop = IOLoop()

    class Foo(object):
        executor = executor

        @run_on_executor
        def f(self, x, y):
            return x + y

        @run_on_executor(executor='executor')
        def g(self, x, y):
            return x + y

    f = Foo()
    fs = [f.g(1, 2), f.g(10, 20), f.f(100, 200)]
    assert not all(f.done() for f in fs)

    def check_fs():
        assert all(f.done() for f in fs)
        ioloop.stop()


# Generated at 2022-06-14 11:56:22.763720
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42



# Generated at 2022-06-14 11:56:36.235382
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    done_callback_calls = 0
    error_callback_calls = 0
    result_callback_calls = 0

    def done_callback(future):
        # type: (Any) -> None
        assert future is a
        assert future.done()
        assert future.result() == 42
        global done_callback_calls
        done_callback_calls += 1

    def error_callback(future):
        # type: (Any) -> None
        assert future is a
        assert future.done()
        assert future.exception() is not None
        global error_callback_calls
        error_callback_calls += 1

    def result_callback(future):
        # type: (Any) -> None
        assert future is a
        assert future.done()

# Generated at 2022-06-14 11:56:37.953874
# Unit test for function chain_future
def test_chain_future():
    f = Future()  # type: Future
    future_add_done_callback(f, lambda future: None)

# Generated at 2022-06-14 11:56:46.134632
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, None)
    assert future.exception() is None
    assert future.result() is None



# Generated at 2022-06-14 11:56:51.372091
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, ValueError())
    assert future.exception() is not None

    # Cancelled future
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError())

# Generated at 2022-06-14 11:56:58.677145
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.testing import AsyncTestCase

    class TestFuture(AsyncTestCase):
        def test_set_exception(self):
            async def set_future_exception():
                future = Future()
                future_set_exception_unless_cancelled(future, ValueError())
                try:
                    await future
                except ValueError:
                    pass
                else:
                    raise AssertionError("The future should be set exception")

            self.loop.run_until_complete(set_future_exception())

    test_future = TestFuture()
    test_future.test_set_exception()


# Generated at 2022-06-14 11:57:12.249585
# Unit test for function chain_future
def test_chain_future():
    async def async_chain_future():
        old_future = Future() # type: Future[int]
        new_future = Future() # type: Future[int]

        chain_future(old_future, new_future)

        old_future.set_result(1)

        assert 1 == await new_future

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_chain_future())
    loop.close()

# Generated at 2022-06-14 11:57:45.392902
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    # type: () -> None
    future = Future()  # type: Future[int]
    future_set_result_unless_cancelled(future, 42)
    assert future.result() == 42

    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 42)
    assert future.cancelled()

# Generated at 2022-06-14 11:57:56.474354
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest

    from concurrent.futures import _base

    import concurrent.futures
    import functools
    import tornado.ioloop
    import tornado.testing
    import tornado.platform.asyncio

    if hasattr(concurrent.futures, "_base"):
        # Python 3.7+
        Executor = _base.Executor
    else:
        # Python 3.6-
        Executor = concurrent.futures.Executor
    ThreadPoolExecutor = functools.partial(concurrent.futures.ThreadPoolExecutor, 5)

    class CustomExecutor(Executor):
        def submit(self, fn, *args, **kwargs):
            future = futures.Future()

# Generated at 2022-06-14 11:58:06.458702
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase

    class TestChainFuture(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            async_future = Future()
            conc_future = Future()

            chain_future(async_future, conc_future)
            self.assertFalse(conc_future.done())

            async_future.set_result(None)
            self.assertTrue(conc_future.done())
            self.assertFalse(conc_future.exception())

            async_future = Future()
            conc_future = Future()
            chain_future(async_future, conc_future)

            async_future.set_exception(Exception("test exception"))
            self.assertTrue(conc_future.done())

# Generated at 2022-06-14 11:58:18.432896
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from io import StringIO
    import logging
    from tornado.platform.asyncio import BaseAsyncIOLoop
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.platform.asyncio import AsyncIOLoop
    from tornado.log import LogFormatter

    # Capture the logs and make sure it was logged.
    stream = StringIO()
    log = logging.getLogger()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(LogFormatter())
    log.addHandler(handler)

    # Prepare asyncio support if available
    if BaseAsyncIOLoop.configured_class() is None:
        BaseAsyncIOLoop.configure(AsyncIOMainLoop)
    old_loop = AsyncIOLoop.current()
    loop = AsyncIOLoop()


# Generated at 2022-06-14 11:58:29.189645
# Unit test for function chain_future
def test_chain_future():
    import unittest.mock
    import asyncio

    def get_result(f, timeout=None):
        if timeout is not None:
            f = asyncio.wait_for(f, timeout)
        return asyncio.get_event_loop().run_until_complete(f)

    def get_exc_info(f, timeout=None):
        if timeout is not None:
            f = asyncio.wait_for(f, timeout)
        try:
            return None, None, None
        except Exception:
            return sys.exc_info()

    def assert_result(a, b, value):
        chain_future(a, b)
        assert get_result(a) == value
        assert get_result(b) == value


# Generated at 2022-06-14 11:58:38.123126
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.ioloop import IOLoop
    loop = IOLoop()

    class TestException(Exception):
        pass

    exc = TestException()

    def test_function(future):
        future_set_exception_unless_cancelled(future, exc)
        assert future.exception() == exc

        # reset the exc, otherwise test_future_set_exception_unless_cancelled
        # will fail
        del exc

    f = Future()
    f.add_done_callback(test_function)
    loop.add_future(f, lambda x: loop.stop())
    f.cancel()
    loop.start()

# Generated at 2022-06-14 11:58:49.832041
# Unit test for function chain_future
def test_chain_future():
    from concurrent import futures

    # add_done_callback is new in python 3.4
    if sys.version_info >= (3, 4):
        # Test that chaining a concurrent.futures.Future to an asyncio.Future works.
        a = futures.Future()
        b = Future()
        chain_future(a, b)
        assert not b.done()
        a.set_result(42)
        assert b.result() == 42

        a = Future()
        b = futures.Future()
        chain_future(a, b)
        assert not b.done()
        a.set_result(42)
        assert b.result() == 42

# Generated at 2022-06-14 11:58:54.455157
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class TestChainFuture(AsyncTestCase):
        def test_chain_future(self):
            fut1 = Future()
            fut2 = Future()
            chain_future(fut1, fut2)
            fut1.set_result(42)
            self.assertIs(fut2.result(), 42)

    test = TestChainFuture()
    test.run_until_complete(gen_test(test.test_chain_future))

# Generated at 2022-06-14 11:59:02.286718
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    future_set_result_unless_cancelled(f, 1)
    assert f.result() == 1

    f = Future()
    f.cancel()
    future_set_result_unless_cancelled(f, 1)
    assert f.cancelled()



# Generated at 2022-06-14 11:59:13.111206
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    # test with concurrent.futures.Future
    loop = asyncio.get_event_loop()
    f1 = futures.Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(5)
    assert f2.result() == 5
    f1 = futures.Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ValueError())
    e = f2.exception()
    assert isinstance(e, ValueError)
    f1 = Future()
    f2 = futures.Future()
    chain_future(f1, f2)
    f1.set_result(5)
    assert f2.result() == 5
    f1 = Future()