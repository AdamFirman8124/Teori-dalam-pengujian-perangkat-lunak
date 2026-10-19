

# Generated at 2022-06-14 11:50:19.383760
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    import threading
    import time

    ioloop = mock.Mock()

    class TestClass(object):
        def __init__(self):
            self.executor = dummy_executor

        @run_on_executor
        def method(self):
            # type: () -> int
            return 42

    t = TestClass()
    f = t.method()
    f.result()
    assert f.done()
    assert f.result() == 42

# Generated at 2022-06-14 11:50:30.414711
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase, gen_test

    class _Base(AsyncTestCase):
        def setUp(self) -> None:
            self.io_loop = IOLoop()
            self.io_loop.make_current()

    class ReturnFutureTest(_Base):
        @gen_test
        def test_chain_future(self) -> None:
            result = {"foo": "bar"}
            fut = Future()  # type: Future[str]
            result2 = yield fut
            self.assertEqual(result, result2)

            fut2 = Future()
            chain_future(fut, fut2)
            fut.set_result(result)
            result3 = yield fut2
            self.assertEqual(result, result3)

            fut3 = Future

# Generated at 2022-06-14 11:50:37.839401
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop.current()
    async_fut = Future()
    conc_fut = futures.Future()
    chain_future(conc_fut, async_fut)

    @testing.gen_test
    def f():
        yield conc_fut
        self.assertTrue(async_fut.done())
        self.assertTrue(async_fut.result())

    conc_fut.set_result(True)
    io_loop.run_sync(f)



# Generated at 2022-06-14 11:50:43.826227
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, ValueError("yikes"))
    assert future.exception() is not None
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError("yikes"))
    assert future.exception() is None # no error is logged here



# Generated at 2022-06-14 11:50:52.645149
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import mock

    class ChainFutureTest(unittest.TestCase):
        def setUp(self):
            self.old_future = None

        def _mock_future(self, *args, **kwargs):
            new_future = mock.Mock(*args, **kwargs)
            if self.old_future is not None:
                self.old_future.__class__.return_value = new_future
            self.old_future = new_future
            return new_future

        def test_chain_future(self):
            f1 = self._mock_future()
            f2 = self._mock_future()
            f1.done.return_value = True
            chain_future(f1, f2)
            self.assertFalse(f2.set_result.called)


# Generated at 2022-06-14 11:51:03.437606
# Unit test for function chain_future
def test_chain_future():
    io_loop = asyncio.get_event_loop()
    f1 = io_loop.create_future()
    f2 = io_loop.create_future()
    chain_future(f1, f2)
    f1.set_result(3)
    io_loop.run_until_complete(f2)
    assert f2.result() == 3

    f1 = asyncio.Future()
    f2 = asyncio.Future()
    chain_future(f1, f2)
    f1.set_result(3)
    io_loop.run_until_complete(f2)
    assert f2.result() == 3

    f1 = futures.Future()
    f2 = asyncio.Future()
    chain_future(f1, f2)
    f1.set_result(3)


# Generated at 2022-06-14 11:51:12.478449
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    loop = IOLoop.current()

    async def read_and_set_result(future: Future) -> None:
        await asyncio.sleep(0.01)
        future.set_result("done")

    async def test() -> None:
        a = Future()
        b = Future()
        loop.add_future(read_and_set_result(a), lambda x: None)
        chain_future(a, b)
        assert (await b) == "done"

    loop.run_sync(test)

# Generated at 2022-06-14 11:51:16.208897
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    f.cancel()
    future_set_result_unless_cancelled(f, "abc")
    assert not f.cancelled()
    assert f.exception() is not None
    assert isinstance(f.exception(), futures.CancelledError)


# Generated at 2022-06-14 11:51:23.333248
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    exc = Exception("test_future_set_exception_unless_cancelled")
    future_set_exception_unless_cancelled(future, exc)
    assert future.exception() == exc

    future2 = Future()
    future2.cancel()
    future_set_exception_unless_cancelled(future2, exc)

# Generated at 2022-06-14 11:51:29.445919
# Unit test for function run_on_executor
def test_run_on_executor():
    class Foo(object):
        def __init__(self):
            self.executor = dummy_executor

        @run_on_executor
        def bar(self, arg):
            return arg + 1
    foo = Foo()
    result_future = foo.bar(1)
    assert isinstance(result_future, Future)
    assert result_future.result() == 2

# Generated at 2022-06-14 11:51:44.233433
# Unit test for function run_on_executor
def test_run_on_executor():
    class TestClass(object):
        def __init__(self, executor):
            self.executor = executor

        def _test_method(self, arg1, arg2, kwarg1=None, kwarg2=None):
            assert self is not None
            assert arg1 == 7
            assert arg2 == 9
            assert kwarg1 == "hello"
            assert kwarg2 == "goodbye"
            return arg1 + arg2

        test_method = run_on_executor()(_test_method)

# Generated at 2022-06-14 11:51:49.715341
# Unit test for function chain_future
def test_chain_future():
    loop = asyncio.get_event_loop()
    a = Future()
    b = Future()
    chain_future(a, b)

    @run_on_executor
    def finish_a(a, result):
        a.set_result(result)
        return result + 1

    loop.run_until_complete(finish_a(a, 1))
    assert b.result() == 1
    loop.close()

# Generated at 2022-06-14 11:51:57.141544
# Unit test for function chain_future
def test_chain_future():
    """Tests that the future returned by f2 is completed when the one returned
    by f1 is.
    """
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(None)
    assert f2.done()
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ReturnValueIgnoredError())
    assert f2.done()

# Generated at 2022-06-14 11:52:00.127089
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 10)
    assert future.cancelled()



# Generated at 2022-06-14 11:52:07.382779
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    assert not future1.done()
    assert not future2.done()

    chain_future(future1, future2)
    future1.set_result(None)
    assert future1.done()
    assert future2.done()

    future1 = Future()
    future2 = Future()
    assert not future1.done()
    assert not future2.done()

    chain_future(future1, future2)
    future2.cancel()
    assert future2.cancelled()
    future1.set_result(None)
    assert future1.done()
    assert future2.done()
    assert future2.cancelled()

    future1 = Future()
    future2 = Future()
    assert not future1.done()

# Generated at 2022-06-14 11:52:11.238001
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # Test that it handles the case where the future is cancelled correctly
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError())


# Generated at 2022-06-14 11:52:15.544426
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()

    future_set_result_unless_cancelled(future, None)
    assert future.done()

    future = Future()

    future.cancel()
    future_set_result_unless_cancelled(future, None)
    assert future.cancelled()



# Generated at 2022-06-14 11:52:23.302196
# Unit test for function run_on_executor
def test_run_on_executor():
    from functools import partial

    class Foo:
        executor = dummy_executor

        @run_on_executor
        def func(self, a, b):
            return a + b

    foo = Foo()

    # Make sure calling the wrapped function directly works
    assert foo.func(3, 4) is None
    foo.func(3, 4).add_done_callback(partial(future_set_result_unless_cancelled, None))
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(foo.func(3, 4))
    assert result == 7

    # Make sure calling through the wrapper correctly passes varargs
    class Foo:
        executor = dummy_executor


# Generated at 2022-06-14 11:52:25.860786
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    import asyncio

    sync_future = DummyExecutor().submit(lambda: 1 + 2)
    async def main():
        return await asyncio.wrap_future(sync_future)

    assert asyncio.run(main()) == 3

# Generated at 2022-06-14 11:52:37.032827
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    f = Future()
    f.set_exception(ValueError())
    assert f.done()
    f = Future()
    f.cancel()
    assert f.done()
    future_set_exception_unless_cancelled(f, TypeError())
    f.add_done_callback(lambda f: f.result())
    assert f.done()
    # get_result() should raise the TypeError, not the ValueError
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, ValueError())
    future_set_exception_unless_cancelled(f, TypeError())
    with pytest.raises(TypeError):
        f.result()
    # When logging is disabled, the exception should not be logged:

# Generated at 2022-06-14 11:52:46.821084
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(None)
    assert f2.done()



# Generated at 2022-06-14 11:52:55.941029
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    future_set_exception_unless_cancelled(future, Exception())
    assert future.result() == 1
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    future_set_exception_unless_cancelled(future, Exception())
    assert future.result() == 1
    exception = Exception()
    future = Future()
    future.cancel()
    future_set_exc_info(future, (None, exception, None))
    exception2 = None
    try:
        future_set_exc_info(
            future, (None, exception, None)
        )  # type: ignore
    except Exception as e:
        exception2 = e

# Generated at 2022-06-14 11:53:05.750827
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, "value")
    assert future.result() == "value"

    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, "value")
    assert future.cancelled()

    # future_set_result_unless_cancelled will not change the result of a future
    # that has already been set
    future = Future()
    future.set_result("result")
    future_set_result_unless_cancelled(future, "value")
    assert future.result() == "result"



# Generated at 2022-06-14 11:53:09.465321
# Unit test for function chain_future
def test_chain_future():
    ioloop = asyncio.new_event_loop()
    asyncio.set_event_loop(ioloop)
    source = Future()
    destination = Future()
    chain_future(source, destination)
    source.set_result(42)
    ioloop.run_until_complete(destination)
    assert destination.result() == 42


# Generated at 2022-06-14 11:53:21.011200
# Unit test for function chain_future
def test_chain_future():
    async def test_helper(
        source_exc: Exception, sink_exc: Exception, source_set: bool
    ) -> None:
        source = Future()
        sink = Future()
        chain_future(source, sink)
        # ensure that we have a reference to the exception
        if source_exc:
            source_exc.args
        if source_set:
            source.set_result(None)
            assert not sink.done()
            source.set_exception(source_exc)
        else:
            source.set_exception(source_exc)
        if sink_exc is not None:
            assert sink.exception() is sink_exc
        else:
            assert sink.exception() is None
        return


# Generated at 2022-06-14 11:53:26.579827
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing

    @tornado.testing.gen_test
    def test_chain():
        conc_future = concurrent.futures.Future()  # type: futures.Future[_T]
        io_future = Future()  # type: Future[_T]
        chain_future(conc_future, io_future)
        assert not conc_future.done()
        assert not io_future.done()
        assert conc_future.set_result(42) is None
        assert conc_future.result() == 42
        assert io_future.result() == 42

    test_chain()



# Generated at 2022-06-14 11:53:38.690106
# Unit test for function chain_future
def test_chain_future():
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    io_loop = asyncio.get_event_loop()

    f1 = Future()
    f2 = Future()

    # chain when f1 is not done.
    chain_future(f1, f2)
    io_loop.run_until_complete(asyncio.wait([f1, f2], timeout=1))
    assert f1.done() and f2.done()

    # chain when f1 is already done.
    f1 = Future()
    f1.set_result(1)
    f2 = Future()
    chain_future(f1, f2)
    io_loop.run_until_complete(asyncio.wait([f1, f2], timeout=1))
    assert f1.done()

# Generated at 2022-06-14 11:53:52.591508
# Unit test for function run_on_executor
def test_run_on_executor():
    called = []

    class MyTestObj(object):
        executor = dummy_executor

        @run_on_executor
        def method(self, arg):
            called.append(arg)
            return arg + 5

        @run_on_executor(executor="_other_pool")
        def method_with_explicit_attr(self, arg):
            called.append(arg)
            return arg + 5

    obj = MyTestObj()

    f = obj.method(42)
    assert is_future(f)
    assert called == [42]
    result = f.result()
    assert result == 47
    assert called == [42]

    f = obj.method_with_explicit_attr(42)
    assert is_future(f)
    assert called == [42, 42]

# Generated at 2022-06-14 11:53:56.231241
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def test_run(t: Future) -> None:
        t.set_result("done")

    if __name__ == "__main__":
        from tornado.testing import AsyncTestCase, gen_test

        gen_test(test_run)

# Generated at 2022-06-14 11:54:03.122951
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception("oops"))
    assert future.exception() is not None
    assert str(future.exception()) == "oops"

    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception("oops"))
    assert future.exception() is None

# Generated at 2022-06-14 11:54:11.220776
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    # type: () -> None
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 1)  # does not raise

# Generated at 2022-06-14 11:54:15.121389
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    execution = future_add_done_callback(dummy_executor.submit, lambda x: print(x))
    print(execution.set_result('Execution finished'))

# Generated at 2022-06-14 11:54:20.545846
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.cancel()
    try:
        future.set_exception(Exception("Test"))
        raise AssertionError("should have thrown")
    except asyncio.InvalidStateError:
        # Success, the future is cancelled.
        pass
    future_set_exception_unless_cancelled(future, Exception("Test"))

# Generated at 2022-06-14 11:54:28.365505
# Unit test for function chain_future
def test_chain_future():
    import time
    import unittest

    from tornado.ioloop import IOLoop

    a = Future()
    b = Future()

    def callback(future):
        assert future is a
        assert b.done()
        assert not b.cancelled()
        assert b.exception() is None
        assert b.result() == 42

    chain_future(a, b)

    future_add_done_callback(b, callback)

    def set_value():
        a.set_result(42)

    IOLoop.current().call_later(0.01, set_value)
    IOLoop.current().start()



# Generated at 2022-06-14 11:54:31.355738
# Unit test for function chain_future
def test_chain_future():
    async def f():
        future = Future()
        chain_future(Future(), future)
        await future

    asyncio.run(f())

# Generated at 2022-06-14 11:54:42.505775
# Unit test for function chain_future
def test_chain_future():
    from tornado.log import gen_log

    @gen.coroutine
    def f():
        gen_log.debug("f() called")
        yield gen.sleep(0.01)
        gen_log.debug("f() done")
        raise gen.Return(42)

    @gen.coroutine
    def g():
        gen_log.debug("g() called")
        f_future = yield f()
        assert f_future.done()
        gen_log.debug("g() done")
        raise gen.Return(f_future.result())

    result = g()
    assert isinstance(result, Future)
    assert not result.done()
    IOLoop.current().add_future(result, lambda result: gen_log.debug("result done"))
    # Give IOLoop a chance to call the callback
    IOL

# Generated at 2022-06-14 11:54:55.096702
# Unit test for function chain_future
def test_chain_future():
    def thread_func():
        yield gen.sleep(0.01)
        raise Exception("from thread")

    def noop(*args, **kwargs):
        pass

    a = future_initialized(Future())
    b = future_initialized(futures.Future())
    chain_future(b, a)

    ioloop = IOLoop()
    ioloop.add_callback(noop, ioloop)
    ioloop.add_callback(noop, ioloop)
    ioloop.add_callback(noop, ioloop)
    ioloop.add_callback(noop, ioloop)
    ioloop.add_future(a, lambda x: None)
    ioloop.add_future(b, lambda x: None)


# Generated at 2022-06-14 11:55:03.663781
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_result(42)
    assert future2.result() == 42

    # Test a chain with a combination of concurrent.futures.Futures
    # and asyncio.Futures.
    future3 = futures.Future()
    future4 = Future()
    chain_future(future3, future4)
    future3.set_result(42)
    assert future4.result() == 42

    # Test that cancel propagates
    future5 = Future()
    future6 = Future()
    chain_future(future5, future6)
    future6.cancel()
    future5.set_result(42)
    assert future6.cancelled()

    #

# Generated at 2022-06-14 11:55:15.634655
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import time

    f1 = Future()  # type: Future[str]
    f2 = Future()  # type: Future[str]
    chain_future(f1, f2)
    f1.set_result("f1_result")
    assert f2.result() == "f1_result"

    f3 = Future()  # type: Future[str]
    f4 = Future()  # type: Future[str]
    chain_future(f3, f4)
    f3.set_exception(ValueError("inconceivable"))
    try:
        f4.result()
        assert False
    except ValueError:
        pass

    f5 = Future()  # type: Future[str]
    f6 = Future()  # type: Future[str]
    chain_

# Generated at 2022-06-14 11:55:20.190672
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 1)
    assert future.done() and future.result() == 1
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, 1)
    assert not future.done()

# Generated at 2022-06-14 11:55:32.058669
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42



# Generated at 2022-06-14 11:55:34.098424
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    f.cancel()
    future_set_result_unless_cancelled(f, None)

# Generated at 2022-06-14 11:55:47.192186
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    ioloop = IOLoop()
    source = Future()
    target = Future()
    chain_future(source, target)

    results = []

    def f1(future):
        results.append('f1')
        assert future is source
        assert not target.done()
        assert source.result() == 'source-result'
        ioloop.stop()

    def f2(future):
        results.append('f2')
        assert future is source
        assert source.result() == 'source-result'
        target.set_result('target-result')

    def f3(future):
        results.append('f3')
        assert future is target
        assert target.result() == 'target-result'
        ioloop.stop()


# Generated at 2022-06-14 11:56:00.504686
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop, TimeoutError
    from tornado import gen
    from tornado.testing import AsyncTestCase

    ioloop = IOLoop.current()

    class TestCase(AsyncTestCase):
        def setUp(self):
            super(TestCase, self).setUp()
            self.executor = futures.ThreadPoolExecutor(1)

        def tearDown(self):
            super(TestCase, self).tearDown()
            self.executor.shutdown()

        @gen.coroutine
        def test_chain_future(self):
            future1 = Future()
            future2 = Future()
            chain_future(future1, future2)
            self.assertFalse(future2.done())
            future1.set_result(42)
            yield future2
            self.assertEqual

# Generated at 2022-06-14 11:56:09.524276
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import io
    import os
    import tempfile
    import time

    class Test_chain_future(unittest.TestCase):
        def test_chain_future1(self):
            f2 = Future()
            chain_future(f2, f2)
            self.assertFalse(f2.done())
            f2.set_result(None)
            self.assertTrue(f2.done())

        def test_chain_future2(self):
            f = Future()
            f2 = Future()
            chain_future(f, f2)
            self.assertFalse(f.done())
            f.set_result(None)
            self.assertTrue(f.done())
            self.assertTrue(f2.done())

        def test_chain_future3(self):
            self

# Generated at 2022-06-14 11:56:18.555250
# Unit test for function chain_future
def test_chain_future():
    import threading
    import unittest
    from unittest import mock

    fut1 = Future()
    fut2 = Future()
    fut1.add_done_callback_result = None

    def callback(future):
        if future is not fut1:
            raise AssertionError()
        fut1.add_done_callback_result = True

    chain_future(fut1, fut2)
    fut1.add_done_callback(callback)

    fut1.set_result(1)
    assert fut1.add_done_callback_result is True
    assert fut2.result() == 1
    assert fut1.result() == 1

    result = [False]

    def callback2(future):
        if future is not fut1:
            raise AssertionError()
        result[0] = True

    fut

# Generated at 2022-06-14 11:56:24.780510
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    loop = asyncio.get_event_loop()

    @asyncio.coroutine
    def _chain_future():
        f = Future()
        f2 = Future()
        chain_future(f, f2)
        f.set_result(42)
        x = yield f2
        raise gen.Return(x)

    assert loop.run_until_complete(_chain_future()) == 42



# Generated at 2022-06-14 11:56:37.436442
# Unit test for function chain_future
def test_chain_future():
    import time

    async def f():
        a = Future()
        b = Future()
        chain_future(a, b)

        assert not a.done()
        assert not b.done()

        a.set_result(None)

        await a
        await b

        assert a.done()
        assert b.done()

        c = Future()
        d = Future()
        chain_future(c, d)

        assert not c.done()
        assert not d.done()

        d.cancel()

        with pytest.raises(asyncio.CancelledError):
            await c
        with pytest.raises(asyncio.CancelledError):
            await d

        assert c.done()
        assert d.done()

        e = Future()
        f = Future()
        chain_future

# Generated at 2022-06-14 11:56:53.996885
# Unit test for function chain_future
def test_chain_future():
    future_1 = Future()
    future_1_result = 123
    future_2 = Future()
    future_2_result = 456
    future_3 = Future()
    future_3_result = 789
    future_4 = Future()
    future_4_result = None

    chain_future(future_1, future_2)
    chain_future(future_2, future_3)
    chain_future(future_3, future_4)

    @asyncio.coroutine
    def set_future_1():
        yield from asyncio.sleep(0.1)
        future_1.set_result(future_1_result)

    @asyncio.coroutine
    def set_future_3():
        yield from asyncio.sleep(0.3)

# Generated at 2022-06-14 11:56:55.478001
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, RuntimeError("test"))

# Generated at 2022-06-14 11:57:17.961868
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing
    import tornado.concurrent
    import tornado.gen

    class SomeError(Exception):
        pass

    @tornado.gen.coroutine
    def sleep_and_raise(value):
        yield tornado.gen.sleep(0.01)
        raise SomeError(value)

    @tornado.gen.coroutine
    def test_add(x, y):
        result = yield x + y
        raise tornado.gen.Return(result)

    @tornado.nio.streams.StreamReader.wait_for_read
    def wait_for_read_mock(self, callback):
        callback()

    def test_chain_future():  # type: ignore
        f1 = tornado.concurrent.Future()
        f2 = tornado.concurrent.Future()

# Generated at 2022-06-14 11:57:24.582676
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # type: () -> None
    future = Future()  # type: Future
    future_set_exception_unless_cancelled(future, ValueError())
    assert isinstance(future.exception(), ValueError)
    assert not future.cancelled()


if typing.TYPE_CHECKING:
    _F = typing.TypeVar("_F", bound=Future)



# Generated at 2022-06-14 11:57:30.144809
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()  # type: Future[int]
    f2 = Future()  # type: Future[int]

    chain_future(f1, f2)

    assert not f2.done()

    f1.set_result(42)
    assert_future_result(f2, 42)



# Generated at 2022-06-14 11:57:34.892820
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    assert b.result() == 42, b.result()



# Generated at 2022-06-14 11:57:48.118914
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    @types.coroutine
    def async_foo():
        # type: () -> None
        raise ValueError

    @types.coroutine
    def async_bar():
        # type: () -> None
        raise ZeroDivisionError

    @types.coroutine
    def async_baz():
        # type: () -> None
        await asyncio.sleep(0)

    def sync_foo():
        # type: () -> None
        raise ValueError

    def sync_bar():
        # type: () -> None
        raise ZeroDivisionError

    def sync_baz():
        # type: () -> None
        pass


# Generated at 2022-06-14 11:57:53.807944
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class _ChainFutureTest(AsyncTestCase):
        def test_chain_future(self):
            f = Future()  # type: Future[int]
            g = Future()  # type: Future[int]
            chain_future(f, g)
            f.set_result(42)
            self.assertEqual(g.result(), 42)

    _ChainFutureTest().run()

# Generated at 2022-06-14 11:58:04.414607
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop.current()
    io_loop.make_current()

    from concurrent import futures

    executor = futures.ThreadPoolExecutor(2)

    class MyObject:
        def __init__(self):
            self.executor = executor

        @run_on_executor
        def slow_method(self):
            return 42

        def fast_method(self):
            return 1

    o = MyObject()

    # chain together the futures returned by slow_method and fast_method
    futures_future = o.slow_method()
    futures_future.add_done_callback(lambda f: f.result() + 1)

    # chain together the futures returned by fast_method and slow_method
    futures_future2 = o.fast_method()

# Generated at 2022-06-14 11:58:13.792650
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = concurrent.futures.Future()
    future_set_exception_unless_cancelled(future, ValueError("foo"))
    assert future.exception().args[0] == "foo"

    future = asyncio.Future()
    future_set_exception_unless_cancelled(future, ValueError("foo"))
    assert future.exception().args[0] == "foo"

    future = concurrent.futures.Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, ValueError("bar"))
    assert future.cancelled()
    assert future.exception() is None

# Generated at 2022-06-14 11:58:21.047148
# Unit test for function chain_future
def test_chain_future():
    import unittest.mock
    from tornado.testing import gen_test

    @gen_test
    def test(self):
        fut = Future()
        fut2 = Future()
        chain_future(fut, fut2)
        self.assertFalse(fut2.done())
        fut.set_result(42)
        self.assertTrue(fut2.done())
        self.assertEqual(fut2.result(), 42)

    test(unittest.mock.Mock())

# Generated at 2022-06-14 11:58:33.517722
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()  # type: Future[int]
    f2 = Future()

    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(42)
    assert f2.result() == 42

    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f1.set_exception(ValueError())
    try:
        f2.result()
        assert False, "Expected exception"
    except ValueError:
        pass

    # Callbacks added to f1 after chain_future shouldn't affect f2.
    f1 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f

# Generated at 2022-06-14 11:58:45.181266
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, ValueError())
    try:
        future.result()
        assert False
    except ValueError:
        pass

# Generated at 2022-06-14 11:58:56.098511
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    loop = IOLoop.current()
    f1 = Future()  # type: Future[str]
    f2 = Future()  # type: Future[str]

    chain_future(f1, f2)

    @run_on_executor
    def f():
        # type: () -> str
        return 'done'

    res = f()
    chain_future(res, f1)

    @gen.coroutine
    def t():
        r = yield f1
        IOLoop.current().stop()

    loop.add_future(res, lambda f: loop.add_future(f1, lambda f: IOLoop.current().stop()))
    loop.start()
    loop.run_sync(t)

    assert res.exception() is None

# Generated at 2022-06-14 11:59:03.204597
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception())
    assert future.exception() is not None
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception())
    assert future.exception() is None

# Generated at 2022-06-14 11:59:12.632757
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    f3 = Future()
    chain_future(f1, f2)
    chain_future(f2, f3)
    f1.set_result(42)
    assert f3.result() == 42
    f1 = Future()
    f2 = Future()
    f3 = Future()
    chain_future(f1, f2)
    chain_future(f2, f3)
    f1.set_exception(RuntimeError("hello"))
    with pytest.raises(RuntimeError) as exc:
        f3.result()
    assert str(exc.value) == "hello"



# Generated at 2022-06-14 11:59:22.159387
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue()

    async def worker():
        return 1 / 0

    async def run_worker():
        try:
            await worker()
        except ZeroDivisionError:
            pass

        return q.get()

    async def run_test():
        f = asyncio.ensure_future(run_worker())
        future_set_exception_unless_cancelled(f, ZeroDivisionError())
        await f
        q.put_nowait(None)

    IOLoop.current().run_sync(run_test)

# Generated at 2022-06-14 11:59:28.230767
# Unit test for function chain_future
def test_chain_future():
    import unittest
    from tornado.testing import AsyncTestCase, gen_test

    class FutureTests(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            a = Future()
            b = Future()
            chain_future(a, b)
            a.set_result(5)

# Generated at 2022-06-14 11:59:34.118617
# Unit test for function chain_future
def test_chain_future():
    next_future = Future()
    a = Future()

    def callback_a(f):
        assert f is a
        next_future.set_result(None)

    chain_future(a, next_future)
    a.set_result(None)
    future_add_done_callback(a, callback_a)



# Generated at 2022-06-14 11:59:44.943968
# Unit test for function chain_future
def test_chain_future():
    # Save and restore the dummy thread pool.
    old = dummy_executor.submit

# Generated at 2022-06-14 11:59:54.636365
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test

    class MyTestCase(AsyncTestCase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.executor = futures.ThreadPoolExecutor(4)

        @gen_test
        def test_chain_future(self):
            future_a = Future()
            future_b = Future()

            chain_future(future_a, future_b)

            future_a.set_result(42)

# Generated at 2022-06-14 12:00:00.530522
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    class Thing(object):
        _thread_pool = dummy_executor

        @run_on_executor(executor="_thread_pool")
        def function(self, x, y, z):
            # type: (int, int, int) -> int
            return x + y + z

    thing = Thing()
    future = thing.function(1, 2, z=3)
    assert future.result() == 6