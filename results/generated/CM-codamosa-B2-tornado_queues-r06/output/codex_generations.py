

# Generated at 2026-11-02 16:52:26.614945
# Unit test for method full of class Queue
def test_Queue_full():
    # Default queue (maxsize=0) is unbounded and never reports full.
    q_unbounded = Queue()
    assert not q_unbounded.full()
    q_unbounded.put_nowait("item")
    q_unbounded.put_nowait("item")
    q_unbounded.put_nowait("item")
    assert not q_unbounded.full()

    # Bounded queue is not full when empty or partially filled.
    q_bounded = Queue(maxsize=2)
    assert not q_bounded.full()
    q_bounded.put_nowait(1)
    assert not q_bounded.full()

    # Bounded queue reports full once item count reaches maxsize.
    q_bounded.put_nowait(2)
    assert q_bounded.full()

    # Removing an item makes the queue not full again.
    q_bounded.get_nowait()
    assert not q_bounded.full()

    # Refilling returns to full state.
    q_bounded.put_nowait(3)
    assert q_bounded.full()

    # Edge case: maxsize=1 is full after a single item.
    q_one = Queue(maxsize=1)
    assert not q_one.full()
    q_one.put_nowait("only")
    assert q_one.full()

# Generated at 2026-11-02 16:53:45.426598
# Unit test for method __anext__ of class _QueueIterator
def test__QueueIterator___anext__():import asyncio
import unittest

from tornado import gen
from tornado.queues import Queue, PriorityQueue, LifoQueue, _QueueIterator
from tornado.testing import AsyncTestCase, gen_test


class Test_QueueIterator___anext__(AsyncTestCase):
    @gen_test
    def test_anext_returns_queued_item(self):
        q = Queue()
        it = _QueueIterator(q)
        yield q.put(42)
        result = yield it.__anext__()
        self.assertEqual(result, 42)

    @gen_test
    def test_anext_waits_until_item_available(self):
        q = Queue()
        it = _QueueIterator(q)

        async def put_later():
            await gen.sleep(0.01)
            await q.put("hello")

        asyncio.ensure_future(put_later())
        result = yield it.__anext__()
        self.assertEqual(result, "hello")

    @gen_test
    def test_anext_fifo_order(self):
        q = Queue()
        it = _QueueIterator(q)
        yield q.put(1)
        yield q.put(2)
        self.assertEqual((yield it.__anext__()), 1)
        self.assertEqual((yield it.__anext__()), 2)

    @gen_test
    def test_anext_with_priority_queue(self):
        q = PriorityQueue()
        it = _QueueIterator(q)
        yield q.put(3)
        yield q.put(1)
        self.assertEqual((yield it.__anext__()), 1)
        self.assertEqual((yield it.__anext__()), 3)

    @gen_test
    def test_anext_with_lifo_queue(self):
        q = LifoQueue()
        it = _QueueIterator(q)
        yield q.put(1)
        yield q.put(2)
        self.assertEqual((yield it.__anext__()), 2)
        self.assertEqual((yield it.__anext__()), 1)

    @gen_test
    def test_anext_is_coroutine_awaitable(self):
        q = Queue()
        it = _QueueIterator(q)
        yield q.put("x")
        fut = it.__anext__()
        self.assertTrue(asyncio.isfuture(fut) or hasattr(fut, "__await__"))
        result = yield fut
        self.assertEqual(result, "x")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 16:55:15.656399
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    # Calling task_done with no pending tasks raises ValueError
    q = Queue()
    try:
        q.task_done()
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError from module_0.task_done() called too many times")

    # Each put must be matched by exactly one task_done
    q = Queue()
    q.put_nowait(1)
    assert q._unfinished_tasks == 1
    assert not q._finished.is_set()

    item = q.get_nowait()
    assert item == 1
    q.task_done()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()

    # A second task_done without a new put raises ValueError
    try:
        q.task_done()
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError from extra module_0.task_done()")

    # Multiple puts/getters: join() completes only after all task_done calls
    async def main():
        q = Queue()
        for i in range(3):
            await q.put(i)
        assert q._unfinished_tasks == 3
        assert not q._finished.is_set()

        for _ in range(3):
            await q.get()
            q.task_done()

        assert q._unfinished_tasks == 0
        assert q._finished.is_set()
        await q.join()

    IOLoop.current().run_sync(main)

# Generated at 2026-11-02 16:56:30.803824
# Unit test for constructor of class LifoQueue
def test_LifoQueue():
    from tornado.queues import LifoQueue, QueueFull, QueueEmpty

    # Default construction: unbounded queue
    q = LifoQueue()
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()
    assert isinstance(q._queue, list)

    # Explicit maxsize=0 means unbounded
    q0 = LifoQueue(maxsize=0)
    assert q0.maxsize == 0
    assert not q0.full()

    # Positive maxsize is honored
    q2 = LifoQueue(maxsize=2)
    assert q2.maxsize == 2
    assert not q2.full()
    q2.put_nowait(1)
    assert not q2.full()
    q2.put_nowait(2)
    assert q2.full()
    try:
        q2.put_nowait(3)
        raise AssertionError("expected QueueFull")
    except QueueFull:
        pass

    # maxsize=None raises TypeError
    try:
        LifoQueue(maxsize=None)
        raise AssertionError("expected TypeError")
    except TypeError:
        pass

    # Negative maxsize raises ValueError
    try:
        LifoQueue(maxsize=-1)
        raise AssertionError("expected ValueError")
    except ValueError:
        pass

    # Constructor initializes internal state correctly
    q3 = LifoQueue()
    assert len(q3._getters) == 0
    assert len(q3._putters) == 0
    assert q3._unfinished_tasks == 0
    assert q3._finished.is_set()

    # LIFO ordering: most recently put item is retrieved first
    q4 = LifoQueue()
    q4.put_nowait(3)
    q4.put_nowait(2)
    q4.put_nowait(1)
    assert q4.get_nowait() == 1
    assert q4.get_nowait() == 2
    assert q4.get_nowait() == 3
    assert q4.empty()
    try:
        q4.get_nowait()
        raise AssertionError("expected QueueEmpty")
    except QueueEmpty:
        pass

# Generated at 2026-11-02 16:57:46.646982
# Unit test for method __anext__ of class _QueueIterator