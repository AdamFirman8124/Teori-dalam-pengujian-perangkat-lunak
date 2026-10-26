

# Generated at 2026-10-25 07:46:51.748211
# Unit test for method full of class Queue
def test_Queue_full():
    # Unbounded queue (maxsize=0) is never full.
    q = Queue()
    assert not q.full()
    for i in range(100):
        q.put_nowait(i)
    assert not q.full()

    # Bounded queue fills up exactly at maxsize.
    q = Queue(maxsize=3)
    assert not q.full()          # empty
    q.put_nowait(0)
    assert not q.full()          # 1 < 3
    q.put_nowait(1)
    assert not q.full()          # 2 < 3
    q.put_nowait(2)
    assert q.full()              # 3 >= 3
    with pytest.raises(QueueFull):
        q.put_nowait(3)

    # Draining an item makes room again.
    assert q.get_nowait() == 0
    assert not q.full()

# Generated at 2026-10-25 07:47:03.652476
# Unit test for method __anext__ of class _QueueIterator
def test__QueueIterator___anext__():
    from unittest.mock import Mock

    queue = Mock()
    expected_awaitable = Mock()
    queue.get.return_value = expected_awaitable

    iterator = _QueueIterator(queue)
    result = iterator.__anext__()

    assert result is expected_awaitable
    queue.get.assert_called_once_with()

# Generated at 2026-10-25 07:47:06.070092
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 07:47:08.484001
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 07:47:10.896752
# Unit test for constructor of class _QueueIterator

# Generated at 2026-10-25 07:47:13.524171
# Unit test for constructor of class _QueueIterator

# Generated at 2026-10-25 07:47:15.937419
# Unit test for constructor of class _QueueIterator

# Generated at 2026-10-25 07:47:18.352063
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-25 07:47:20.766321
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-25 07:47:23.182899
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-25 07:47:25.594954
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:47:28.009110
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:47:30.425442
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:47:33.196239
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:47:35.611639
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:47:38.027025
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:47:40.510491
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:47:42.919835
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:47:45.305666
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:47:47.720742
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:47:50.134997
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:47:52.550399
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:47:54.966245
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:47:57.379617
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:47:59.794687
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:48:02.241624
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:48:04.660432
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:48:07.070765
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:48:09.484760
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:48:11.899019
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:48:14.315973
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:48:34.483173
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:48:41.136564
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-25 07:48:58.955673
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test() -> None:
        queue = Queue[str]()

        # module_0.get() returns an already-resolved awaitable when an item is available.
        queue.put_nowait("first")
        assert await queue.get() == "first"
        queue.task_done()

        # module_0.get() waits when the queue is empty and is resolved by a later put.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("second")
        assert await pending_get == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:49:00.388044
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 07:49:03.031179
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:49:05.593634
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:49:08.007687
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:49:10.421634
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:49:12.839934
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:49:15.253670
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:49:17.666336
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:49:20.080904
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:49:22.497556
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:49:24.915772
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:49:27.329052
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:49:29.742192
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:49:32.157695
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:49:37.336193
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-25 07:49:47.125658
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)

    # An empty queue raises QueueEmpty.
    try:
        q.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")

    # Items are returned immediately in FIFO order.
    q.put_nowait("first")
    q.put_nowait("second")
    assert q.get_nowait() == "first"
    assert q.get_nowait() == "second"
    assert q.empty()

    # Removing an item from a full queue admits the oldest waiting putter.
    q = Queue(maxsize=1)
    q.put_nowait("first")
    pending_put = q.put("second")

    assert not pending_put.done()
    assert q.get_nowait() == "first"
    assert pending_put.done()
    assert pending_put.result() is None
    assert q.get_nowait() == "second"

# Generated at 2026-10-25 07:50:05.312815
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

# Generated at 2026-10-25 07:50:16.780968
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # module_0.get() waits while the queue is empty.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("first")
        assert await pending_get == "first"
        queue.task_done()

        # module_0.get() resolves immediately when an item is available.
        queue.put_nowait("second")
        assert await queue.get() == "second"
        queue.task_done()

        # An empty queue respects relative timeouts.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=1))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # A timed-out getter must not consume later items.
        queue.put_nowait("third")
        assert await queue.get() == "third"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:50:19.443461
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:50:21.858581
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:50:24.274881
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:50:26.692996
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:50:29.110618
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:50:31.580798
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:50:37.055985
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():queue = Queue()

# Generated at 2026-10-25 07:50:38.487520
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

# Generated at 2026-10-25 07:50:39.921136
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

# Generated at 2026-10-25 07:50:41.457074
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

# Generated at 2026-10-25 07:50:52.775037
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # Getting from an empty queue waits until an item is available.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # Getting an already queued item completes immediately.
        await queue.put("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        queue.task_done()

        # A get from an empty queue respects its timeout.
        timed_get = queue.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The queue remains usable after a timed-out getter.
        await queue.put("third")
        assert await queue.get() == "third"
        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:50:54.565912
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 07:50:55.998978
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

# Generated at 2026-10-25 07:51:03.946519
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # An item already in the queue is returned immediately.
        queue.put_nowait("first")
        assert await queue.get() == "first"
        queue.task_done()

        # Getting from an empty queue waits until an item is added.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("second")
        assert await pending_get == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:51:12.037507
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Enqueue an item immediately.
    q = Queue(maxsize=1)
    q.put_nowait("first")

    assert q.qsize() == 1
    assert not q.empty()
    assert q.full()
    assert q.get_nowait() == "first"
    q.task_done()

    # A full queue must reject additional items without modifying the queue.
    q.put_nowait("first")
    try:
        q.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert q.qsize() == 1
    assert q.get_nowait() == "first"
    q.task_done()

    # If a getter is waiting, the item should be delivered directly to it.
    waiting_getter = q.get()
    assert not waiting_getter.done()

    q.put_nowait("direct")

    assert waiting_getter.done()
    assert waiting_getter.result() == "direct"
    assert q.empty()
    q.task_done()

    # Cancelled getters must be skipped.
    cancelled_getter = q.get()
    next_getter = q.get()
    cancelled_getter.cancel()

    q.put_nowait("next")

    assert next_getter.done()
    assert next_getter.result() == "next"
    assert q.empty()
    q.task_done()

# Generated at 2026-10-25 07:51:21.776028
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # module_0.get() waits while the queue is empty.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("first")
        assert await pending_get == "first"
        queue.task_done()

        # module_0.get() resolves immediately when an item is available.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

        # A waiting module_0.get() raises TimeoutError after its timeout.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:51:24.371232
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:51:26.993191
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:51:29.447627
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:51:31.865562
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:51:33.365472
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 07:51:41.873831
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # module_0.get() returns an already queued item.
        await queue.put("first")
        assert await queue.get() == "first"
        queue.task_done()

        # module_0.get() waits until a new item is available.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("second")
        assert await pending_get == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:51:53.343279
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # An item is added immediately when space is available.
    q = Queue(maxsize=1)
    q.put_nowait("first")

    assert q.qsize() == 1
    assert not q.empty()
    assert q.full()

    # Adding to a full queue fails without modifying the queue.
    try:
        q.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert q.qsize() == 1
    assert q.get_nowait() == "first"
    q.task_done()

    # A waiting getter receives the item directly.
    getter = q.get()
    assert not getter.done()

    q.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert q.empty()
    q.task_done()

    # Cancelled getters are discarded before the item is inserted.
    cancelled_getter = q.get()
    cancelled_getter.cancel()

    q.put_nowait("after-cancellation")

    assert q.qsize() == 1
    assert q.get_nowait() == "after-cancellation"
    q.task_done()
    assert q.join().done()

# Generated at 2026-10-25 07:52:03.404796
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=1)

    # An empty queue raises QueueEmpty.
    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() should raise QueueEmpty")

    queue.put_nowait("first")

    # A second put waits because the queue is full.
    pending_put = queue.put("second")
    assert not pending_put.done()

    # Getting the first item makes room for the waiting put.
    assert queue.get_nowait() == "first"
    assert pending_put.done()
    assert pending_put.result() is None

    # The waiting item is now available.
    assert queue.get_nowait() == "second"
    assert queue.empty()

    queue.task_done()
    queue.task_done()

# Generated at 2026-10-25 07:52:16.225282
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=1)

    with pytest.raises(QueueEmpty):
        queue.get_nowait()

    queue.put_nowait("first")
    blocked_put = queue.put("second")

    assert not blocked_put.done()
    assert queue.get_nowait() == "first"

    # Removing the first item makes room for the blocked putter.
    assert blocked_put.done()
    assert blocked_put.result() is None
    assert queue.get_nowait() == "second"
    assert queue.empty()

    with pytest.raises(QueueEmpty):
        queue.get_nowait()

    queue.task_done()
    queue.task_done()

# Generated at 2026-10-25 07:52:18.641307
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 07:52:21.211210
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 07:52:23.628916
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 07:52:26.179721
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:52:28.585383
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:52:31.002569
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:52:33.418686
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 07:52:35.834116
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 07:52:38.248372
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 07:52:40.661716
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:52:43.080399
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:52:45.509330
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:52:48.283462
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:52:49.868615
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 07:53:01.543409
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=2)

    # An empty queue raises QueueEmpty.
    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")

    # Items are returned immediately in FIFO order.
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.get_nowait() == "second"
    queue.task_done()
    assert queue.empty()

    # Removing an item from a full queue admits a waiting putter.
    queue = Queue(maxsize=1)
    queue.put_nowait("current")
    put_future = queue.put("waiting")

    assert not put_future.done()
    assert queue.get_nowait() == "current"
    queue.task_done()
    assert put_future.done()
    assert put_future.result() is None
    assert queue.get_nowait() == "waiting"
    queue.task_done()

# Generated at 2026-10-25 07:53:02.974354
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

# Generated at 2026-10-25 07:53:17.824338
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # An existing item is returned immediately.
        queue.put_nowait("first")
        assert await queue.get() == "first"
        queue.task_done()

        # module_0.get() waits until an item becomes available.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("second")
        assert await pending_get == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

        # Waiting for an item respects the timeout.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:53:30.847530
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=2)

    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.qsize() == 2
    assert queue.full()

    try:
        queue.put_nowait("third")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.get_nowait() == "second"
    queue.task_done()

    assert queue.empty()

    # An item should be delivered directly to an already-waiting getter.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-25 07:53:46.696770
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # An available item is returned immediately.
        queue.put_nowait("first")
        immediate = queue.get()
        assert isinstance(immediate, Future)
        assert immediate.done()
        assert await immediate == "first"
        queue.task_done()

        # An empty queue waits until an item is added.
        waiting = queue.get()
        assert isinstance(waiting, Future)
        assert not waiting.done()

        queue.put_nowait("second")
        assert await waiting == "second"
        queue.task_done()

        # A timed-out getter must not consume a subsequently added item.
        timed_out = queue.get(timeout=ioloop.IOLoop.current().time() - 1)
        try:
            await timed_out
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        queue.put_nowait("third")
        assert await queue.get() == "third"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:53:49.114288
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:53:51.786558
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 07:54:07.476331
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue[str]()

        # An available item is returned immediately.
        q.put_nowait("first")
        assert await q.get() == "first"
        q.task_done()

        # A get on an empty queue waits for a producer.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait("second")
        assert await pending_get == "second"
        q.task_done()

        # A waiting get raises TimeoutError when its timeout expires.
        try:
            await q.get(timeout=datetime.timedelta(milliseconds=1))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The expired getter must not consume a subsequently added item.
        q.put_nowait("third")
        assert await q.get() == "third"
        q.task_done()

        await q.join()
        assert q.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:54:09.012255
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 07:54:10.457474
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

# Generated at 2026-10-25 07:54:25.119564
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue(maxsize=1)

        # Getting from an empty queue waits until an item is available.
        pending_get = q.get()
        assert isinstance(pending_get, Future)
        assert not pending_get.done()

        await q.put("first")
        assert await pending_get == "first"
        q.task_done()

        # Getting an existing item also admits a blocked putter.
        await q.put("second")
        pending_put = q.put("third")
        assert not pending_put.done()

        assert await q.get() == "second"
        q.task_done()

        await pending_put
        assert await q.get() == "third"
        q.task_done()

        await q.join()
        assert q.empty()

        # A get on an empty queue honors relative timeouts.
        try:
            await q.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 07:54:26.526468
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 07:54:27.957528
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

# Generated at 2026-10-25 07:54:30.385555
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:54:32.923046
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:54:35.475700
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:54:37.894453
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:54:40.307620
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:54:42.873282
# Unit test for method put of class Queue

# Generated at 2026-10-25 07:54:45.288327
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:54:47.703232
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:54:50.118049
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:54:52.532131
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:54:54.946371
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:54:57.359411
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:54:58.865294
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

# Generated at 2026-10-25 07:55:15.278271
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import pytest

    queue = Queue(maxsize=2)

    # An empty queue raises QueueEmpty.
    with pytest.raises(QueueEmpty):
        queue.get_nowait()

    # Items are returned immediately in FIFO order.
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.get_nowait() == "second"
    queue.task_done()

    assert queue.empty()
    assert queue.join().done()

    # Removing an item from a full queue admits a waiting putter.
    bounded_queue = Queue(maxsize=1)
    bounded_queue.put_nowait(1)
    pending_put = bounded_queue.put(2)

    assert not pending_put.done()
    assert bounded_queue.get_nowait() == 1
    bounded_queue.task_done()

    assert pending_put.done()
    assert pending_put.result() is None
    assert bounded_queue.get_nowait() == 2
    bounded_queue.task_done()

    assert bounded_queue.empty()
    assert bounded_queue.join().done()

# Generated at 2026-10-25 07:55:16.653191
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

# Generated at 2026-10-25 07:55:26.746008
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # An item is added immediately when space is available.
    queue = Queue(maxsize=1)
    queue.put_nowait("first")

    assert queue.qsize() == 1
    assert queue.full()
    assert not queue.empty()

    # Adding another item to a full queue raises QueueFull and leaves the
    # existing item unchanged.
    try:
        queue.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.empty()
    assert queue.join().done()

    # A waiting getter receives the item directly.
    queue = Queue()
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-25 07:55:36.616856
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=1)

    # An empty queue raises QueueEmpty.
    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")

    # An available item is returned immediately.
    queue.put_nowait("first")
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.empty()

    # Removing an item makes room for the oldest waiting putter.
    queue.put_nowait("second")
    pending_put = queue.put("third")

    assert not pending_put.done()
    assert queue.get_nowait() == "second"
    assert pending_put.done()
    assert pending_put.result() is None

    assert queue.get_nowait() == "third"
    queue.task_done()
    queue.task_done()

    assert queue.empty()
    assert queue._unfinished_tasks == 0

# Generated at 2026-10-25 07:55:39.185088
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:55:41.818667
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:55:44.232523
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:55:46.646528
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:55:49.061987
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:55:51.477940
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 07:55:53.892826
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 07:55:56.306161
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 07:56:01.970667
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():queue = Queue(maxsize=1)

# Generated at 2026-10-25 07:56:18.042181
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Empty queues raise QueueEmpty.
    queue = Queue()
    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")

    # Available items are returned in FIFO order.
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.get_nowait() == "second"
    queue.task_done()
    assert queue.empty()

    # Removing an item from a full queue admits the first waiting putter.
    queue = Queue(maxsize=1)
    queue.put_nowait("current")
    putter = queue.put("waiting")

    assert not putter.done()
    assert queue.get_nowait() == "current"
    queue.task_done()
    assert putter.done()
    assert putter.result() is None
    assert queue.get_nowait() == "waiting"
    queue.task_done()

    # Cancelled putters are ignored.
    queue = Queue(maxsize=1)
    queue.put_nowait("kept")
    cancelled_putter = queue.put("discarded")
    assert cancelled_putter.cancel()

    assert queue.get_nowait() == "kept"
    queue.task_done()
    assert queue.empty()

# Generated at 2026-10-25 07:56:27.366638
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import pytest

    queue = Queue(maxsize=1)

    # An empty queue raises QueueEmpty.
    with pytest.raises(QueueEmpty):
        queue.get_nowait()

    queue.put_nowait("first")
    assert queue.qsize() == 1

    # Since the queue is full, this put must wait.
    pending_put = queue.put("second")
    assert not pending_put.done()

    # Retrieving the first item admits the waiting putter.
    assert queue.get_nowait() == "first"
    assert pending_put.done()
    assert pending_put.result() is None
    assert queue.qsize() == 1

    assert queue.get_nowait() == "second"
    assert queue.empty()

    # Both successfully enqueued items must be marked complete.
    queue.task_done()
    queue.task_done()

    with pytest.raises(QueueEmpty):
        queue.get_nowait()

# Generated at 2026-10-25 07:56:37.699497
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=1)

    # An empty queue raises QueueEmpty.
    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")

    # Available items are returned immediately in FIFO order.
    queue.put_nowait("first")
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.empty()

    # Removing an item from a full queue admits the next waiting putter.
    queue.put_nowait("second")
    pending_put = queue.put("third")

    assert not pending_put.done()
    assert queue.get_nowait() == "second"
    assert pending_put.done()
    assert pending_put.result() is None
    assert queue.get_nowait() == "third"

    queue.task_done()
    queue.task_done()
    assert queue.empty()

# Generated at 2026-10-25 07:56:43.395141
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:56:46.059653
# Unit test for method get of class Queue

# Generated at 2026-10-25 07:56:48.473945
# Unit test for method get of class Queue