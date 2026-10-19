

# Generated at 2022-06-14 11:50:13.652122
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    loop = IOLoop.current()
    f = Future()
    f2 = Future()
    chain_future(f, f2)
    assert not f2.done()
    assert f2.result() is None

    loop.run_sync(lambda: f.set_result(42))
    assert f2.result() == 42
    chain_future(f, f2)
    assert f2.result() == 42

    loop.run_sync(lambda: f.set_exception(Exception("foo")))
    assert f2.exception() is None
    chain_future(f, f2)
    assert f2.result() == 42

    f = Future()
    f2 = Future()
    chain_future(f, f2)

# Generated at 2022-06-14 11:50:21.796998
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    import random
    import math
    dummy_executor = DummyExecutor()
    future = dummy_executor.submit(pow, 4, 2)
    assert future.result() == 4 ** 2

    def func(*args: Any) -> float:
        return sum(args) / (len(args) + 1)

    for i in range(10):
        future = dummy_executor.submit(func, *[v for v in range(random.randrange(1, 10))])
        assert future.result() == sum([v for v in range(random.randrange(1, 10))]) / (
            random.randrange(1, 10) + 1
        )

    def func2(a: float, b: float, c: float) -> float:
        return pow(a, b) + c


# Generated at 2022-06-14 11:50:31.179747
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # The code below is a slightly modified version of the test cases
    # in the asyncio.Future implementation.

    def test_exception(future, exception):
        future_set_exc_info(future, (type(exception), exception, None))
        return future

    def test_exception_cancel(future, exception):
        future.cancel()
        future_set_exc_info(future, (type(exception), exception, None))
        return future

    def test_exception_cancel_result(future, exception):
        future.cancel()
        future.set_result(None)
        future_set_exception_unless_cancelled(future, exception)
        return future


# Generated at 2022-06-14 11:50:38.823408
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()  # type: Future[Any]
    f2 = Future()  # type: Future[Any]

    chain_future(f1, f2)

    f1.set_result(42)
    assert f1.result() == 42
    assert f2.result() == 42

    f1 = Future()  # type: Future[Any]
    f2 = Future()  # type: Future[Any]


    def f(future):
        # type: (Future[Any]) -> None
        future.set_exception(ValueError())


    chain_future(f1, f2)
    tornado.ioloop.IOLoop.current().add_callback(f, f1)
    try:
        f2.result()
    except ValueError:
        pass
   

# Generated at 2022-06-14 11:50:47.272470
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest.mock as mock
    from tornado.ioloop import IOLoop

    class Example(object):
        executor = "executor"

        def __init__(self):
            self._executor = mock.MagicMock()

        @run_on_executor()
        def foo(self, a, b):
            return a + b

    def test_executor(a, b):
        return a + b

    example = Example()
    example.foo(1, 2)
    example._executor.submit.assert_called_once_with(test_executor, 1, 2)

    example._executor.submit.reset_mock()

    with mock.patch.object(IOLoop.current(), "add_future") as add_future:
        example = Example()

# Generated at 2022-06-14 11:51:00.788934
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado import gen
    from tornado.testing import AsyncTestCase
    from concurrent.futures import ThreadPoolExecutor

    class TestCase(AsyncTestCase):
        def setUp(self):
            super().setUp()
            self.executor = ThreadPoolExecutor(1)

        @run_on_executor
        def func(self, a: int, b: int) -> int:
            # type: (...) -> int
            return a + b

        @run_on_executor(executor="my_executor")
        def func_with_arg(self, a: int, b: int) -> int:
            # type: (...) -> int
            return a + b

        @gen.coroutine
        def test_run_on_executor(self):
            result = yield self.func(1, 2)

# Generated at 2022-06-14 11:51:13.212541
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class ChainFutureTest(AsyncTestCase):
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super(ChainFutureTest, self).__init__(*args, **kwargs)
            self.future1 = None  # type: Any
            self.future2 = None  # type: Any
            self.value = None  # type: Any
            self.exception = None  # type: Any

        @gen_test
        def test_chain_future_cancellation(self) -> None:
            def set_exception(future: "Future[_T]") -> None:
                future.set_exception(ValueError())

            self.future1 = Future()
            self.future2 = Future()

# Generated at 2022-06-14 11:51:16.393476
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    assert not future2.done()
    future1.set_result(42)
    assert future2.done()
    assert future2.result() == 42

# Generated at 2022-06-14 11:51:19.134711
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, ValueError())
    assert not future.done()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError())
    assert future.done()

# Generated at 2022-06-14 11:51:25.115838
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    @asyncio.coroutine
    def main():
        fut = asyncio.Future()
        fut.cancel()
        future_set_exception_unless_cancelled(fut, ValueError())

    asyncio.get_event_loop().run_until_complete(main())

# Generated at 2022-06-14 11:51:36.655906
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from concurrent.futures import Future as FutureF
    from asyncio import Future as FutureA
    from tornado.testing import gen_test, AsyncTestCase, bind_unused_port

    class TestCase(AsyncTestCase):
        @gen_test
        def test(self):
            # type: () -> None
            # All four combinations of FutureA/FutureF for first/second future
            for fcls in (FutureA, FutureF):
                for scls in (FutureA, FutureF):
                    fut1 = fcls()
                    fut2 = scls()
                    chain_future(fut1, fut2)
                    fut1.set_result(None)
                    yield fut2

    TestCase().test()

# Generated at 2022-06-14 11:51:42.357468
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.ioloop import IOLoop

    io_loop = IOLoop()
    io_loop.make_current()

    class Object:
        executor = dummy_executor

        @run_on_executor
        def function(self, arg):
            return arg + 1

    obj = Object()
    future = obj.function(10)
    assert future.result() == 11

# Generated at 2022-06-14 11:51:51.745849
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest.mock
    from tornado import gen

    class Foo(object):
        executor = dummy_executor

        @run_on_executor
        def func(self, arg1, kwarg1=None, kwarg2=5):
            return (self, arg1, kwarg1, kwarg2)

    f = Foo()
    f.func = unittest.mock.Mock(wraps=f.func)

    res = gen.convert_yielded(f.func(1, kwarg2=10))
    assert isinstance(res, Future)
    assert f.func.called

# Generated at 2022-06-14 11:52:03.140035
# Unit test for function chain_future
def test_chain_future():
    from tornado.iostream import StreamClosedError

    # Ensure chain_future chaining works when the chainee is already
    # completed.
    first = Future()
    second = Future()
    chain_future(first, second)
    first.set_result(4)
    assert second.result() == 4

    for chainee_future in (Future(), futures.Future()):
        # Ensure chain_future chaining works with chainee not yet
        # completed.
        first = Future()
        second = Future()
        chain_future(first, second)
        first.set_result(5)
        assert second.result() == 5

        # Ensure chain_future's chaining propagates exceptions.
        first = Future()
        second = Future()
        chain_future(first, second)
        exc = RuntimeError("some exception")
       

# Generated at 2022-06-14 11:52:14.750186
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
    assert isinstance(f2.exception(), ZeroDivisionError)
    f1 = Future()
    f2 = Future()
    f2.cancel()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.cancelled()

# Generated at 2022-06-14 11:52:22.787119
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest.mock as mock

    io_loop = mock.Mock()
    # This is a mock of functions defined by the decorator
    fn = mock.Mock()
    executor = mock.Mock()
    self = mock.Mock(
        fn=fn,
        executor=executor,
        io_loop=io_loop,
        _thread_pool=executor,
    )
    args = mock.Mock()
    kwargs = mock.Mock()

    # Test that the decorator returned by run_on_executor returns
    # a new function
    wrapper = run_on_executor(fn)
    assert wrapper.__name__ == fn.__name__
    assert wrapper.__doc__ == fn.__doc__

    # Test the resulting wrapper

# Generated at 2022-06-14 11:52:35.375603
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    assert not future.done()
    future_set_exception_unless_cancelled(future, RuntimeError("foo"))
    assert future.done()
    exc = future.exception()
    assert isinstance(exc, RuntimeError)
    assert exc.args == ("foo",)
    future = Future()
    future.cancel()
    assert future.done()
    future_set_exception_unless_cancelled(future, RuntimeError("foo"))
    assert future.done()
    future = Future()
    assert not future.done()
    exception = RuntimeError("foo")
    future.set_exception(exception)
    assert future.done()
    future_set_exception_unless_cancelled(future, RuntimeError("bar"))
    assert future.done()

# Generated at 2022-06-14 11:52:48.653399
# Unit test for function chain_future
def test_chain_future():
    import unittest.mock
    from tornado.ioloop import IOLoop

    io_loop = IOLoop()
    io_loop.make_current()

    # The following tests are not ideal because they are not testing
    # the futures implementation, but are at least better than nothing.

    # Test chaining with concurrent.futures.Future
    def callback(arg: int) -> None:
        pass

    f1 = futures.Future()  # type: futures.Future[int]
    f2 = Future()  # type: Future[int]
    chain_future(f1, f2)
    future_add_done_callback(f2, callback)
    f1.set_result(1)

# Generated at 2022-06-14 11:52:58.693833
# Unit test for function chain_future
def test_chain_future():
    import time
    from tornado.ioloop import IOLoop

    def f1(callback):
        time.sleep(0.01)
        callback(42)

    def f2(callback):
        time.sleep(0.01)
        callback(43)

    async def async_f1():
        await asyncio.sleep(0.01)
        return 42

    async def async_f2():
        await asyncio.sleep(0.01)
        return 43

    def callback(future):
        IOLoop.current().stop()
        assert future.result() == 42


    executor = futures.ThreadPoolExecutor(2)
    a = Future()
    b = futures.Future()
    chain_future(a, b)
    executor.submit(f1, a.set_result)
    executor.submit

# Generated at 2022-06-14 11:52:59.369057
# Unit test for function chain_future
def test_chain_future():
    pass



# Generated at 2022-06-14 11:53:11.004725
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.testing import AsyncTestCase, gen_test

    class Test(AsyncTestCase):
        @gen_test
        def test_chain(self):
            # type: () -> None
            future1 = Future()  # type: Future
            future2 = Future()  # type: Future
            chain_future(future1, future2)
            self.assertFalse(future1.done())
            self.assertFalse(future2.done())
            future1.set_result(42)
            self.assertEqual(future2.result(), 42)

# Generated at 2022-06-14 11:53:22.231208
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    # Testing this is a bit tricky because we don't want to
    # actually block.  So we spawn two threads and make them talk
    # to each other.  We could use a Queue instead of a pipe, but
    # this is probably close enough.
    import threading

    a, b = futures.Future(), futures.Future()

    def b_done():
        # type: () -> None
        assert a.done()
        assert b.done()
        # b always copies the result of a, even if the result of
        # a is an exception (even a cancellation).
        try:
            b.result()
        except futures.CancelledError:
            assert a.cancelled()
            assert b.cancelled()
            # b is guaranteed to be cancelled after a, but not necessarily
            #

# Generated at 2022-06-14 11:53:34.892980
# Unit test for function chain_future
def test_chain_future():
    import unittest

    from tornado import gen
    from tornado.ioloop import IOLoop

    class FutureChainTest(unittest.TestCase):
        def setUp(self):
            # type: () -> None
            self.io_loop = IOLoop()
            self.io_loop.make_current()
            self.executor = futures.ThreadPoolExecutor(1)

        def test_chain_callback(self):
            # type: () -> None
            @gen.coroutine
            def f():
                # type: () -> int
                raise gen.Return(42)

            a = Future()
            chain_future(f(), a)
            self.assertEqual(self.io_loop.run_sync(a.result), 42)

            # Tests that the ``copy`` function passed to
            # ``Future.add

# Generated at 2022-06-14 11:53:39.216891
# Unit test for function chain_future
def test_chain_future():
    from tornado import gen

    async def f():
        f = gen.Future()
        chain_future(gen.Task(f), gen.Task(f))
        raise gen.Return(f)

    f = gen.Task(f())
    f.set_result(42)
    assert f.result() == 42

# Generated at 2022-06-14 11:53:50.482078
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    @gen_test
    async def test():
        main_future = Future()
        secondary_future = Future()
        chain_future(secondary_future, main_future)
        secondary_future.set_result(42)
        assert main_future.result() == 42

    loop.run_until_complete(test())


# These classes are indirectly compared against by `isinstance()`
# Sometimes, `AssertionError` is used instead of `Exception`
# so allow that in the future if needed.

# Generated at 2022-06-14 11:54:00.548346
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    dummy_executor.submit(lambda: 1).result()


if __name__ == "__main__":
    import unittest
    from tornado.testing import AsyncTestCase, gen_test

    class FutureTest(AsyncTestCase):
        def test_chain_future(self):
            f = Future()
            f2 = Future()
            chain_future(f, f2)
            self.assertFalse(f2.done())
            f.set_result(42)
            self.assertEqual(f2.result(), 42)

            f = Future()
            f2 = Future()
            chain_future(f, f2)
            self.assertFalse(f2.done())
            f.set_exception(RuntimeError())
            with self.assertRaises(RuntimeError):
                f2.result()

            f

# Generated at 2022-06-14 11:54:08.187835
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    assert future.cancelled() is False
    future_set_result_unless_cancelled(future, 100)
    assert future.result() == 100
    future.cancel()
    assert future.cancelled() is True
    future_set_result_unless_cancelled(future, None)
    assert future.cancelled() is True
    with pytest.raises(InvalidStateError):
        future.result()



# Generated at 2022-06-14 11:54:15.198515
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class TestChainFuture(AsyncTestCase):
        pass

    for name, test_case in (
        ("asyncio Future", Future()),
        ("concurrent.futures.Future", futures.Future()),
    ):
        # test_case is a Future instance
        assert is_future(test_case)

        @gen_test
        def test_success(self):
            f1 = test_case
            f2 = test_case
            chain_future(f1, f2)
            f1.set_result(42)
            assert (yield f2) == 42

        test_name = "%s.%s" % (name, "test_success")
        setattr(TestChainFuture, test_name, test_success)


# Generated at 2022-06-14 11:54:19.189111
# Unit test for function chain_future
def test_chain_future():

    future_a = Future()
    future_b = Future()
    chain_future(future_a, future_b)
    future_a.set_result(42)

    assert future_b.result() == 42



# Generated at 2022-06-14 11:54:28.792776
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test

    @gen_test
    async def test_future():
        from tornado.httpclient import AsyncHTTPClient

        async def async_func(n):
            await asyncio.sleep(0.01, result=n)
            return n

        executor = DummyExecutor()

        def func(n):
            return async_func(n)

        f1 = executor.submit(func, 1)
        # assert chained future is async future
        f2 = Future()
        chain_future(f1, f2)
        result = await f2
        assert result == 1

        # assert chained future is conc future
        f3 = executor.submit(func, 2)
        f4 = Future()
        chain_future(f3, f4)
        result = await f4
        assert result

# Generated at 2022-06-14 11:54:43.777457
# Unit test for function run_on_executor
def test_run_on_executor():
    from unittest.mock import Mock

    class Result(object):
        def __init__(self):
            self.value = None
            self.exc_info = None

    def done_callback(future):
        result.value = future.result()
        result.exc_info = future.exc_info()

    class TestCls(object):
        executor = dummy_executor

        @run_on_executor
        def func(self, value):
            return value

    result = Result()
    test_cls = TestCls()
    future = test_cls.func(1)
    future_add_done_callback(future, done_callback)
    assert result.value == 1
    assert result.exc_info is None
    future = test_cls.func(None)
    future_add_done

# Generated at 2022-06-14 11:54:47.928910
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.testing import AsyncTestCase, gen_test


# Generated at 2022-06-14 11:54:53.087899
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def fn_1():
        return True
    def fn_2():
        return False
    def fn_3():
        raise Exception
    def fn_4():
        return None
    def fn_5():
        return "a"
    def fn_6():
        return [1,2]
    def fn_7():
        return (1,2)
    def fn_8():
        return {'a':1}
    def fn_9(x,y):
        return x+y
    def fn_10(x,y):
        return x*y

    def executor_test(fn, test_case):
        f = dummy_executor.submit(fn)
        test_case.assertEqual(f.done(), True)
        test_case.assertEqual(f.result(), True)


# Generated at 2022-06-14 11:55:01.778027
# Unit test for function chain_future
def test_chain_future():
    result = []

    @chain_future
    def f1(callback):
        result.append(1)
        callback(None)
        result.append(6)

    @chain_future
    def f2(future, callback):
        result.append(7)
        callback(None)

    @chain_future
    def f3(future, callback):
        result.append(2)
        callback(None)

    @chain_future
    def f4(future, callback):
        result.append(3)
        callback(None)
        result.append(5)

    @chain_future
    def f5(callback):
        result.append(4)

    f1(f2(f3(f4(f5()))))
    assert result == [1, 2, 3, 5, 6, 7]



# Generated at 2022-06-14 11:55:03.246813
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, ValueError())

# Generated at 2022-06-14 11:55:09.240199
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    loop = IOLoop()
    loop.make_current()

    done_future = Future()
    chain_future(Future(), done_future)

    exception = RuntimeError()
    done_future.set_exception(exception)
    assert done_future.exception() == exception

# Generated at 2022-06-14 11:55:18.410492
# Unit test for function chain_future
def test_chain_future():
    from tornado import testing

    def f(x: int, y: int) -> int:
        return x + y

    def g(x: int) -> int:
        return x * 2

    def h(x: int, y: int) -> None:
        assert x == 12
        assert y == 34

    future1 = Future()
    future2 = Future()  # type: Future[int]
    future3 = Future()  # type: Future[int]
    chain_future(future1, future2)
    chain_future(future2, future3)
    future1.set_result(object())
    testing.gen_test(f)(12, y=34).add_done_callback(lambda f: future1.set_result(f))

# Generated at 2022-06-14 11:55:29.174699
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)

    future1.set_result(42)
    assert future2.exception() is None
    assert future2.result() == 42

    def callback(f):
        # type: (Future) -> None
        assert f.exception() is None
        assert f.result() == 42

    future2.add_done_callback(callback)

    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)

    exc_info = None
    try:
        1 / 0
    except ZeroDivisionError:
        # This captures the traceback that would have been lost if we had
        # used sys.exc_info() here.
        exc_info = sys

# Generated at 2022-06-14 11:55:32.775454
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future: Future[Any] = Future()
    future_set_exception_unless_cancelled(future, ValueError())
    assert not future.cancelled()
    assert future.exception()

# Generated at 2022-06-14 11:55:36.300710
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    executor = DummyExecutor()
    futureResult = executor.submit(lambda x: x+1, 5)
    assert futureResult == 6


# Generated at 2022-06-14 11:55:51.055187
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import unittest
    import asynctest  # type: ignore


    class TestChainFuture(asynctest.TestCase):
        def test_chain_future(self):
            # type: () -> None
            result = object()
            async_future = Future()
            conc_future = futures.Future()
            chain_future(conc_future, async_future)
            conc_future.set_result(result)
            self.assertEqual(async_future.result(), result)

        def test_chain_future_exception(self):
            # type: () -> None
            exception = Exception()
            async_future = Future()
            conc_future = futures.Future()
            chain_future(conc_future, async_future)
            conc_future.set_exception

# Generated at 2022-06-14 11:55:59.773633
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    import tornado
    future = tornado.concurrent.Future()
    future_set_result_unless_cancelled(future, "abc")
    assert future.result() == "abc"

    future = tornado.concurrent.Future()
    future_set_result_unless_cancelled(future, 123)
    assert future.result() == 123

    future = tornado.concurrent.Future()
    future_set_result_unless_cancelled(future, None)
    assert future.result() is None

# Generated at 2022-06-14 11:56:03.801181
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    assert future_set_result_unless_cancelled(future, 5) == None
    assert future.done()
    assert future.result() == 5

# Generated at 2022-06-14 11:56:16.839711
# Unit test for function chain_future
def test_chain_future():
    future2 = Future()
    future1 = Future()
    chain_future(future1, future2)

    future1.set_result(42)
    assert future2.result() == 42

    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)

    future1.set_exception(RuntimeError("foo"))
    try:
        future2.result()
    except RuntimeError as e:
        assert e.args[0] == "foo"
    else:
        raise AssertionError("did not get expected exception")

    # Verify that the next result is not affected by the first
    future2 = Future()
    future1 = Future()
    chain_future(future1, future2)

    future2.cancel()
    future1.set_result(42)

# Generated at 2022-06-14 11:56:27.081148
# Unit test for function chain_future
def test_chain_future():
    """
    .. versionchanged:: 4.1
       ``chain_future`` now accepts both `concurrent.futures.Future`
       and `.Future`.
    """
    # Test an asyncio.Future
    async_future = Future()
    future = futures.Future()
    chain_future(future, async_future)
    future.result()
    assert not async_future.done()
    future.set_result(42)
    assert async_future.result() == 42
    # Test a concurrent.futures.Future
    async_future = Future()
    future = futures.Future()
    chain_future(future, async_future)
    future.result()
    assert not async_future.done()
    future.set_result(42)
    assert async_future.result() == 42

# Generated at 2022-06-14 11:56:38.950283
# Unit test for function chain_future
def test_chain_future():
    import logging
    import time
    import unittest

    from tornado.ioloop import IOLoop, TimeoutError

    logging.getLogger().setLevel(logging.DEBUG)

    class ChainFutureTest(unittest.TestCase):
        def run_future(self, f):
            if not is_future(f):
                return
            for cb in self.ioloop.run_sync(lambda: future_add_done_callback(f, cb), timeout=1):
                cb(f)

        def setUp(self):
            self.ioloop = IOLoop()
            self.ioloop.make_current()

        def tearDown(self):
            self.ioloop.clear_current()
            self.ioloop.close()

        def test_chain_future(self):
            f1 = Future()

# Generated at 2022-06-14 11:56:48.584675
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    future_set_result_unless_cancelled(f, 5)
    assert f.result() == 5
    f = Future()
    f.cancel()
    future_set_result_unless_cancelled(f, 5)
    assert f.cancelled()


# Generated at 2022-06-14 11:56:53.166718
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception("foo"))
    assert future.exception()
    assert isinstance(future.exception(), Exception)
    assert str(future.exception()) == "foo"

    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception("bar"))
    assert future.cancelled()

# Generated at 2022-06-14 11:57:00.452821
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_result(42)
    assert future2.result() == 42

    future3 = Future()
    future4 = Future()
    chain_future(future3, future4)
    future3.set_exception(ZeroDivisionError())
    try:
        future4.result()
    except ZeroDivisionError:
        pass
    else:
        assert False, "did not propagate exception"

    future5 = Future()
    future6 = Future()
    future7 = Future()
    chain_future(future5, future6)
    chain_future(future6, future7)
    future5.set_result(42)
    assert future6.result() == 42

# Generated at 2022-06-14 11:57:05.874915
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = asyncio.Future()
    exc = Exception()
    future_set_exception_unless_cancelled(future, exc)
    assert future.exception() is exc
    future = asyncio.Future()
    future.cancel()
    with app_log.catch_logs(app_log.error) as logs:
        future_set_exception_unless_cancelled(future, exc)
    assert len(logs) == 1
    assert "Exception after Future was cancelled" in logs[0]["msg"]

# Generated at 2022-06-14 11:57:29.687090
# Unit test for function chain_future
def test_chain_future():
    async def coro_fn():
        return "result"

    fut_1 = Future()
    fut_2 = Future()

    chain_future(fut_1, fut_2)

    coro = coro_fn()
    coro.add_done_callback(lambda f: fut_1.set_result(f.result()))

    result = asyncio.run(fut_2)
    assert result == "result"



# Generated at 2022-06-14 11:57:37.905232
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.testing import AsyncTestCase, gen_test

    class TestCase(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            # type: () -> None
            future1 = Future()  # type: Future[str]
            future2 = Future()  # type: Future[str]
            chain_future(future1, future2)
            future1.set_result("foo")
            self.assertEqual("foo", (yield future2))

    TestCase().test_chain_future()

# Generated at 2022-06-14 11:57:43.764526
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()

    future_set_exception_unless_cancelled(f, ValueError())

    # Not testing logging here as it is not thread-safe.
    # See: https://github.com/tornadoweb/tornado/issues/2245#issuecomment-533898765

# Generated at 2022-06-14 11:57:48.363380
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f1.done()
    assert not f2.done()
    f1.set_result(42)
    assert f1.result() == f2.result()
    assert f1.done()
    assert f2.done()

    f1 = Future()
    f2 = Future()
    f2.set_result(None)
    chain_future(f1, f2)
    assert f1.done()
    assert f2.done()

    f1 = Future()
    f2 = Future()
    f2.cancel()
    chain_future(f1, f2)
    assert f1.done()
    assert f2.done()

# Generated at 2022-06-14 11:57:59.021955
# Unit test for function chain_future
def test_chain_future():
    import unittest
    from concurrent.futures import Future as ConcFuture

    class DummyExecutor(futures.Executor):
        def submit(
            self, fn: Callable[..., _T], *args: Any, **kwargs: Any
        ) -> "futures.Future[_T]":
            future = ConcFuture()  # type: futures.Future[_T]
            try:
                future_set_result_unless_cancelled(future, fn(*args, **kwargs))
            except Exception:
                future_set_exc_info(future, sys.exc_info())
            return future

        def shutdown(self, wait: bool = True) -> None:
            pass

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.io_loop = IOLoop

# Generated at 2022-06-14 11:58:07.610879
# Unit test for function chain_future
def test_chain_future():
    client = DummyExecutor()

    def server_job(x, y):
        return x + y

    def client_job(x, y):
        return x * y

    loop = asyncio.get_event_loop()

    @asyncio.coroutine
    def test():
        f1 = client.submit(client_job, 1, 2)
        f2 = client.submit(client_job, 3, 4)
        f3 = client.submit(client_job, 5, 6)

        w1 = loop.create_future()
        w2 = loop.create_future()
        w3 = loop.create_future()

        chain_future(f1, w1)
        chain_future(f2, w2)
        chain_future(f3, w3)

        assert (yield from w1)

# Generated at 2022-06-14 11:58:12.325090
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    async def test():
        # type: () -> None
        future = Future()
        chain_future(future, Future())
        assert not future.done()

    asyncio.get_event_loop().run_until_complete(test())

# Generated at 2022-06-14 11:58:22.336402
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import threading
    from tornado.escape import utf8
    from concurrent.futures import ThreadPoolExecutor

    class ThreadPoolRunOnExecutorTest(unittest.TestCase):
        def setUp(self):
            self.executor = ThreadPoolExecutor(10)

        def tearDown(self):
            self.executor.shutdown(wait=True)

        def test_no_args(self):
            @run_on_executor(executor="executor")
            def foo(self):
                pass
            f = foo(self)
            self.assertIsInstance(f, Future)
            f.set_result(None)
            ret = f.result()
            self.assertIsNone(ret)


# Generated at 2022-06-14 11:58:34.633094
# Unit test for function chain_future
def test_chain_future():
    import unittest

    io_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(io_loop)

    def finish_future(future: "Future[_T]") -> None:
        io_loop.call_later(0.01, future.set_result, None)

    class TestChainFuture(unittest.TestCase):
        def test_chain_future(self):
            f1 = Future()
            f2 = Future()
            f1.set_result(None)
            chain_future(f1, f2)
            f2.add_done_callback(self.stop)
            self.wait()

        def test_chain_cancelled(self):
            f1 = Future()
            f2 = Future()
            f2.set_result(None)
            chain

# Generated at 2022-06-14 11:58:47.001349
# Unit test for function chain_future
def test_chain_future():
    def fail_future(exc):
        future = Future()
        future_set_exc_info(future, sys.exc_info())
        return future

    def succeed_future(result):
        future = Future()
        future_set_result_unless_cancelled(future, result)
        return future

    def fail(exc):
        future = Future()
        future_set_exception_unless_cancelled(future, exc)
        return future

    # Success transfers successfully
    a = succeed_future(42)
    b = Future()
    chain_future(a, b)
    assert b.result() == 42

    # Failure transfers successfully
    a = fail(ValueError())
    b = Future()
    chain_future(a, b)
    assert b.exception() is not None

    # Chain already-com

# Generated at 2022-06-14 11:59:21.170331
# Unit test for function chain_future
def test_chain_future():
    import unittest

    from tornado import testing

    try:
        from asyncio import wait_for
    except ImportError:
        return

    class ChainFutureTest(testing.AsyncTestCase):
        def test_chain(self):
            a = Future()
            b = Future()
            chain_future(a, b)
            a.set_result(42)
            self.assertEqual(wait_for(b, 0.1), 42)

            a = Future()
            b = Future()
            chain_future(a, b)
            a.set_exception(ValueError("foo"))
            try:
                wait_for(b, 0.1)
            except Exception as e:
                self.assertIsInstance(e, ValueError)
                self.assertEqual(str(e), "foo")

# Generated at 2022-06-14 11:59:27.553433
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()
    with app_log.catch_logs() as logs:
        # set_exception no longer raises an exception if the future
        # is cancelled, it just logs
        future_set_exception_unless_cancelled(f, RuntimeError())
    assert len(logs) == 1
    assert issubclass(logs[0].exc_info[0], RuntimeError)

# Generated at 2022-06-14 11:59:31.756179
# Unit test for function chain_future
def test_chain_future():
    @gen.coroutine
    def f():
        yield gen.moment
        raise gen.Return(42)

    @gen.coroutine
    def g():
        f_future = f()
        g_future = Future()
        chain_future(f_future, g_future)
        result = yield g_future
        raise gen.Return(result)

    IOLoop.current().run_sync(g)



# Generated at 2022-06-14 11:59:43.727590
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    # This can't be in a unittest.TestCase because it uses threads
    import tornado.testing
    import time

    @tornado.testing.gen_test
    def test_chain_future_helper(executor):
        f1 = Future()
        f2 = Future()
        chain_future(f1, f2)
        f1.set_result("foo")
        result = yield f2
        tornado.testing.assert_equal("foo", result)

        f1 = Future()
        f2 = Future()
        chain_future(f1, f2)
        yield executor.submit(f1.set_result, "foo")
        result = yield f2
        tornado.testing.assert_equal("foo", result)

        f1 = Future()
        f2 = Future()

# Generated at 2022-06-14 11:59:56.529607
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    try:
        from concurrent.futures import Future
    except ImportError:
        Future = object

    def make_future(result=None, exception=None):
        # type: (Optional[Any], Optional[Exception]) -> Future[Any]
        f = Future()
        if exception is not None:
            f.set_exception(exception)
        else:
            f.set_result(result)
        return f

    f1 = make_future(1)
    f2 = make_future(2)
    chain_future(f1, f2)
    assert f2.result() == 1

    f1 = make_future(exception=KeyError)
    f2 = make_future(result=2)
    chain_future(f1, f2)

# Generated at 2022-06-14 12:00:04.123213
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import time

    def f(n):
        # type: (int) -> int
        time.sleep(n)
        return n

    io_loop = IOLoop.current()
    f1 = Future()
    f2 = Future()

    io_loop.add_callback(lambda: chain_future(io_loop.run_in_executor(None, f, 1), f1))
    io_loop.add_callback(lambda: chain_future(io_loop.run_in_executor(None, f, 2), f2))
    io_loop.add_callback(lambda: chain_future(f1, f2))

    def stop(future):
        # type: (Future) -> None
        io_loop.stop()
        assert future.result() == 1
