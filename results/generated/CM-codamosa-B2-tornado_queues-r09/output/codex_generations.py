

# Generated at 2026-11-02 08:25:18.468388
# Unit test for method get_nowait of class Queue

# Generated at 2026-11-02 08:25:36.488717
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():q = Queue()

# Generated at 2026-11-02 08:25:43.535852
# Unit test for constructor of class QueueEmpty
def test_QueueEmpty():
    # QueueEmpty should be instantiable with no arguments
    exc = QueueEmpty()
    assert isinstance(exc, QueueEmpty)
    assert isinstance(exc, Exception)

    # It should support standard exception behavior
    assert str(exc) == ""

    # It should be raisable and catchable
    try:
        raise QueueEmpty()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("QueueEmpty was not raised")

    # It should be catchable as a generic Exception
    try:
        raise QueueEmpty()
    except Exception:
        pass
    else:
        raise AssertionError("QueueEmpty was not caught as Exception")

    # It should support message arguments like a normal Exception
    exc_with_msg = QueueEmpty("queue is empty")
    assert str(exc_with_msg) == "queue is empty"
    assert exc_with_msg.args == ("queue is empty",)

# Generated at 2026-11-02 08:25:54.815796
# Unit test for method put of class Queue

# Generated at 2026-11-02 08:26:05.773372
# Unit test for method put of class Queue
def test_Queue_put():from tornado.queues import Queue


# Generated at 2026-11-02 08:26:21.337815
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    async def main():
        q = Queue()

        # module_0.task_done() before any put() raises ValueError
        try:
            q.task_done()
            raise AssertionError("expected ValueError")
        except ValueError:
            pass

        # Put two items; unfinished task count and finished event update
        q.put_nowait(1)
        q.put_nowait(2)
        assert q._unfinished_tasks == 2
        assert not q._finished.is_set()

        # Consume first item and mark it done
        item = await q.get()
        assert item == 1
        q.task_done()
        assert q._unfinished_tasks == 1
        assert not q._finished.is_set()

        # join() is still blocked while a task remains unfinished
        join_future = q.join()
        assert not join_future.done()

        # Consume second item and mark it done
        item = await q.get()
        assert item == 2
        q.task_done()
        assert q._unfinished_tasks == 0
        assert q._finished.is_set()
        assert join_future.done()
        await join_future

        # Extra module_0.task_done() calls raise ValueError
        try:
            q.task_done()
            raise AssertionError("expected ValueError")
        except ValueError:
            pass

        # join() times out if tasks remain unfinished
        q.put_nowait(3)
        try:
            await q.join(timeout=datetime.timedelta(seconds=0.05))
            raise AssertionError("expected TimeoutError")
        except gen.TimeoutError:
            pass
        q.task_done()
        await q.join()

    ioloop.IOLoop.current().run_sync(main)

# Generated at 2026-11-02 08:26:33.467344
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado import gen
from tornado.testing import AsyncTestCase, gen_test
from tornado.queues import Queue, QueueFull

import unittest


class TestQueuePutNowait(AsyncTestCase):
    def test_put_nowait_adds_item(self):
        q = Queue()
        self.assertTrue(q.empty())
        q.put_nowait("item1")
        self.assertEqual(q.qsize(), 1)
        self.assertFalse(q.empty())

    def test_put_nowait_multiple_items(self):
        q = Queue()
        for i in range(5):
            q.put_nowait(i)
        self.assertEqual(q.qsize(), 5)

    def test_put_nowait_full_raises(self):
        q = Queue(maxsize=1)
        q.put_nowait(1)
        self.assertTrue(q.full())
        with self.assertRaises(QueueFull):
            q.put_nowait(2)
        self.assertEqual(q.qsize(), 1)

    def test_put_nowait_unbounded_never_full(self):
        q = Queue(maxsize=0)
        for i in range(100):
            q.put_nowait(i)
        self.assertEqual(q.qsize(), 100)
        self.assertFalse(q.full())

    def test_put_nowait_fills_to_maxsize(self):
        q = Queue(maxsize=3)
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        self.assertTrue(q.full())
        with self.assertRaises(QueueFull):
            q.put_nowait(4)

    @gen_test
    def test_put_nowait_wakes_getter(self):
        q = Queue()
        getter = q.get()
        q.put_nowait(42)
        item = yield getter
        self.assertEqual(item, 42)
        self.assertTrue(q.empty())

    @gen_test
    def test_put_nowait_with_waiting_getter_bypasses_queue(self):
        q = Queue(maxsize=1)
        q.put_nowait("a")
        getter = q.get()  # getter waits, queue still full with "a"
        # Getter hasn't consumed yet (get resolves only when woken).
        q.put_nowait("b")  # goes directly to waiting getter
        item = yield getter
        self.assertEqual(item, "b")

    def test_put_nowait_marks_unfinished_task(self):
        q = Queue()
        q.put_nowait(1)
        self.assertFalse(q._finished.is_set())
        q.task_done()
        self.assertTrue(q._finished.is_set())

    def test_put_nowait_then_join_completes(self):
        q = Queue()
        q.put_nowait(1)
        q.task_done()
        future = q.join()
        self.assertTrue(future.done())


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 08:27:21.245760
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime

    from tornado.ioloop import IOLoop
    from tornado.queues import Queue, QueueEmpty
    from tornado.util import TimeoutError

    async def test_get_nowait_returns_item():
        q = Queue()
        q.put_nowait(1)
        assert q.get_nowait() == 1

    async def test_get_nowait_empty_raises():
        q = Queue()
        try:
            q.get_nowait()
        except QueueEmpty:
            pass
        else:
            raise AssertionError("QueueEmpty was not raised")

    async def test_get_awaits_available_item():
        q = Queue()
        q.put_nowait("item")
        assert await q.get() == "item"

    async def test_get_unblocked_by_subsequent_put():
        q = Queue()
        fut = q.get()
        assert not fut.done()
        q.put_nowait(42)
        assert await fut == 42

    async def test_get_timeout_raises():
        q = Queue()
        try:
            await q.get(timeout=0.05)
        except TimeoutError:
            pass
        else:
            raise AssertionError("TimeoutError was not raised")

    async def test_get_timeout_timedelta_raises():
        q = Queue()
        try:
            await q.get(timeout=datetime.timedelta(seconds=0.05))
        except TimeoutError:
            pass
        else:
            raise AssertionError("TimeoutError was not raised")

    async def test_timed_out_getter_is_consumed():
        q = Queue()
        fut = q.get(timeout=0.05)
        try:
            await fut
        except TimeoutError:
            pass
        # The timed-out waiter must not steal the next item.
        q.put_nowait("x")
        assert await q.get() == "x"

    async def test_getters_served_in_fifo_order():
        q = Queue()
        f1 = q.get()
        f2 = q.get()
        q.put_nowait(1)
        q.put_nowait(2)
        assert await f1 == 1

# Generated at 2026-11-02 08:28:32.937284
# Unit test for method put of class Queue
def test_Queue_put():
    import datetime
    import unittest

    from tornado import gen
    from tornado.queues import Queue
    from tornado.testing import AsyncTestCase, gen_test

    class QueuePutTest(AsyncTestCase):
        @gen_test
        async def test_put_unbounded(self):
            q = Queue()
            for i in range(5):
                await q.put(i)
            self.assertEqual(q.qsize(), 5)
            self.assertFalse(q.empty())
            self.assertFalse(q.full())

        @gen_test
        async def test_put_until_full(self):
            q = Queue(maxsize=2)
            await q.put(1)
            await q.put(2)
            self.assertTrue(q.full())
            self.assertEqual(q.maxsize, 2)

        @gen_test
        async def test_put_blocks_when_full(self):
            q = Queue(maxsize=1)
            await q.put(0)
            done = []

            async def putter():
                await q.put(1)
                done.append(True)

            self.io_loop.spawn_callback(putter)
            await gen.sleep(0.05)
            self.assertEqual(done, [])
            self.assertEqual(await q.get(), 0)
            await gen.sleep(0.05)
            self.assertEqual(done, [True])
            self.assertEqual(q.qsize(), 1)

        @gen_test
        async def test_put_timeout(self):
            q = Queue(maxsize=1)
            await q.put(0)
            with self.assertRaises(gen.TimeoutError):
                await q.put(1, timeout=0.01)
            self.assertEqual(q.qsize(), 1)
            self.assertEqual(await q.get(), 0)

        @gen_test
        async def test_put_timeout_timedelta(self):
            q = Queue(maxsize=1)
            await q.put(0)
            with self.assertRaises(gen.TimeoutError):
                await q.put(1, timeout=datetime.timedelta(seconds=0.01))

        @gen_test
        async def test_put_resolves_when_space_frees(self):
            q = Queue(maxsize=1)
            await q.put(0)
            fut = q.put(1)
            self.assertFalse(fut.done())
            self.assertEqual(q.get_nowait(), 0)
            await gen.sleep(0.05)
            self.assertTrue(fut.done())
            self.assertEqual(q.qsize(), 1)
            self.assertEqual(q.get_nowait(), 1)

        @gen_test
        async def test_put_delivers_to_waiting_getter(self):
            q = Queue()
            getter = q.get()
            await gen.sleep(0.05)
            await q.put(42)
            self.assertEqual(await getter, 42)
            self.assertTrue(q.empty())

    loader = unittest.TestLoader()
    suite = unittest.TestSuite(loader.loadTestsFromTestCase(QueuePutTest))
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2026-11-02 08:30:25.257774
# Unit test for method empty of class Queue
def test_Queue_empty():
    # A newly created queue should be empty.
    q = Queue()
    assert q.empty() is True

    # After putting an item, the queue should not be empty.
    q.put_nowait(1)
    assert q.empty() is False

    # After removing the item, the queue should be empty again.
    item = q.get_nowait()
    assert item == 1
    assert q.empty() is True

    # maxsize should not affect the empty check.
    q2 = Queue(maxsize=3)
    assert q2.empty() is True
    q2.put_nowait("x")
    assert q2.empty() is False
    q2.get_nowait()
    assert q2.empty() is True

# Generated at 2026-11-02 08:32:34.283355
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.queues import Queue, QueueEmpty

    # Getting from an empty queue raises QueueEmpty
    q = Queue()
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # Items are returned in FIFO order
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.empty()

    # Empty again after draining
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # When the queue is full and a putter is waiting, get_nowait
    # resolves the putter's future and returns the buffered item.
    q = Queue(maxsize=1)
    q.put_nowait("a")
    put_future = q.put("b")  # queue full, putter registered
    assert not put_future.done()
    assert q.get_nowait() == "a"
    assert put_future.done()
    # The putter's item is now in the queue
    assert q.get_nowait() == "b"
    assert q.empty()

# Generated at 2026-11-02 08:33:44.858125
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import unittest
import datetime

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue, QueueFull, QueueEmpty


class TestQueuePutNowait(unittest.TestCase):
    def test_put_nowait_basic(self):
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        self.assertEqual(q.qsize(), 2)
        self.assertFalse(q.empty())
        self.assertEqual(q.get_nowait(), 1)
        self.assertEqual(q.get_nowait(), 2)

    def test_put_nowait_unbounded(self):
        q = Queue()
        for i in range(10):
            q.put_nowait(i)
        self.assertEqual(q.qsize(), 10)
        self.assertFalse(q.full())

    def test_put_nowait_full_raises(self):
        q = Queue(maxsize=1)
        q.put_nowait("a")
        self.assertTrue(q.full())
        with self.assertRaises(QueueFull):
            q.put_nowait("b")
        self.assertEqual(q.qsize(), 1)

    def test_put_nowait_after_consume(self):
        q = Queue(maxsize=2)
        q.put_nowait(1)
        q.put_nowait(2)
        with self.assertRaises(QueueFull):
            q.put_nowait(3)
        self.assertEqual(q.get_nowait(), 1)
        q.put_nowait(3)
        self.assertEqual(list(q._queue), [2, 3])

    def test_put_nowait_hands_off_to_waiting_getter(self):
        q = Queue()

        async def getter():
            return await q.get()

        async def main():
            fut = getter()
            await gen.sleep(0.01)
            q.put_nowait(42)
            self.assertEqual(await fut, 42)
            self.assertTrue(q.empty())

        IOLoop.current().run_sync(main)

    def test_put_nowait_hands_off_to_waiting_getter_full_queue(self):
        q = Queue(maxsize=1)
        q.put_nowait("x")

        async def getter():
            return await q.get()

        async def main():
            fut = getter()
            await gen.sleep(0.01)
            q.put_nowait("y")
            self.assertEqual(await fut, "x")
            self.assertEqual(q.get_nowait(), "y")

        IOLoop.current().run_sync(main)

    def test_put_nowait_marked_task_unfinished(self):
        q = Queue()
        q.put_nowait("task")
        self.assertEqual(q._unfinished_tasks, 1)
        self.assertFalse(q._finished.is_set())
        q.task_done()
        self.assertTrue(q._finished.is_set())

    def test_put_nowait_maxsize_zero_unbounded(self):
        q = Queue(maxsize=0)
        for i in range(100):
            q.put_nowait(i)
        self.assertFalse(q.full())
        self.assertEqual(q.qsize(), 100)

    def test_put_nowait_invalid_maxsize_none(self):
        with self.assertRaises(TypeError):
            Queue(maxsize=None)

    def test_put_nowait_invalid_maxsize_negative(self):
        with self.assertRaises(ValueError):
            Queue(maxsize=-1)

    def test_put_nowait_maxsize_property(self):
        q = Queue(maxsize=5)
        self.assertEqual(q.maxsize, 5)

    def test_put_nowait_expired_putters_consumed(self):
        q = Queue(maxsize=1)
        q.put_nowait(1)

        async def main():
            fut = q.put(2, timeout=0.01)
            await gen.sleep(0.05)
            self.assertTrue(fut.done())
            # Expired putter should be discarded, allowing a new put.
            with self.assertRaises(QueueFull):
                q.put_nowait(3)
            q.get_nowait()
            q.put_nowait(3)
            self.assertEqual(q.get_nowait(), 3)

        IOLoop.current().run_sync(main)


if __name__ == "__main__":
    unittest.main()