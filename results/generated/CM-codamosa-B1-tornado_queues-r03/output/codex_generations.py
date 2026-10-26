

# Generated at 2026-10-25 08:47:14.706562
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 08:47:34.571529
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 08:47:50.953427
# Unit test for method __anext__ of class _QueueIterator
def test__QueueIterator___anext__():from tornado.queues import Queue, _QueueIterator

# Generated at 2026-10-25 08:47:52.587535
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():import unittest

from tornado.queues import Queue, QueueEmpty


class QueueGetNowaitTest(unittest.AsyncTestCase):
    async def test_get_nowait_empty_raises(self):
        q = Queue()
        with self.assertRaises(QueueEmpty):
            q.get_nowait()

    async def test_get_nowait_returns_item(self):
        q = Queue()
        q.put_nowait("item")
        self.assertEqual(q.get_nowait(), "item")

    async def test_get_nowait_fifo_order(self):
        q = Queue()
        for i in range(3):
            q.put_nowait(i)
        self.assertEqual([q.get_nowait() for _ in range(3)], [0, 1, 2])
        with self.assertRaises(QueueEmpty):
            q.get_nowait()

    async def test_get_nowait_resolves_waiting_putter(self):
        # A putter blocked on a full queue is unblocked by get_nowait.
        q = Queue(maxsize=1)
        q.put_nowait(1)
        putter_future = q.put(2)  # blocks: queue full
        self.assertFalse(putter_future.done())

        item = q.get_nowait()
        self.assertEqual(item, 1)
        self.assertTrue(putter_future.done())  # putter unblocked
        self.assertEqual(q.get_nowait(), 2)  # putter's item now retrievable

    async def test_get_nowait_skips_expired_getters_and_putters(self):
        # Timed-out waiters are discarded, not handed items.
        q = Queue()
        stale_getter = q.get(timeout=0.01)
        await gen.sleep(0.05)
        self.assertTrue(stale_getter.done())  # timed out

        q.put_nowait("fresh")
        self.assertEqual(q.get_nowait(), "fresh")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-10-25 08:47:53.977732
# Unit test for method put of class Queue
def test_Queue_put():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def body():
        # 1. Unbounded queue: module_0.put() resolves immediately.
        q = Queue()
        f = q.put(1)
        assert f.done()
        assert await f is None
        assert q.qsize() == 1
        assert q._unfinished_tasks == 1

        # 2. Bounded queue: fill to maxsize, next module_0.put() blocks.
        q2 = Queue(maxsize=1)
        await q2.put("a")
        assert q2.full()
        assert q2.qsize() == 1

        blocked = q2.put("b")
        assert not blocked.done()
        assert len(q2._putters) == 1
        assert q2.qsize() == 1  # blocked item not in queue yet

        # get() unblocks the putter in FIFO order.
        assert await q2.get() == "a"
        await blocked  # must now succeed
        assert blocked.done()
        assert blocked.result() is None
        assert q2

# Generated at 2026-10-25 08:48:32.831943
# Unit test for method join of class Queue
def test_Queue_join():
    import asyncio
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def run_test():
        # 1. module_0.join() on an empty (already finished) queue returns immediately.
        q = Queue()
        assert q._finished.is_set()
        await q.join()

        # 2. module_0.join() blocks until all put items are consumed and task_done() is called.
        results = []
        for item in range(3):
            q.put_nowait(item)
        assert not q._finished.is_set(), "queue should not be finished with pending tasks"

        async def consumer():
            while True:
                item = await q.get()
                await gen.sleep(0.01)
                q.task_done()
                results.append(item)

        IOLoop.current().spawn_callback(consumer)
        await q.join(timeout=5)
        assert results == [0, 1, 2], "consumer processed items out of order: %r" % results
        assert q._finished.is_set(), "queue should be finished after all task_done() calls"

        # 3. module_0.join() with a timeout raises TimeoutError when tasks are never finished.
        q2 = Queue()
        q2.put_nowait("never processed")
        try:
            await q2.join(timeout=0.05)
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("expected TimeoutError from module_0.join() with pending tasks")

        # 4. task_done() called more times than put() raises ValueError.
        try:
            q2.task_done()
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError from extra task_done()")

    IOLoop.run_sync(run_test)

# Generated at 2026-10-25 08:48:42.464356
# Unit test for method empty of class Queue
def test_Queue_empty():
    q = Queue()
    # New queue is empty
    assert q.empty() is True

    # Non-empty after put
    q.put_nowait(1)
    assert q.empty() is False

    # Empty again after removing item
    q.get_nowait()
    assert q.empty() is True

    # Multiple items
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.empty() is False
    q.get_nowait()
    assert q.empty() is False
    q.get_nowait()
    assert q.empty() is True

# Generated at 2026-10-25 08:48:45.085607
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:48:47.505276
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:48:50.129527
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:48:52.549562
# Unit test for method full of class Queue

# Generated at 2026-10-25 08:48:54.963285
# Unit test for method full of class Queue

# Generated at 2026-10-25 08:48:57.710974
# Unit test for method full of class Queue

# Generated at 2026-10-25 08:49:00.064383
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:49:02.486074
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:49:04.903642
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:49:07.320266
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:09.769651
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:12.189025
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:14.607190
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:49:17.020464
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:49:19.436709
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:49:21.857371
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:49:24.272259
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:49:26.686062
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:49:29.104963
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:31.520262
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:33.937982
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:36.356508
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:49:38.771244
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:49:41.188883
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:49:43.606394
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:46.022414
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:48.436600
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:50.854566
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:53.274734
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:55.818313
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:49:58.237383
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:00.657495
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:03.077437
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:05.495037
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:50:07.911642
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:50:10.332489
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:50:12.751349
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:50:15.170916
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:50:17.587953
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:50:20.006696
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:22.421459
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:24.858685
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:27.280381
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-25 08:50:29.706610
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-25 08:50:32.124719
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-25 08:50:34.544442
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-25 08:50:37.132456
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-25 08:50:39.379924
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-25 08:50:41.793297
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:50:44.209651
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:50:46.625001
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:50:49.041381
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:51.456480
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:53.869882
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:56.286297
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:50:58.708352
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:51:01.125634
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:51:03.544391
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:51:23.638998
# Unit test for constructor of class LifoQueue
def test_LifoQueue():q = LifoQueue(maxsize=5)

# Generated at 2026-10-25 08:51:57.945168
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():q = Queue(maxsize=1)

q.put_nowait("first")
assert q.qsize() == 1
assert not q.empty()
assert q.full()
assert q.get_nowait() == "first"
assert q.empty()

try:
    q.put_nowait("second")
except QueueFull:
    pass
else:
    raise AssertionError("module_0.put_nowait() did not raise QueueFull")

getter = q.get()
assert not getter.done()

q.put_nowait("delivered")
assert getter.done()
assert getter.result() == "delivered"
assert q.empty()

q.task_done()
assert q._unfinished_tasks == 0

# Generated at 2026-10-25 08:52:00.712495
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:52:03.130233
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:52:05.548438
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:52:07.966739
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:52:10.385513
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:52:12.800564
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:52:15.221862
# Unit test for constructor of class Queue

# Generated at 2026-10-25 08:52:17.635305
# Unit test for constructor of class Queue

# Generated at 2026-10-25 08:52:29.980837
# Unit test for constructor of class Queue
def test_Queue():from tornado.queues import Queue

# Generated at 2026-10-25 08:52:31.430010
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 08:52:32.863435
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 08:52:48.017957
# Unit test for constructor of class Queue
def test_Queue():
    # default: unbounded queue
    q = Queue()
    assert q.maxsize == 0
    assert q._maxsize == 0
    assert isinstance(q._queue, collections.deque)
    assert len(q._queue) == 0
    assert isinstance(q._getters, collections.deque)
    assert len(q._getters) == 0
    assert isinstance(q._putters, collections.deque)
    assert len(q._putters) == 0
    assert q._unfinished_tasks == 0
    assert isinstance(q._finished, Event)
    assert q._finished.is_set()
    assert q.qsize() == 0
    assert q.empty() is True
    assert q.full() is False

    # explicit maxsize=0 is also unbounded
    q0 = Queue(maxsize=0)
    assert q0.maxsize == 0
    assert q0.empty() is True
    assert q0.full() is False

    # positive maxsize is stored and reported
    q2 = Queue(maxsize=2)
    assert q2.maxsize == 2
    assert q2.qsize() == 0
    assert q2.empty() is True
    assert q2.full() is False
    assert q2._unfinished_tasks == 0
    assert q2._finished.is_set()

    # each instance gets independent state
    q3 = Queue(maxsize=5)
    assert q3.maxsize == 5
    assert q3._queue is not q2._queue
    assert q3._getters is not q2._getters
    assert q3._putters is not q2._putters
    assert q3._finished is not q2._finished

    # maxsize=None is rejected
    with pytest.raises(TypeError, match="maxsize can't be None"):
        Queue(maxsize=None)

    # negative maxsize is rejected
    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-1)

    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-100)

# Generated at 2026-10-25 08:52:50.590256
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:52:53.009080
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:52:55.424888
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:52:57.846828
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:53:00.265671
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:53:02.683165
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:53:05.102024
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-25 08:53:07.517814
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-25 08:53:09.937059
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-25 08:53:12.353789
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:53:14.771889
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:53:17.189921
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:53:19.609600
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:53:22.026257
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:53:24.442578
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:53:26.859227
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:53:29.276113
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:53:31.697538
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:53:34.111190
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:53:49.746614
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import pytest

# Generated at 2026-10-25 08:53:52.743135
# Unit test for method put of class Queue
def test_Queue_put():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def body():
        # 1. Unbounded queue: module_0.put() resolves immediately.
        q = Queue()
        f = q.put(1)
        assert f.done()
        assert await f is None
        assert q.qsize() == 1
        assert q._unfinished_tasks == 1

        # 2. Bounded queue: fill to maxsize, next module_0.put() blocks.
        q2 = Queue(maxsize=1)
        await q2.put("a")
        assert q2.full()
        assert q2.qsize() == 1

        blocked = q2.put("b")
        assert not blocked.done()
        assert len(q2._putters) == 1
        assert q2.qsize() == 1  # blocked item not in queue yet

        # get() unblocks the putter in FIFO order.
        assert await q2.get() == "a"
        await blocked  # must now succeed
        assert blocked.done()
        assert blocked.result() is None
        assert q2

# Generated at 2026-10-25 08:54:10.552531
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():q = Queue(maxsize=1)

q.put_nowait("first")
assert q.qsize() == 1
assert q.full()
assert not q.empty()

try:
    q.put_nowait("second")
except QueueFull:
    pass
else:
    raise AssertionError("module_0.put_nowait() did not raise QueueFull")

assert q.get_nowait() == "first"
q.task_done()
assert q.empty()

q.put_nowait("second")
assert q.get_nowait() == "second"
q.task_done()

waiting = Queue()
future = waiting.get()
waiting.put_nowait(42)

assert future.done()
assert future.result() == 42
assert waiting.empty()
waiting.task_done()

# Generated at 2026-10-25 08:54:12.971154
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:54:15.389001
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:54:18.136240
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:54:20.554465
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:54:22.974672
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:54:25.390014
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:54:27.807682
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:54:30.228273
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:54:32.643159
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:54:35.060354
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:54:37.475972
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:54:39.892182
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:55:11.378744
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 08:55:14.013447
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:55:16.432263
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:55:18.849993
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:55:21.266528
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:55:23.683263
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:55:26.101882
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:55:28.517265
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:55:30.933546
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:55:33.351812
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:55:35.766915
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:55:38.185008
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:55:40.605569
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:55:43.030585
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:55:45.439262
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:55:47.916015
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:55:50.335031
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:55:52.751378
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:55:55.168430
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:55:57.583460
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:56:00.000782
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:56:02.419739
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:56:04.834762
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:56:07.253867
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:56:09.671644
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:56:12.091229
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:56:14.507636
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:56:16.921331
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:56:19.346825
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:56:21.757766
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:56:24.177749
# Unit test for method get of class Queue