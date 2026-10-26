

# Generated at 2026-10-25 08:25:41.780148
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=1)

    queue.put_nowait("item")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "item"
    assert queue.empty()

    queue.task_done()

    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() should raise QueueEmpty for an empty queue")

# Generated at 2026-10-25 08:25:46.533977
# Unit test for constructor of class QueueEmpty
def test_QueueEmpty():
    error = QueueEmpty()

    assert isinstance(error, QueueEmpty)
    assert isinstance(error, Exception)
    assert error.args == ()
    assert str(error) == ""

# Generated at 2026-10-25 08:25:47.918598
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

# Generated at 2026-10-25 08:25:59.271992
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    queue = Queue()
    queue.put_nowait("first")
    queue.put_nowait("second")

    joined = queue.join()
    assert not joined.done()

    assert queue.get_nowait() == "first"
    queue.task_done()
    assert not joined.done()

    assert queue.get_nowait() == "second"
    queue.task_done()
    assert joined.done()
    assert joined.result() is None

    try:
        queue.task_done()
    except ValueError as error:
        assert str(error) == "module_0.task_done() called too many times"
    else:
        raise AssertionError("module_0.task_done() should raise ValueError when over-called")

# Generated at 2026-10-25 08:26:07.899919
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Putting into an empty, unbounded queue succeeds immediately.
    q = Queue()
    q.put_nowait("item1")
    assert q.qsize() == 1
    assert not q.empty()
    assert not q.full()

    # Multiple puts accumulate.
    q.put_nowait("item2")
    assert q.qsize() == 2

    # Items come out in FIFO order.
    assert q.get_nowait() == "item1"
    assert q.get_nowait() == "item2"
    assert q.empty()

    # A bounded queue raises QueueFull once maxsize is reached.
    bounded = Queue(maxsize=2)
    bounded.put_nowait("a")
    bounded.put_nowait("b")
    assert bounded.full()
    with pytest.raises(QueueFull):
        bounded.put_nowait("c")
    assert bounded.qsize() == 2  # queue unchanged after failed put

    # maxsize=1 queue rejects the second put.
    single = Queue(maxsize=1)
    single.put_nowait("only")
    with pytest.raises(QueueFull):
        single.put_nowait("extra")

    # A waiting getter receives the item directly, queue stays empty,
    # and the putter slot is not consumed (nothing raises).
    q2 = Queue(maxsize=1)
    getter_future = q2.get()  # registers a waiting getter
    q2.put_nowait("direct")
    assert q2.empty()
    assert getter_future.done()
    assert getter_future.result() == "direct"

    # Putting into a queue that has a waiting getter but is full:
    # the item goes to the getter, not into the queue.
    q3 = Queue(maxsize=1)
    q3.put_nowait("held")
    blocked_getter = q3.get()  # queue is full, getter waits in _getters? No:
    # get_nowait succeeded above, so blocked_getter already resolved.
    assert blocked_getter.result() == "held"

    # Invalid maxsize values are rejected at construction.
    with pytest.raises(TypeError):
        Queue(maxsize=None)
    with pytest.raises(ValueError):
        Queue(maxsize=-1)

# Generated at 2026-10-25 08:26:17.739286
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
        assert isinstance(pending_get, Future)
        assert not pending_get.done()

        queue.put_nowait("second")

        assert await pending_get == "second"
        assert pending_get.done()
        queue.task_done()

        # All enqueued items have been processed.
        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 08:26:26.236781
# Unit test for constructor of class PriorityQueue
def test_PriorityQueue():
    # Default constructor: unbounded, empty
    q = PriorityQueue()
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()
    assert q._queue == []  # uses a list (heap), not a deque

    # Custom maxsize
    q2 = PriorityQueue(maxsize=3)
    assert q2.maxsize == 3
    assert q2.full() is False

    # Invalid arguments
    with pytest.raises(TypeError):
        PriorityQueue(maxsize=None)
    with pytest.raises(ValueError):
        PriorityQueue(maxsize=-1)

    # Constructor leaves the queue usable: heap ordering after puts
    q3 = PriorityQueue()
    q3.put_nowait((5, "low"))
    q3.put_nowait((1, "high"))
    q3.put_nowait((3, "mid"))
    assert q3.qsize() == 3
    assert q3.get_nowait() == (1, "high")
    assert q3.get_nowait() == (3, "mid")
    assert q3.get_nowait() == (5, "low")
    assert q3.empty()

# Generated at 2026-10-25 08:26:28.659665
# Unit test for constructor of class Queue

# Generated at 2026-10-25 08:26:31.077149
# Unit test for constructor of class Queue

# Generated at 2026-10-25 08:26:33.495442
# Unit test for constructor of class Queue

# Generated at 2026-10-25 08:26:35.910911
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:26:38.328358
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:26:40.747161
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:26:43.164431
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:26:45.582616
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:26:48.000125
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:26:50.417929
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:26:52.836004
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:26:55.255104
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-25 08:26:57.676026
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:27:00.097829
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:27:02.518586
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:27:04.943311
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:27:07.359866
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:27:12.729722
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-25 08:27:14.113681
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

# Generated at 2026-10-25 08:27:15.595555
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

# Generated at 2026-10-25 08:27:17.007500
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

# Generated at 2026-10-25 08:27:18.418935
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

# Generated at 2026-10-25 08:27:28.648507
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    queue = Queue()

    # An empty queue has no unfinished tasks.
    assert queue.join().done()

    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"

    joined = queue.join()
    assert not joined.done()

    # One unfinished task remains.
    queue.task_done()
    assert not joined.done()

    # Completing the final task releases join().
    queue.task_done()
    assert joined.done()
    assert joined.result() is None

    # module_0.task_done() cannot be called more times than items were put.
    try:
        queue.task_done()
    except ValueError as error:
        assert str(error) == "module_0.task_done() called too many times"
    else:
        raise AssertionError("Expected module_0.task_done() to raise ValueError")

# Generated at 2026-10-25 08:27:38.228059
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

    # Available items are returned in FIFO order.
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    queue.task_done()

    assert queue.get_nowait() == "second"
    queue.task_done()

    assert queue.empty()
    assert queue._unfinished_tasks == 0

# Generated at 2026-10-25 08:27:40.857360
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 08:27:43.277175
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 08:27:45.693151
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 08:27:48.110229
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:27:50.531792
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:27:52.946730
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:27:55.365643
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:27:57.780364
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:28:00.220067
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:28:02.638404
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:05.056744
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:07.474593
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:09.891315
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:12.310816
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:14.727012
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:17.145873
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:19.561721
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:21.976301
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:24.393494
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 08:28:26.812344
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 08:28:29.229222
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 08:28:31.645249
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:34.064771
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:36.483732
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:38.956527
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:28:41.357041
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:28:43.774604
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:28:46.192949
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:28:48.609829
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:28:51.029260
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:28:53.447264
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:55.864445
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:28:58.282670
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:29:01.453276
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:29:09.156419
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-25 08:29:19.399415
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is inserted immediately when space is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()

    # Inserting into a full queue raises without modifying the queue.
    with pytest.raises(QueueFull):
        queue.put_nowait("second")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.join().done()

    # A waiting getter receives the item directly.
    waiting_queue = Queue()
    getter = waiting_queue.get()
    assert not getter.done()

    waiting_queue.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert waiting_queue.empty()

    waiting_queue.task_done()
    assert waiting_queue.join().done()

# Generated at 2026-10-25 08:29:22.059096
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:29:24.629895
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:29:27.045118
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:29:29.462408
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 08:29:31.883671
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 08:29:34.419119
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 08:29:36.834383
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:29:39.300366
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:29:41.681994
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:29:44.982019
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:29:47.397342
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:29:49.812701
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:29:52.228378
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:29:54.644977
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:29:57.061597
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:29:59.479912
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:30:01.897841
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:30:04.315002
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:30:06.730421
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:30:08.294518
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 08:30:09.722873
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

# Generated at 2026-10-25 08:30:11.315285
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

# Generated at 2026-10-25 08:30:12.753396
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

# Generated at 2026-10-25 08:30:24.062038
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 08:30:25.443816
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 08:30:26.878135
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

# Generated at 2026-10-25 08:30:28.270270
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 08:30:29.643018
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 08:30:31.692932
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

# Generated at 2026-10-25 08:30:33.173323
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

# Generated at 2026-10-25 08:30:34.660229
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

# Generated at 2026-10-25 08:30:35.992408
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 08:30:37.476479
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 08:30:38.971658
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

# Generated at 2026-10-25 08:30:41.525668
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:30:44.051246
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:30:46.464038
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:30:48.880798
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:30:51.499471
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:30:53.918640
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:30:56.562712
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:30:59.009038
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:31:01.398620
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:31:03.813471
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:31:06.231745
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:31:08.646282
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:31:11.064574
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:31:13.672418
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 08:31:15.267397
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # 2. Basic FIFO + qsize / empty bookkeeping
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.qsize() == 3
    assert not q.empty()

    assert q.get_nowait() == 1
    assert q.qsize() == 2
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    assert q.empty()

    try:
        q.get_nowait()
        assert False, "expected QueueEmpty after drain"
    except QueueEmpty:
        pass

    # 3. Full queue with blocked putter: get_nowait hands off
    q2: Queue[str] = Queue(maxsize=1)
    q2.put_nowait("a")
    assert q2.full()

    putter_fut = q2.put("b")  # queues in _putters, not done
    assert len(q2._putters) == 1
    assert not putter_fut.done()

    # Should return oldest item "a", admit "b", resolve putter
    assert q2.get_nowait() == "a"
    assert putter_fut.done()
    assert putter_fut.result() is None
    assert q2.qsize() == 1
    assert q2.full()

    # Remaining item is the handed-off one
    assert q2.get_nowait() == "b"
    assert q2.empty()

    # 4. Expired/cancelled putters are skipped by _consume_expired
    q3: Queue[str] = Queue(maxsize=1)
    q3.put_nowait("x")

# Generated at 2026-10-25 08:31:16.748901
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

# Generated at 2026-10-25 08:31:33.597300
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # 2. Basic FIFO + qsize / empty bookkeeping
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.qsize() == 3
    assert not q.empty()

    assert q.get_nowait() == 1
    assert q.qsize() == 2
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    assert q.empty()

    try:
        q.get_nowait()
        assert False, "expected QueueEmpty after drain"
    except QueueEmpty:
        pass

    # 3. Full queue with blocked putter: get_nowait hands off
    q2: Queue[str] = Queue(maxsize=1)
    q2.put_nowait("a")
    assert q2.full()

    putter_fut = q2.put("b")  # queues in _putters, not done
    assert len(q2._putters) == 1
    assert not putter_fut.done()

    # Should return oldest item "a", admit "b", resolve putter
    assert q2.get_nowait() == "a"
    assert putter_fut.done()
    assert putter_fut.result() is None
    assert q2.qsize() == 1
    assert q2.full()

    # Remaining item is the handed-off one
    assert q2.get_nowait() == "b"
    assert q2.empty()

    # 4. Expired/cancelled putters are skipped by _consume_expired
    q3: Queue[str] = Queue(maxsize=1)
    q3.put_nowait("x")

# Generated at 2026-10-25 08:31:35.288820
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 08:31:36.619625
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 08:31:38.579503
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # 2. Basic FIFO + qsize / empty bookkeeping
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.qsize() == 3
    assert not q.empty()

    assert q.get_nowait() == 1
    assert q.qsize() == 2
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    assert q.empty()

    try:
        q.get_nowait()
        assert False, "expected QueueEmpty after drain"
    except QueueEmpty:
        pass

    # 3. Full queue with blocked putter: get_nowait hands off
    q2: Queue[str] = Queue(maxsize=1)
    q2.put_nowait("a")
    assert q2.full()

    putter_fut = q2.put("b")  # queues in _putters, not done
    assert len(q2._putters) == 1
    assert not putter_fut.done()

    # Should return oldest item "a", admit "b", resolve putter
    assert q2.get_nowait() == "a"
    assert putter_fut.done()
    assert putter_fut.result() is None
    assert q2.qsize() == 1
    assert q2.full()

    # Remaining item is the handed-off one
    assert q2.get_nowait() == "b"
    assert q2.empty()

    # 4. Expired/cancelled putters are skipped by _consume_expired
    q3: Queue[str] = Queue(maxsize=1)
    q3.put_nowait("x")

# Generated at 2026-10-25 08:31:40.035973
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

# Generated at 2026-10-25 08:31:41.566717
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

# Generated at 2026-10-25 08:31:43.049996
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

# Generated at 2026-10-25 08:31:45.622099
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:31:48.040307
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:31:50.455183
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:31:52.872672
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:31:55.327957
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:31:57.745054
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:32:03.244542
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:05.662094
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:08.079236
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:10.497426
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:12.912507
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:15.467505
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:17.788178
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:32:20.205470
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:32:22.621164
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:32:25.040322
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:27.464045
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:29.875841
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:32.293072
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:34.709830
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:37.329310
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:32:39.735249
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:32:42.151315
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:32:43.581421
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 08:32:45.121538
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 08:32:46.625401
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 08:33:13.287035
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Putting into an empty, unbounded queue succeeds immediately.
    q = Queue()
    q.put_nowait("item1")
    assert q.qsize() == 1
    assert not q.empty()
    assert not q.full()

    # Multiple puts accumulate.
    q.put_nowait("item2")
    assert q.qsize() == 2

    # Items come out in FIFO order.
    assert q.get_nowait() == "item1"
    assert q.get_nowait() == "item2"
    assert q.empty()

    # A bounded queue raises QueueFull once maxsize is reached.
    bounded = Queue(maxsize=2)
    bounded.put_nowait("a")
    bounded.put_nowait("b")
    assert bounded.full()
    with pytest.raises(QueueFull):
        bounded.put_nowait("c")
    assert bounded.qsize() == 2  # queue unchanged after failed put

    # maxsize=1 queue rejects the second put.
    single = Queue(maxsize=1)
    single.put_nowait("only")
    with pytest.raises(QueueFull):
        single.put_nowait("extra")

    # A waiting getter receives the item directly, queue stays empty,
    # and the putter slot is not consumed (nothing raises).
    q2 = Queue(maxsize=1)
    getter_future = q2.get()  # registers a waiting getter
    q2.put_nowait("direct")
    assert q2.empty()
    assert getter_future.done()
    assert getter_future.result() == "direct"

    # Putting into a queue that has a waiting getter but is full:
    # the item goes to the getter, not into the queue.
    q3 = Queue(maxsize=1)
    q3.put_nowait("held")
    blocked_getter = q3.get()  # queue is full, getter waits in _getters? No:
    # get_nowait succeeded above, so blocked_getter already resolved.
    assert blocked_getter.result() == "held"

    # Invalid maxsize values are rejected at construction.
    with pytest.raises(TypeError):
        Queue(maxsize=None)
    with pytest.raises(ValueError):
        Queue(maxsize=-1)

# Generated at 2026-10-25 08:33:14.717641
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

# Generated at 2026-10-25 08:33:17.579708
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # 2. Basic FIFO + qsize / empty bookkeeping
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.qsize() == 3
    assert not q.empty()

    assert q.get_nowait() == 1
    assert q.qsize() == 2
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    assert q.empty()

    try:
        q.get_nowait()
        assert False, "expected QueueEmpty after drain"
    except QueueEmpty:
        pass

    # 3. Full queue with blocked putter: get_nowait hands off
    q2: Queue[str] = Queue(maxsize=1)
    q2.put_nowait("a")
    assert q2.full()

    putter_fut = q2.put("b")  # queues in _putters, not done
    assert len(q2._putters) == 1
    assert not putter_fut.done()

    # Should return oldest item "a", admit "b", resolve putter
    assert q2.get_nowait() == "a"
    assert putter_fut.done()
    assert putter_fut.result() is None
    assert q2.qsize() == 1
    assert q2.full()

    # Remaining item is the handed-off one
    assert q2.get_nowait() == "b"
    assert q2.empty()

    # 4. Expired/cancelled putters are skipped by _consume_expired
    q3: Queue[str] = Queue(maxsize=1)
    q3.put_nowait("x")

# Generated at 2026-10-25 08:33:21.424561
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:33:23.994587
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:33:26.412121
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:33:28.947412
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:33:31.361359
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:33:33.791634
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:33:36.203130
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:33:38.625588
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:33:41.041839
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:33:43.458140
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:33:46.072362
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 08:33:48.837812
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Putting into an empty, unbounded queue succeeds immediately.
    q = Queue()
    q.put_nowait("item1")
    assert q.qsize() == 1
    assert not q.empty()
    assert not q.full()

    # Multiple puts accumulate.
    q.put_nowait("item2")
    assert q.qsize() == 2

    # Items come out in FIFO order.
    assert q.get_nowait() == "item1"
    assert q.get_nowait() == "item2"
    assert q.empty()

    # A bounded queue raises QueueFull once maxsize is reached.
    bounded = Queue(maxsize=2)
    bounded.put_nowait("a")
    bounded.put_nowait("b")
    assert bounded.full()
    with pytest.raises(QueueFull):
        bounded.put_nowait("c")
    assert bounded.qsize() == 2  # queue unchanged after failed put

    # maxsize=1 queue rejects the second put.
    single = Queue(maxsize=1)
    single.put_nowait("only")
    with pytest.raises(QueueFull):
        single.put_nowait("extra")

    # A waiting getter receives the item directly, queue stays empty,
    # and the putter slot is not consumed (nothing raises).
    q2 = Queue(maxsize=1)
    getter_future = q2.get()  # registers a waiting getter
    q2.put_nowait("direct")
    assert q2.empty()
    assert getter_future.done()
    assert getter_future.result() == "direct"

    # Putting into a queue that has a waiting getter but is full:
    # the item goes to the getter, not into the queue.
    q3 = Queue(maxsize=1)
    q3.put_nowait("held")
    blocked_getter = q3.get()  # queue is full, getter waits in _getters? No:
    # get_nowait succeeded above, so blocked_getter already resolved.
    assert blocked_getter.result() == "held"

    # Invalid maxsize values are rejected at construction.
    with pytest.raises(TypeError):
        Queue(maxsize=None)
    with pytest.raises(ValueError):
        Queue(maxsize=-1)

# Generated at 2026-10-25 08:33:51.605424
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Putting into an empty, unbounded queue succeeds immediately.
    q = Queue()
    q.put_nowait("item1")
    assert q.qsize() == 1
    assert not q.empty()
    assert not q.full()

    # Multiple puts accumulate.
    q.put_nowait("item2")
    assert q.qsize() == 2

    # Items come out in FIFO order.
    assert q.get_nowait() == "item1"
    assert q.get_nowait() == "item2"
    assert q.empty()

    # A bounded queue raises QueueFull once maxsize is reached.
    bounded = Queue(maxsize=2)
    bounded.put_nowait("a")
    bounded.put_nowait("b")
    assert bounded.full()
    with pytest.raises(QueueFull):
        bounded.put_nowait("c")
    assert bounded.qsize() == 2  # queue unchanged after failed put

    # maxsize=1 queue rejects the second put.
    single = Queue(maxsize=1)
    single.put_nowait("only")
    with pytest.raises(QueueFull):
        single.put_nowait("extra")

    # A waiting getter receives the item directly, queue stays empty,
    # and the putter slot is not consumed (nothing raises).
    q2 = Queue(maxsize=1)
    getter_future = q2.get()  # registers a waiting getter
    q2.put_nowait("direct")
    assert q2.empty()
    assert getter_future.done()
    assert getter_future.result() == "direct"

    # Putting into a queue that has a waiting getter but is full:
    # the item goes to the getter, not into the queue.
    q3 = Queue(maxsize=1)
    q3.put_nowait("held")
    blocked_getter = q3.get()  # queue is full, getter waits in _getters? No:
    # get_nowait succeeded above, so blocked_getter already resolved.
    assert blocked_getter.result() == "held"

    # Invalid maxsize values are rejected at construction.
    with pytest.raises(TypeError):
        Queue(maxsize=None)
    with pytest.raises(ValueError):
        Queue(maxsize=-1)

# Generated at 2026-10-25 08:33:52.984912
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

# Generated at 2026-10-25 08:33:55.880590
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Putting into an empty, unbounded queue succeeds immediately.
    q = Queue()
    q.put_nowait("item1")
    assert q.qsize() == 1
    assert not q.empty()
    assert not q.full()

    # Multiple puts accumulate.
    q.put_nowait("item2")
    assert q.qsize() == 2

    # Items come out in FIFO order.
    assert q.get_nowait() == "item1"
    assert q.get_nowait() == "item2"
    assert q.empty()

    # A bounded queue raises QueueFull once maxsize is reached.
    bounded = Queue(maxsize=2)
    bounded.put_nowait("a")
    bounded.put_nowait("b")
    assert bounded.full()
    with pytest.raises(QueueFull):
        bounded.put_nowait("c")
    assert bounded.qsize() == 2  # queue unchanged after failed put

    # maxsize=1 queue rejects the second put.
    single = Queue(maxsize=1)
    single.put_nowait("only")
    with pytest.raises(QueueFull):
        single.put_nowait("extra")

    # A waiting getter receives the item directly, queue stays empty,
    # and the putter slot is not consumed (nothing raises).
    q2 = Queue(maxsize=1)
    getter_future = q2.get()  # registers a waiting getter
    q2.put_nowait("direct")
    assert q2.empty()
    assert getter_future.done()
    assert getter_future.result() == "direct"

    # Putting into a queue that has a waiting getter but is full:
    # the item goes to the getter, not into the queue.
    q3 = Queue(maxsize=1)
    q3.put_nowait("held")
    blocked_getter = q3.get()  # queue is full, getter waits in _getters? No:
    # get_nowait succeeded above, so blocked_getter already resolved.
    assert blocked_getter.result() == "held"

    # Invalid maxsize values are rejected at construction.
    with pytest.raises(TypeError):
        Queue(maxsize=None)
    with pytest.raises(ValueError):
        Queue(maxsize=-1)

# Generated at 2026-10-25 08:33:59.024970
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Putting into an empty, unbounded queue succeeds immediately.
    q = Queue()
    q.put_nowait("item1")
    assert q.qsize() == 1
    assert not q.empty()
    assert not q.full()

    # Multiple puts accumulate.
    q.put_nowait("item2")
    assert q.qsize() == 2

    # Items come out in FIFO order.
    assert q.get_nowait() == "item1"
    assert q.get_nowait() == "item2"
    assert q.empty()

    # A bounded queue raises QueueFull once maxsize is reached.
    bounded = Queue(maxsize=2)
    bounded.put_nowait("a")
    bounded.put_nowait("b")
    assert bounded.full()
    with pytest.raises(QueueFull):
        bounded.put_nowait("c")
    assert bounded.qsize() == 2  # queue unchanged after failed put

    # maxsize=1 queue rejects the second put.
    single = Queue(maxsize=1)
    single.put_nowait("only")
    with pytest.raises(QueueFull):
        single.put_nowait("extra")

    # A waiting getter receives the item directly, queue stays empty,
    # and the putter slot is not consumed (nothing raises).
    q2 = Queue(maxsize=1)
    getter_future = q2.get()  # registers a waiting getter
    q2.put_nowait("direct")
    assert q2.empty()
    assert getter_future.done()
    assert getter_future.result() == "direct"

    # Putting into a queue that has a waiting getter but is full:
    # the item goes to the getter, not into the queue.
    q3 = Queue(maxsize=1)
    q3.put_nowait("held")
    blocked_getter = q3.get()  # queue is full, getter waits in _getters? No:
    # get_nowait succeeded above, so blocked_getter already resolved.
    assert blocked_getter.result() == "held"

    # Invalid maxsize values are rejected at construction.
    with pytest.raises(TypeError):
        Queue(maxsize=None)
    with pytest.raises(ValueError):
        Queue(maxsize=-1)

# Generated at 2026-10-25 08:34:00.592550
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 08:34:01.945609
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 08:34:05.899972
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:34:08.537651
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:34:11.185523
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 08:34:13.788064
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:34:16.207415
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:34:18.624617
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:34:21.210355
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:34:23.625634
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:34:26.043523
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:34:28.459663
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:34:30.877070
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:34:33.296461
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:34:35.716023
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:34:38.131594
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:34:40.548438
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:34:42.963625
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:34:45.384378
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:34:47.806895
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:34:50.223448
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:34:52.640410
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:34:55.058101
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:34:57.475094
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:34:59.893031
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:35:02.309166
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 08:35:04.730348
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:35:07.148211
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:35:09.568381
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:35:17.170995
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

# Generated at 2026-10-25 08:35:22.672769
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 08:35:24.007208
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 08:35:25.358174
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 08:35:27.783521
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:35:30.198581
# Unit test for method get of class Queue

# Generated at 2026-10-25 08:35:32.614120
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:35:35.031486
# Unit test for method put of class Queue

# Generated at 2026-10-25 08:35:37.450266
# Unit test for method put of class Queue