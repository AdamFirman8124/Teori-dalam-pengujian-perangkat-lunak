

# Generated at 2022-06-14 11:50:21.116449
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    try:
        import unittest2 as unittest  # type: ignore
    except ImportError:
        import unittest

    class ChainFutureTest(unittest.TestCase):
        def setUp(self):
            # type: () -> None
            self.f1 = Future()
            self.f2 = Future()

        def test_f1_finish_fail(self):
            # type: () -> None
            self.f1.set_exception(Exception("fail"))
            chain_future(self.f1, self.f2)
            self.assertTrue(self.f2.exception())

        def test_f1_finish_ok(self):
            # type: () -> None
            self.f1.set_result(1)

# Generated at 2022-06-14 11:50:30.927029
# Unit test for function chain_future
def test_chain_future():
    result = None

    def f(arg):
        return arg

    def on_done(future):
        nonlocal result
        result = future.result()

    def on_done_exc(future):
        nonlocal result
        result = future.exception()

    a = Future()
    chain_future(a, a) # type: ignore

    for arg in ["1", Exception()]:
        result = None
        a.set_result(arg)
        assert result is arg

        result = None
        a.set_exception(arg)
        assert result is arg

    b = Future()
    chain_future(a, b)
    a.set_result("2")
    assert result is None
    assert b.result() == "2"

    chain_future(a, b)

# Generated at 2022-06-14 11:50:34.365171
# Unit test for function chain_future
def test_chain_future():  # pragma: no cover
    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()

    a.set_result(42)
    assert b.done()
    assert b.result() == 42



# Generated at 2022-06-14 11:50:40.337106
# Unit test for function chain_future
def test_chain_future():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Generated at 2022-06-14 11:50:44.746478
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    assert not f.done()
    future_set_result_unless_cancelled(f, None)
    assert f.done()

    g = Future()
    g.cancel()
    future_set_result_unless_cancelled(g, None)
    assert g.done()



# Generated at 2022-06-14 11:50:48.275349
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    test_future = Future()
    test_future.set_result(3)
    assert test_future.result() == 3



# Generated at 2022-06-14 11:50:56.051420
# Unit test for function run_on_executor
def test_run_on_executor():
    class Dummy(object):
        def __init__(self):
            self.executor = DummyExecutor()

        @run_on_executor
        def foo(self, arg):
            return arg + 1

    d = Dummy()
    f = d.foo(21)
    assert isinstance(f, Future)
    assert f.result() == 22

# Generated at 2022-06-14 11:51:05.493039
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    class UnitTestFuture(Future):
        def __init__(self):
            super().__init__()
            self._cancelled = False

        def cancel(self) -> bool:
            self._cancelled = True
            return True

        def cancelled(self) -> bool:
            return self._cancelled

    f = UnitTestFuture()
    future_set_result_unless_cancelled(f, None)
    assert f.done() and f.result() is None

    f = UnitTestFuture()
    f.cancel()
    future_set_result_unless_cancelled(f, None)
    assert f.cancelled() and f.result() is None

    try:
        raise ValueError()
    except ValueError:
        exc_info = sys.exc_info()

    f = UnitTestFuture

# Generated at 2022-06-14 11:51:11.398986
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    val = DummyExecutor().submit(lambda a, b: a + b, 1, 5)
    assert val.result(4) == 6
    try:
        val = DummyExecutor().submit(lambda: 1 / 0)
        val.result(4)  # It will raise ZeroDivisionError
        assert False
    except ZeroDivisionError:
        pass

# Generated at 2022-06-14 11:51:19.619605
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import tornado
    import tornado.testing
    import tornado.platform.asyncio

    @tornado.platform.asyncio.to_tornado_future
    async def async_foo():
        await asyncio.sleep(0.01)
        return 42

    def foo():
        return 24

    class ChainFutureTest(unittest.TestCase):
        def setUp(self):
            self.io_loop = tornado.testing.AsyncIOMock()
            self.io_loop.make_current()
            self.executor = futures.ThreadPoolExecutor(1)

        @tornado.testing.gen_test
        async def test_chain(self):
            a = async_foo()
            b = Future()
            chain_future(a, b)

# Generated at 2022-06-14 11:54:13.235441
# Unit test for function chain_future
def test_chain_future():
    # chain_future has been tested in the past via unittest.mock;
    # here we just test for typing errors.
    def callback(fut: "futures.Future[_T]") -> None:
        fut.result()

    chain_future(Future(), Future())
    chain_future(Future(), futures.Future())
    chain_future(futures.Future(), Future())
    chain_future(futures.Future(), futures.Future())
    future_add_done_callback(Future(), callback)
    future_add_done_callback(futures.Future(), callback)

# Generated at 2022-06-14 11:54:26.012456
# Unit test for function run_on_executor
def test_run_on_executor():
    @typing.overload
    def no_args(self: "Foo") -> None:
        ...

    @typing.overload  # noqa: F811
    def no_args(self: "Foo") -> Future:
        ...

    @typing.overload  # noqa: F811
    def no_args(self: "Foo", executor: str) -> Callable:
        ...

    @typing.overload  # noqa: F811
    def no_args(self: "Foo", *args: Any) -> None:
        ...

    @typing.overload  # noqa: F811
    def no_args(self: "Foo", *args: Any) -> Future:
        ...


# Generated at 2022-06-14 11:54:39.188157
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase, ExpectLog

    class Test(AsyncTestCase):
        def test_no_result(self):

            @gen_test
            async def test_future():
                source = Future()
                dest = Future()
                chain_future(source, dest)
                source.set_result(None)
                await dest

        def test_with_result(self):

            @gen_test
            async def test_future():
                source = Future()
                dest = Future()
                chain_future(source, dest)
                source.set_result(42)
                self.assertEqual(await dest, 42)

        def test_error(self):

            @gen_test
            async def test_future():
                source = Future()
                dest = Future()

# Generated at 2022-06-14 11:54:50.916596
# Unit test for function chain_future
def test_chain_future():
    def assert_future_state(expected_state, f):
        assert expected_state == f.done(), "expected %s but got %s" % (expected_state, f.done())
        if not expected_state:
            f.cancel()

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert_future_state(False, f1)
    assert_future_state(False, f2)
    f2.cancel()
    assert_future_state(False, f1)
    assert_future_state(True, f2)
    f1.set_result(None)
    assert_future_state(True, f1)
    assert_future_state(True, f2)
    f1 = Future()
    f2 = Future()
    chain

# Generated at 2022-06-14 11:55:00.817077
# Unit test for function chain_future
def test_chain_future():
    from tornado import testing
    from concurrent import futures

    executor = futures.ThreadPoolExecutor(2)
    io_loop = testing.IOLoop()


# Generated at 2022-06-14 11:55:10.003275
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.cancel()
    try:
        future_set_exception_unless_cancelled(future, ValueError("test"))
    except Exception:
        raise AssertionError("ValueError should not be raised.")

    future = Future()
    try:
        future_set_exception_unless_cancelled(future, ValueError("test"))
        raise AssertionError("ValueError should be raised.")
    except ValueError:
        pass

# Generated at 2022-06-14 11:55:18.802893
# Unit test for function chain_future
def test_chain_future():
    def future1_result():
        return 10

    def future2_result(arg):
        return arg + 10

    def future3_result(arg):
        return arg + 20

    def future4_result(arg):
        return arg + 30

    f1 = Future()
    f2 = Future()
    f3 = Future()
    f4 = Future()

    chain_future(f1, f2)
    chain_future(f2, f3)
    chain_future(f3, f4)

    f1.set_result(future1_result())
    f2.set_result(future2_result(f2.result()))
    f3.set_result(future3_result(f3.result()))
    f4.set_result(future4_result(f4.result()))

   

# Generated at 2022-06-14 11:55:29.480841
# Unit test for function chain_future
def test_chain_future():
    io_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(io_loop)

    a = Future()
    b = Future()

    chain_future(a, b)

    assert not a.done()
    assert not b.done()

    a.set_result(True)
    assert a.done()
    assert b.done()

    a = Future()
    b = Future()
    chain_future(a, b)

    assert not a.done()
    assert not b.done()

    a.set_exception(ValueError)
    assert a.done()
    assert b.done()

    # Now test that chain_future can be used with concurrent.futures.Future.
    # See also https://github.com/tornadoweb/tornado/issues/2158


# Generated at 2022-06-14 11:55:37.445992
# Unit test for function chain_future
def test_chain_future():
    @typing.no_type_check
    def f(x: int) -> int:
        return x + 1

    @typing.no_type_check
    def g(x: int) -> int:
        return x * 2

    a = Future()
    b = Future()
    c = Future()
    chain_future(a, b)
    chain_future(b, c)
    a.set_result(42)
    assert b.result() == 42
    assert c.result() == 42
    a = Future()
    b = Future()
    c = Future()
    a.set_result(42)
    chain_future(a, b)
    chain_future(b, c)
    assert b.result() == 42
    assert c.result() == 42
    a = Future()

# Generated at 2022-06-14 11:55:48.704812
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import get_unused_port, AsyncTestCase

    class TestChainFuture(AsyncTestCase):
        @property
        def thread_executor(self):
            from concurrent.futures import ThreadPoolExecutor
            return ThreadPoolExecutor(max_workers=1)

        def test_chain(self):
            future = Future()

            def thread_callback():
                future.set_result(3)

            self.thread_executor.submit(thread_callback)
            chained = Future()
            chain_future(future, chained)
            chained.add_done_callback(self.stop)
            self.wait()
            self.assertEqual(chained.result(), 3)


# Generated at 2022-06-14 11:58:55.417085
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception("a"))
    assert future.exception() is not None

    future = Future()
    future_set_result_unless_cancelled(future, None)
    future_set_exception_unless_cancelled(future, Exception("a"))
    assert future.exception() is None

    future = Future()
    future_set_result_unless_cancelled(future, None)
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception("a"))
    assert future.cancelled()

# Generated at 2022-06-14 11:59:06.016971
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()

    chain_future(f1, f2)
    test_result = []

    def cb(future):
        test_result.append(future.result())

    f2.add_done_callback(cb)

    assert not f1.done()
    assert not f2.done()

    f1.set_result(42)

    assert f1.done()
    assert f2.done()
    assert test_result == [42]

# Generated at 2022-06-14 11:59:14.467873
# Unit test for function chain_future
def test_chain_future():
    def f(x: int, delay: float) -> int:
        import time

        time.sleep(delay)
        return x * x

    import time
    import unittest

    from tornado.ioloop import IOLoop

    IOLoop.clear_instance()

    def future_chain_test(x: int, delay: float) -> str:
        a = asyncio.ensure_future(asyncio.sleep(delay))
        b = Future()
        chain_future(a, b)
        b.add_done_callback(lambda future: future.result())
        b.set_result(x * x)
        return b.result()

    class FutureChainTest(unittest.TestCase):
        def tearDown(self):
            IOLoop.clear_instance()


# Generated at 2022-06-14 11:59:20.034537
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    try:
        raise Exception('foo')
    except Exception:
        future_set_exception_unless_cancelled(f, sys.exc_info())
    assert f.exception() is not None
    f.cancel()
    future_set_exception_unless_cancelled(f, sys.exc_info())

# Generated at 2022-06-14 11:59:30.403982
# Unit test for function chain_future
def test_chain_future():
    import concurrent.futures
    import tornado.gen

    # Futures used with tornado.concurrent.run_on_executor.
    def get_future() -> Future:
        future = Future()
        future_set_result_unless_cancelled(future, 1)
        return future

    async def get_future_awaitable() -> Future:
        future = Future()
        future_set_result_unless_cancelled(future, 2)
        return future

    async def test_chain_async_future_asyncio_future() -> Future:
        f1 = get_future()
        f2 = Future()
        chain_future(f1, f2)
        assert f1.result() == 1
        return f2


# Generated at 2022-06-14 11:59:40.877606
# Unit test for function chain_future
def test_chain_future():
    import tornado.ioloop

    # This unit test creates a Future that does not produce a result, because
    # it immediately chains to another Future. Since 3.2, Future's set_result
    # method has an assertion that the Future must not already have a result.
    # This test avoids triggering that assertion by setting the chained-to
    # Future's result before adding the callback. Unfortunately there's no
    # corresponding way to avoid the assertion on set_exception in this
    # test framework.

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.result()
    f2.set_result(42)



# Generated at 2022-06-14 11:59:44.837649
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 42)
    assert future.result() == 42
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 42)
    assert future.cancelled()

# Generated at 2022-06-14 11:59:57.350667
# Unit test for function chain_future
def test_chain_future():
    def fib(n: int) -> int:
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)

    @run_on_executor
    def fib_async(n: int) -> int:
        return fib(n)

    class Foo:
        executor = dummy_executor

        def async_fib(self, n: int) -> Future:
            f = Future()
            if n <= 1:
                f.set_result(n)
            else:
                chain_future(fib_async(n - 1), f)

                def add_second(f: Future) -> None:
                    chain_future(fib_async(n - 2), f)

                future_add_done_callback(f, add_second)
           

# Generated at 2022-06-14 12:00:09.835761
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop()
    io_loop.make_current()

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    io_loop.add_future(f1, lambda f: f2.set_result(f.result() + 1))
    io_loop.add_future(f2, lambda f: io_loop.stop())
    f1.set_result(1)
    io_loop.start()
    assert f2.result() == 2

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    io_loop.add_future(f1, lambda f: f2.set_exception(Exception('test')))