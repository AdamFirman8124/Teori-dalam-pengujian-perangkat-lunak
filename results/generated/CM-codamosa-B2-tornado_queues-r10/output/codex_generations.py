

# Generated at 2026-11-01 19:36:46.885678
# Unit test for constructor of class PriorityQueue
def test_PriorityQueue():
    # Test default constructor
    q = PriorityQueue()
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()

    # Test constructor with explicit maxsize
    q2 = PriorityQueue(maxsize=5)
    assert q2.maxsize == 5
    assert q2.qsize() == 0
    assert q2.empty()
    assert not q2.full()

    # Verify internal queue is initialized as a list (heap)
    assert q2._queue == []

    # Verify the queue is usable right after construction
    q2.put_nowait((1, "item"))
    assert q2.qsize() == 1
    assert not q2.empty()
    assert q2.full()

# Generated at 2026-11-01 19:37:48.428578
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado.queues import Queue, QueueFull
    from tornado.ioloop import IOLoop

    # --- Basic behavior on an empty queue ---
    q = Queue(maxsize=2)
    assert q.empty()
    q.put_nowait(1)
    assert q.qsize() == 1
    assert not q.empty()
    assert not q.full()

    # --- Queue fills up and QueueFull is raised ---
    q.put_nowait(2)
    assert q.qsize() == 2
    assert q.full()
    try:
        q.put_nowait(3)
        raise AssertionError("expected QueueFull")
    except QueueFull:
        pass
    assert q.qsize() == 2

    # --- Unbounded queue (maxsize=0) never raises QueueFull ---
    unbounded = Queue()
    for i in range(100):
        unbounded.put_nowait(i)
    assert unbounded.qsize() == 100
    assert not unbounded.full()

    # --- FIFO ordering is preserved ---
    fifo = Queue()
    for i in range(5):
        fifo.put_nowait(i)
    assert [fifo.get_nowait() for _ in range(5)] == [0, 1, 2, 3, 4]

    # --- Interaction with waiting getters ---
    async def main():
        # put_nowait wakes up a single blocked getter
        q1 = Queue()
        getter = q1.get()
        assert not getter.done()
        q1.put_nowait("hello")
        assert getter.done()
        assert getter.result() == "hello"
        assert q1.empty()  # item handed straight to the getter

        # Multiple waiting getters are served FIFO
        q2 = Queue()
        g1 = q2.get()
        g2 = q2.get()
        q2.put_nowait("a")
        q2.put_nowait("b")
        assert g1.done() and g1.result() == "a"
        assert g2.done() and g2.result() == "b"
        assert q2.empty()

        # A cancelled (expired) getter is discarded; item goes into the queue
        q3 = Queue()
        stale = q3.get()
        stale.cancel()
        q3.put_nowait("x")
        assert q3.qsize() == 1
        assert await q3.get() == "x"

    IOLoop.current().run_sync(main)

# Generated at 2026-11-01 19:38:31.205248
# Unit test for method join of class Queue
def test_Queue_join():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def _run():
        # module_0.join() on an empty queue (all tasks finished) returns immediately.
        q = Queue()
        await q.join()

        # module_0.join() blocks until every put() has a matching task_done().
        q = Queue()
        processed = []

        async def consumer():
            async for item in q:
                processed.append(item)
                q.task_done()

        IOLoop.current().spawn_callback(consumer)
        for i in range(5):
            await q.put(i)
        await q.join()
        assert processed == [0, 1, 2, 3, 4], processed

        # module_0.join(timeout=...) raises TimeoutError while tasks are unfinished.
        q = Queue()
        q.put_nowait("pending")
        try:
            await q.join(timeout=0.05)
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("module_0.join() did not time out")

        # A datetime.timedelta is accepted as a relative timeout.
        q = Queue()
        q.put_nowait("pending")
        try:
            await q.join(timeout=datetime.timedelta(seconds=0.05))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("module_0.join() did not time out with timedelta")

        # module_0.join() resumes once the final task_done() is called.
        q = Queue()
        q.put_nowait("work")

        async def delayed_done():
            await gen.sleep(0.02)
            q.task_done()

        IOLoop.current().spawn_callback(delayed_done)
        await q.join()  # Should complete without raising.

    IOLoop.current().run_sync(_run)

# Generated at 2026-11-01 19:39:17.609370
# Unit test for method __repr__ of class Queue
def test_Queue___repr__():
    # Empty queue with default maxsize
    q = Queue()
    r = repr(q)
    assert r.startswith("<Queue at ")
    assert "maxsize=0" in r
    assert r.endswith(">")
    # No queue contents shown when empty
    assert "queue=" not in r

    # Queue with items shows contents
    q.put_nowait(1)
    q.put_nowait(2)
    r = repr(q)
    assert "maxsize=0" in r
    assert "queue=deque([1, 2])" in r

    # Queue with maxsize set
    q2 = Queue(maxsize=5)
    r = repr(q2)
    assert r.startswith("<Queue at ")
    assert "maxsize=5" in r

    # Custom maxsize reflected in repr
    q3 = Queue(maxsize=1)
    q3.put_nowait("x")
    r = repr(q3)
    assert "maxsize=1" in r
    assert "queue=deque(['x'])" in r

    # str() produces shorter form without address
    s = str(q)
    assert s == "<Queue maxsize=0 queue=deque([1, 2])>"
    assert " at " not in s

    # Unfinished tasks are reported
    q4 = Queue()
    q4.put_nowait(1)
    r = repr(q4)
    assert "tasks=1" in r

    # Waiting getters are reported
    from tornado.queues import QueueEmpty

    fut = q4.get()
    r = repr(q4)
    assert "getters[1]" in r
    # Clean up: the pending future has result available now
    try:
        q4.get_nowait()
    except QueueEmpty:
        pass
    q4.task_done()

    # Waiting putters are reported
    q5 = Queue(maxsize=1)
    q5.put_nowait(1)
    putter_future = q5.put(2)
    r = repr(q5)
    assert "putters[1]" in r

# Generated at 2026-11-01 19:39:59.705816
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.queues import Queue, QueueFull, QueueEmpty

    # Empty queue raises QueueEmpty
    q = Queue()
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # FIFO order on unbounded queue
    q = Queue()
    assert q.maxsize == 0
    for i in range(3):
        q.put_nowait(i)
        assert q.qsize() == i + 1
        assert not q.empty()
    for i in range(3):
        assert q.get_nowait() == i
    assert q.empty()
    assert q.qsize() == 0

    # Bounded queue: get_nowait drains a waiting putter when full
    q = Queue(maxsize=1)
    q.put_nowait("a")
    try:
        q.put_nowait("b")
        assert False, "expected QueueFull"
    except QueueFull:
        pass
    put_future = q.put("b")
    assert not put_future.done()
    assert q.full()
    assert q.get_nowait() == "a"
    assert put_future.done()
    assert put_future.result() is None
    assert q.get_nowait() == "b"
    assert q.empty()
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # Repr/str should work while items pending
    q = Queue(maxsize=2)
    q.put_nowait(1)
    assert "maxsize=2" in str(q)
    assert q.get_nowait() == 1

# Generated at 2026-11-01 19:40:23.666308
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.queues import Queue, QueueEmpty
    from tornado import gen
    from tornado.ioloop import IOLoop

    async def _inner():
        q = Queue()

        # Empty queue raises QueueEmpty
        try:
            q.get_nowait()
            assert False, "should have raised QueueEmpty"
        except QueueEmpty:
            pass

        # Items come out in FIFO order
        q.put_nowait(0)
        q.put_nowait(1)
        assert q.get_nowait() == 0
        assert q.get_nowait() == 1
        assert q.empty()

        # A waiting getter is satisfied by put_nowait
        getter_future = q.get()
        q.put_nowait("item")
        assert (await getter_future) == "item"

        # A blocked putter is unblocked by get_nowait on a full queue
        q = Queue(maxsize=1)
        q.put_nowait("a")
        put_future = q.put("b")
        assert not put_future.done()
        assert q.get_nowait() == "a"
        await gen.sleep(0)
        assert put_future.done()
        assert q.get_nowait() == "b"

    IOLoop.current().run_sync(_inner)

# Generated at 2026-11-01 19:41:09.771081
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    q = Queue()

    # Calling module_0.task_done() with no outstanding tasks raises ValueError.
    with pytest.raises(ValueError):
        q.task_done()

    # A single put creates one unfinished task; task_done clears it.
    q.put_nowait("a")
    assert q._unfinished_tasks == 1
    assert not q._finished.is_set()
    q.task_done()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()

    # Once balanced, an extra task_done raises ValueError again.
    with pytest.raises(ValueError):
        q.task_done()

    # Multiple puts require exactly that many task_done calls.
    for i in range(3):
        q.put_nowait(i)
    assert q._unfinished_tasks == 3
    assert not q._finished.is_set()
    q.task_done()
    q.task_done()
    assert q._unfinished_tasks == 1
    assert not q._finished.is_set()
    q.task_done()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()

    # join() stays blocked until every put has a matching task_done.
    async def main():
        q2 = Queue()
        for i in range(3):
            await q2.put(i)
        join_fut = q2.join()
        assert not join_fut.done()
        for i in range(3):
            item = await q2.get()
            q2.task_done()
        assert join_fut.done()

        # After all tasks are done, further task_done calls fail.
        with pytest.raises(ValueError):
            q2.task_done()

    IOLoop.current().run_sync(main)

# Generated at 2026-11-01 19:42:10.270015
# Unit test for method put of class Queue
def test_Queue_put():
    import unittest
    from datetime import timedelta

    from tornado import gen
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.queues import Queue, QueueFull

    class TestQueuePut(AsyncTestCase):
        @gen_test
        def test_put_returns_resolved_future_when_not_full(self):
            q = Queue(maxsize=2)
            future = q.put(1)
            self.assertTrue(future.done())
            self.assertIsNone(future.result())
            self.assertEqual(q.qsize(), 1)
            self.assertFalse(q.full())

        @gen_test
        def test_put_blocks_when_full(self):
            q = Queue(maxsize=1)
            yield q.put(1)
            self.assertTrue(q.full())

            put_future = q.put(2)
            self.assertFalse(put_future.done())

            item = yield q.get()
            self.assertEqual(item, 1)

            yield put_future
            self.assertEqual(q.qsize(), 1)
            self.assertEqual(q._queue[0], 2)

        @gen_test
        def test_put_timeout_float(self):
            q = Queue(maxsize=1)
            yield q.put(1)
            with self.assertRaises(gen.TimeoutError):
                yield q.put(2, timeout=0.05)
            # Original item is unaffected.
            self.assertEqual(q.qsize(), 1)
            self.assertEqual((yield q.get()), 1)

        @gen_test
        def test_put_timeout_timedelta(self):
            q = Queue(maxsize=1)
            yield q.put(1)
            with self.assertRaises(gen.TimeoutError):
                yield q.put(2, timeout=timedelta(seconds=0.05))

        @gen_test
        def test_put_unblocked_after_timeout_cleanup(self):
            q = Queue(maxsize=1)
            yield q.put(1)
            with self.assertRaises(gen.TimeoutError):
                yield q.put(2, timeout=0.05)
            # Timed-out putter should be consumed, allowing a new put.
            q.put_nowait(3)
            self.assertEqual(q.qsize(), 1)
            self.assertEqual((yield q.get()), 3)

        @gen_test
        def test_put_wakes_waiting_getter(self):
            q = Queue()
            get_future = q.get()
            self.assertFalse(get_future.done())

            yield q.put(42)
            self.assertEqual((yield get_future), 42)
            self.assertTrue(q.empty())

        @gen_test
        def test_put_unbounded_queue_never_blocks(self):
            q = Queue()  # maxsize=0 -> unbounded
            for i in range(5):
                future = q.put(i)
                self.assertTrue(future.done())
            self.assertEqual(q.qsize(), 5)

        def test_put_nowait_raises_when_full(self):
            q = Queue(maxsize=1)
            q.put_nowait(1)
            with self.assertRaises(QueueFull):
                q.put_nowait(2)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestQueuePut)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    assert test_Queue_put()

# Generated at 2026-11-01 19:42:28.904390
# Unit test for method __anext__ of class _QueueIterator
def test__QueueIterator___anext__():
    async def _test():
        q = Queue(maxsize=1)
        iterator = _QueueIterator(q)

        # Put an item, then retrieve it via __anext__
        await q.put(1)
        result = await iterator.__anext__()
        assert result == 1

        # Queue is empty now; __anext__ should wait until an item is put
        q.put(2)
        result = await iterator.__anext__()
        assert result == 2

        # Multiple iterations in FIFO order
        await q.put(3)
        await q.put(4)
        assert await iterator.__anext__() == 3
        assert await iterator.__anext__() == 4

    asyncio.get_event_loop().run_until_complete(_test())


def test__QueueIterator___anext___async_for():
    async def _test():
        q = Queue()
        for x in range(5):
            await q.put(x)

        # Use the iterator directly through async for
        results = []
        async for item in _QueueIterator(q):
            results.append(item)
            if len(results) == 5:
                break
        assert results == [0, 1, 2, 3, 4]

    asyncio.get_event_loop().run_until_complete(_test())


def test__QueueIterator___anext___timeout():
    async def _test():
        q = Queue()
        iterator = _QueueIterator(q)

        # Getting from an empty queue raises TimeoutError
        try:
            await gen.with_timeout(datetime.timedelta(seconds=0.1), iterator.__anext__())
            assert False, "should have raised TimeoutError"
        except gen.TimeoutError:
            pass

    asyncio.get_event_loop().run_until_complete(_test())


def test__QueueIterator___anext___priority_queue():
    async def _test():
        q = PriorityQueue()
        iterator = _QueueIterator(q)
        await q.put(2)
        await q.put(1)
        await q.put(3)
        results = [await iterator.__anext__() for _ in range(3)]
        assert results == [1, 2, 3]

    asyncio.get_event_loop().run_until_complete(_test())


def test__QueueIterator___anext___lifo_queue():
    async def _test():
        q = LifoQueue()
        iterator = _QueueIterator(q)
        await q.put(1)
        await q.put(2)
        await q.put(3)
        results = [await iterator.__anext__() for _ in range(3)]
        assert results == [3, 2, 1]

    asyncio.get_event_loop().run_until_complete(_test())


from tornado.queues import _QueueIterator  # noqa: E402

# Generated at 2026-11-01 19:43:04.955228
# Unit test for method __aiter__ of class Queue
def test_Queue___aiter__():
    from tornado.queues import Queue, _QueueIterator
    from tornado.ioloop import IOLoop
    from tornado.gen import sleep

    q = Queue()

    # __aiter__ returns a _QueueIterator wrapping this queue
    iterator = q.__aiter__()
    assert isinstance(iterator, _QueueIterator)
    assert iterator.q is q
    # Each call to __aiter__ returns a new iterator object
    assert q.__aiter__() is not iterator

    # __anext__ returns an awaitable that resolves to the next queue item
    q.put_nowait("a")
    fut = iterator.__anext__()
    assert fut.result() == "a"

    # Full async-for iteration over the queue
    async def consumer():
        results = []
        async for item in q:
            results.append(item)
            if len(results) == 3:
                break
        return results

    async def producer():
        for i in range(3):
            await q.put(i)
            await sleep(0.01)

    async def main():
        IOLoop.current().spawn_callback(producer)
        results = await consumer()
        assert results == [0, 1, 2]
        assert q.empty()

    IOLoop.current().run_sync(main)

# Generated at 2026-11-01 19:43:37.794991
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    @gen.coroutine
    def run():
        q = Queue()

        # module_0.task_done() before any put raises ValueError.
        try:
            q.task_done()
            raise AssertionError("expected ValueError")
        except ValueError:
            pass

        # With no pending tasks, the finished event is set and join returns
        # immediately.
        assert q._finished.is_set()
        yield q.join()

        # Putting an item marks the queue as having unfinished work.
        yield q.put(0)
        assert q._unfinished_tasks == 1
        assert not q._finished.is_set()

        # join() does not complete until the fetched item is marked done.
        join_future = q.join()
        assert not join_future.done()

        item = yield q.get()
        assert item == 0
        q.task_done()
        assert q._unfinished_tasks == 0
        assert q._finished.is_set()
        yield join_future

        # An extra module_0.task_done() beyond the number of puts raises ValueError.
        try:
            q.task_done()
            raise AssertionError("expected ValueError")
        except ValueError:
            pass

        # Multiple items: join() completes only after every task_done call.
        q = Queue()
        for i in range(3):
            yield q.put(i)
        assert q._unfinished_tasks == 3

        for _ in range(2):
            yield q.get()
            q.task_done()
        assert q._unfinished_tasks == 1
        assert not q._finished.is_set()

        yield q.get()
        q.task_done()
        assert q._unfinished_tasks == 0
        assert q._finished.is_set()
        yield q.join()

        # Works with put_nowait/get_nowait as well.
        q = Queue()
        q.put_nowait("x")
        assert q.get_nowait() == "x"
        q.task_done()
        yield q.join()

    IOLoop.current().run_sync(run)

# Generated at 2026-11-01 19:44:22.369458
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue(maxsize=2)

# Generated at 2026-11-01 19:45:12.948285
# Unit test for method put of class Queue
def test_Queue_put():
    import datetime
    from tornado import gen
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop

    async def _test():
        # Unbounded queue: put completes immediately.
        q = Queue()
        fut = q.put(1)
        assert fut.done()
        assert fut.result() is None
        assert q.qsize() == 1
        assert not q.empty()
        assert not q.full()

        # Bounded queue: put blocks (returns unresolved future) when full.
        q2 = Queue(maxsize=1)
        await q2.put(1)
        assert q2.full()
        blocked_fut = q2.put(2)
        assert not blocked_fut.done()
        assert len(q2._putters) == 1
        assert q2.qsize() == 1  # item held by waiter, not yet in queue

        # Freeing space lets the blocked put complete.
        item = await q2.get()
        assert item == 1
        await gen.sleep(0)
        assert blocked_fut.done()
        await blocked_fut
        assert q2.qsize() == 1

        # Timed out put raises TimeoutError when queue stays full.
        q3 = Queue(maxsize=1)
        await q3.put(1)
        try:
            await q3.put(2, timeout=0.05)
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("expected TimeoutError")

        # datetime.timedelta timeout is supported as well.
        q4 = Queue(maxsize=1)
        await q4.put(1)
        try:
            await q4.put(2, timeout=datetime.timedelta(seconds=0.05))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("expected TimeoutError")

        # Multiple puts preserve FIFO ordering.
        q5 = Queue()
        await q5.put("a")
        await q5.put("b")
        assert await q5.get() == "a"
        assert await q5.get() == "b"
        assert q5.empty()

        # A blocked put satisfies a waiting getter first.
        q6 = Queue(maxsize=1)
        await q6.put(10)
        pending = q6.put(20)
        getter = q6.get()
        assert await getter == 10
        await gen.sleep(0)
        assert pending.done()
        assert await q6.get() == 20

    IOLoop.current().run_sync(_test)

# Generated at 2026-11-01 19:45:33.740715
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    async def _inner():
        q = Queue(maxsize=1)

        # Put an item: unfinished tasks counter increments, finished event clears.
        await q.put(1)
        assert q._unfinished_tasks == 1
        assert not q._finished.is_set()

        # Consume the item and mark it done.
        item = await q.get()
        assert item == 1
        q.task_done()
        assert q._unfinished_tasks == 0
        assert q._finished.is_set()

        # join() should now complete immediately.
        await gen.with_timeout(datetime.timedelta(seconds=0.1), q.join())

        # Calling task_done more times than put raises ValueError.
        try:
            q.task_done()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError from extra module_0.task_done()")

        # Multiple put/task_done cycles keep the counter consistent.
        for i in range(3):
            await q.put(i)
        assert q._unfinished_tasks == 3
        assert not q._finished.is_set()

        for i in range(3):
            await q.get()
            q.task_done()
        assert q._unfinished_tasks == 0
        assert q._finished.is_set()

    import datetime  # noqa: F401  (used inside coroutine scope above)

    IOLoop().run_sync(_inner)