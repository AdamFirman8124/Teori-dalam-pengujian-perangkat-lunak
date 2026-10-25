

# Generated at 2026-10-25 00:44:43.008405
# Unit test for constructor of class PriorityQueue
def test_PriorityQueue():
    # 1. Default constructor
    q = PriorityQueue()
    assert isinstance(q, Queue)
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty() is True
    assert q.full() is False
    assert q._queue == []
    assert isinstance(q._queue, list)
    assert q._unfinished_tasks == 0
    assert len(q._getters) == 0
    assert len(q._putters) == 0

    # 2. Custom maxsize
    q2 = PriorityQueue(maxsize=3)
    assert q2.maxsize == 3
    assert q2.empty() is True
    assert q2.full() is False
    assert q2._queue == []

    # maxsize=1 boundary for full()
    q3 = PriorityQueue(maxsize=1)
    assert q3.maxsize == 1
    assert q3.full() is False

    # 3. Each instance gets independent storage
    q4 = PriorityQueue()
    q5 = PriorityQueue()
    assert q4._queue is not q5._queue

    # 4. maxsize=None must raise TypeError
    try:
        PriorityQueue(maxsize=None)
        assert False, "expected TypeError for maxsize=None"
    except TypeError as e:
        assert "maxsize can't be None" in str(e)

    # 5. Negative maxsize must raise ValueError
    try:
        PriorityQueue(maxsize=-1)
        assert False, "expected ValueError for negative maxsize"
    except ValueError as e:
        assert "maxsize can't be negative" in str(e)

# Generated at 2026-10-25 00:44:54.477375
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is inserted immediately when space is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()
    assert queue.get_nowait() == "first"
    queue.task_done()

    # Inserting into a full queue raises QueueFull without modifying it.
    queue.put_nowait("existing")
    try:
        queue.put_nowait("extra")
    except QueueFull:
        pass
    else:
        raise AssertionError("QueueFull was not raised")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "existing"
    queue.task_done()

    # A waiting getter receives the item directly.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("delivered")
    assert getter.done()
    assert getter.result() == "delivered"
    assert queue.empty()

    queue.task_done()
    assert queue._unfinished_tasks == 0

# Generated at 2026-10-25 00:45:01.337163
# Unit test for method join of class Queue
def test_Queue_join():
    async def test():
        queue = Queue()

        # An empty queue has no unfinished tasks.
        await queue.join()

        await queue.put("item")
        join_future = queue.join()

        # module_0.join() must remain pending until task_done() is called.
        assert not join_future.done()
        assert await queue.get() == "item"
        assert not join_future.done()

        queue.task_done()
        await join_future
        assert join_future.done()

    ioloop.IOLoop.current().run_sync(test)

# Generated at 2026-10-25 00:45:03.984136
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-25 00:45:06.399038
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-25 00:45:08.932035
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-25 00:45:11.346243
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:45:22.840114
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue

# Generated at 2026-10-25 00:45:34.209135
# Unit test for method get of class Queue
def test_Queue_get():
    async def exercise_queue():
        queue = Queue()

        # Getting from an empty queue waits for an item.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("first")
        assert await pending_get == "first"
        queue.task_done()

        # Available items are returned immediately and in FIFO order.
        await queue.put("second")
        await queue.put("third")

        assert await queue.get() == "second"
        queue.task_done()
        assert await queue.get() == "third"
        queue.task_done()

        assert queue.empty()
        await queue.join()

        # A get on an empty queue respects its timeout.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # A timed-out getter must not consume a subsequently added item.
        await queue.put("after-timeout")
        assert await queue.get() == "after-timeout"
        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(exercise_queue)

# Generated at 2026-10-25 00:45:43.937080
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        q = Queue(maxsize=1)

        # Putting into an empty queue completes immediately.
        first_put = q.put("first")
        assert first_put.done()
        assert await first_put is None
        assert q.qsize() == 1

        # Putting into a full queue waits until space is available.
        second_put = q.put("second")
        assert not second_put.done()
        assert q.qsize() == 1

        assert await q.get() == "first"
        q.task_done()

        # Removing the first item allows the pending put to complete.
        assert await second_put is None
        assert q.qsize() == 1

        assert await q.get() == "second"
        q.task_done()

        await q.join()
        assert q.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:45:48.236525
# Unit test for method put of class Queue
def test_Queue_put():q = Queue(maxsize=1)

# Generated at 2026-10-25 00:45:56.326666
# Unit test for method put of class Queue
def test_Queue_put():
    queue = Queue(maxsize=1)

    first_put = queue.put("first")
    assert first_put.done()
    assert first_put.result() is None
    assert queue.qsize() == 1

    # A second put must wait because the queue is full.
    second_put = queue.put("second")
    assert not second_put.done()
    assert queue.qsize() == 1

    # Removing the first item creates room and completes the pending put.
    assert queue.get_nowait() == "first"
    assert second_put.done()
    assert second_put.result() is None
    queue.task_done()

    assert queue.qsize() == 1
    assert queue.get_nowait() == "second"
    queue.task_done()

    assert queue.empty()
    assert queue.join().done()

# Generated at 2026-10-25 00:45:57.644914
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 00:45:59.092396
# Unit test for method __anext__ of class _QueueIterator
def test__QueueIterator___anext__():from tornado.queues import Queue, _QueueIterator

# Generated at 2026-10-25 00:46:08.936856
# Unit test for method put of class Queue
def test_Queue_put():
    queue = Queue(maxsize=1)

    # An item is inserted immediately when capacity is available.
    first_put = queue.put("first")
    assert first_put.done()
    assert first_put.result() is None
    assert queue.qsize() == 1
    assert queue.full()

    # A second put waits while the queue is full.
    second_put = queue.put("second")
    assert not second_put.done()
    assert queue.qsize() == 1

    # Removing the first item makes room for the pending put.
    assert queue.get_nowait() == "first"
    assert second_put.done()
    assert second_put.result() is None
    assert queue.qsize() == 1

    assert queue.get_nowait() == "second"
    assert queue.empty()

    # Both successfully enqueued items must be marked complete.
    queue.task_done()
    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-25 00:46:10.357463
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

# Generated at 2026-10-25 00:46:12.869038
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 00:46:15.285116
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 00:46:16.721721
# Unit test for method __anext__ of class _QueueIterator
def test__QueueIterator___anext__():from tornado.queues import Queue, _QueueIterator

# Generated at 2026-10-25 00:46:26.843245
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import pytest

    queue = Queue(maxsize=1)

    # An item is added immediately when space is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()

    # Adding another item to a full queue raises QueueFull.
    with pytest.raises(QueueFull):
        queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.empty()

    # A waiting getter receives the item immediately.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("third")

    assert getter.done()
    assert getter.result() == "third"
    assert queue.empty()

    queue.task_done()

# Generated at 2026-10-25 00:46:35.738805
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # Putting into a non-full queue completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        await first_put
        assert queue.qsize() == 1

        # Putting into a full queue waits for space.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item admits the waiting putter.
        assert await queue.get() == "first"
        queue.task_done()

        await second_put
        assert queue.qsize() == 1
        assert await queue.get() == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:46:40.372815
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-25 00:46:50.154816
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import pytest

    # Enqueues an item immediately when space is available.
    queue = Queue(maxsize=2)
    queue.put_nowait("first")

    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.get_nowait() == "first"
    queue.task_done()

    # Raises QueueFull when no slot is available.
    queue = Queue(maxsize=1)
    queue.put_nowait("first")

    with pytest.raises(QueueFull):
        queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    queue.task_done()

    # Delivers directly to a waiting getter.
    queue = Queue()
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("item")

    assert getter.done()
    assert getter.result() == "item"
    assert queue.empty()
    queue.task_done()

# Generated at 2026-10-25 00:47:00.126398
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()

    # Getting from an empty queue should wait for an item.
    pending_get = q.get()
    assert not pending_get.done()

    first_item = object()
    q.put_nowait(first_item)

    assert pending_get.done()
    assert pending_get.result() is first_item
    assert q.empty()
    q.task_done()

    # Getting an already queued item should complete immediately.
    second_item = object()
    q.put_nowait(second_item)

    immediate_get = q.get()
    assert immediate_get.done()
    assert immediate_get.result() is second_item
    assert q.empty()
    q.task_done()

    assert q.join().done()

# Generated at 2026-10-25 00:47:02.540917
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:47:04.958828
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:47:07.371083
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:47:09.786543
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:47:12.219904
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:47:14.632366
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:47:17.047244
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:47:19.463960
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:47:21.885786
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:47:24.301753
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:47:26.741027
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:47:29.157555
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:47:31.572329
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:47:34.182709
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue

# Generated at 2026-10-25 00:47:46.306656
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is added immediately when space is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert queue.full()
    assert queue.get_nowait() == "first"
    queue.task_done()

    # QueueFull is raised when no slot is available.
    queue.put_nowait("second")
    try:
        queue.put_nowait("third")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.get_nowait() == "second"
    queue.task_done()

    # A waiting getter receives the item directly.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert queue.empty()
    queue.task_done()

    # Completed/cancelled getters are ignored.
    cancelled_getter = queue.get()
    cancelled_getter.cancel()

    queue.put_nowait("after-cancel")
    assert queue.qsize() == 1
    assert queue.get_nowait() == "after-cancel"
    queue.task_done()

    assert queue._unfinished_tasks == 0

# Generated at 2026-10-25 00:47:47.738931
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

# Generated at 2026-10-25 00:48:03.422120
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # An item already in the queue is returned immediately.
        queue.put_nowait("ready")
        ready = queue.get()
        assert ready.done()
        assert await ready == "ready"
        queue.task_done()

        # An empty queue returns a pending awaitable that resolves after put().
        pending = queue.get()
        assert not pending.done()

        await queue.put("later")
        assert await pending == "later"
        assert queue.empty()
        queue.task_done()

        # A pending get raises TimeoutError when its timeout expires.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # Timed-out getters must not consume subsequently added items.
        queue.put_nowait("after-timeout")
        assert await queue.get() == "after-timeout"
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:48:05.963025
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:48:08.505385
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:48:10.924453
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:48:13.497863
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:48:15.924121
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:48:18.338711
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:48:20.756113
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:48:23.182905
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:48:25.598963
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:48:28.012941
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:48:30.431925
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:48:32.855636
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:48:35.276933
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:48:37.693992
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:48:40.115513
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:48:42.537719
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:48:57.781434
# Unit test for method put of class Queue
def test_Queue_put():q = Queue()

# Generated at 2026-10-25 00:49:09.373586
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # module_0.get() waits when the queue is empty.
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

        # A timed-out getter must not consume a subsequently added item.
        timed_get = queue.get(timeout=ioloop.IOLoop.current().time() - 1)
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        queue.put_nowait("third")
        assert await queue.get() == "third"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:49:21.845034
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # module_0.get() waits while the queue is empty.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # module_0.get() immediately returns an already queued item.
        queue.put_nowait("second")
        assert await queue.get() == "second"
        assert queue.empty()
        queue.task_done()

        # An empty queue respects the timeout.
        timed_get = queue.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("module_0.get() did not time out")

        # The expired getter must not consume later items.
        queue.put_nowait("third")
        assert await queue.get() == "third"
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:49:24.377317
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:26.792215
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:29.206287
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:49:31.798456
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:49:34.215129
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:49:36.630168
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:39.046794
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:41.463816
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:43.881490
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:46.298692
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:48.714836
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:51.142011
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:53.556294
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:55.971985
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:49:58.437098
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:50:00.850402
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:50:03.264770
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:50:05.679335
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:50:08.094749
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:50:10.510646
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:50:13.087073
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:50:14.478338
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 00:50:25.231409
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # Getting an already queued item resolves immediately.
        queue.put_nowait("first")
        assert await queue.get() == "first"
        assert queue.empty()
        queue.task_done()

        # Getting from an empty queue waits for a producer.
        pending_get = queue.get()
        assert isinstance(pending_get, Future)
        assert not pending_get.done()

        queue.put_nowait("second")
        assert await pending_get == "second"
        assert queue.empty()
        queue.task_done()

        # A waiting get raises TimeoutError when its timeout expires.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=1))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The expired getter must not consume a later item.
        queue.put_nowait("third")
        assert await queue.get() == "third"
        queue.task_done()

        assert queue.empty()
        assert queue._unfinished_tasks == 0

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:50:26.664868
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 00:50:28.052306
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

# Generated at 2026-10-25 00:50:37.112541
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item is inserted immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1

        # A second put waits while the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item creates space and completes the waiting put.
        first_item = await queue.get()
        assert first_item == "first"
        queue.task_done()

        await second_put
        assert queue.qsize() == 1

        second_item = await queue.get()
        assert second_item == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:50:55.860350
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        # An item is inserted immediately when space is available.
        queue = Queue(maxsize=1)
        first_put = queue.put("first")

        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1

        # A put waits while the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert queue.get_nowait() == "first"
        queue.task_done()

        assert await second_put is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        queue.task_done()
        await queue.join()

        # A waiting getter receives a newly put item directly.
        direct_queue = Queue()
        getter = direct_queue.get()
        assert not getter.done()

        direct_put = direct_queue.put("direct")
        assert await direct_put is None
        assert await getter == "direct"
        assert direct_queue.empty()

        direct_queue.task_done()
        await direct_queue.join()

        # A blocked put raises TimeoutError and does not enqueue its item.
        timeout_queue = Queue(maxsize=1)
        await timeout_queue.put("held")

        timed_out_put = timeout_queue.put(
            "not-inserted", timeout=datetime.timedelta(milliseconds=10)
        )

        try:
            await timed_out_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.put() did not time out")

        assert timeout_queue.get_nowait() == "held"
        assert timeout_queue.empty()

        timeout_queue.task_done()
        await timeout_queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:50:58.309146
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:51:00.749040
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:51:03.193172
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:51:05.607528
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:51:08.022256
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:51:10.437948
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:51:12.853574
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:51:15.269025
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:51:17.684833
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:51:20.122752
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:51:22.565146
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:51:25.200397
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue

# Generated at 2026-10-25 00:51:35.899488
# Unit test for method get of class Queue
def test_Queue_get():
    async def exercise():
        queue = Queue[str]()

        # An empty queue should return a pending awaitable.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # An available item should be returned immediately.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        queue.task_done()

        # Waiting on an empty queue should respect the timeout.
        timed_get = queue.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(exercise)

# Generated at 2026-10-25 00:51:37.249309
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 00:51:38.755261
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

# Generated at 2026-10-25 00:51:48.475441
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # Putting into a queue with available capacity completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1
        assert queue.full()

        # A second put must wait until space becomes available.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert await queue.get() == "first"
        queue.task_done()

        # Removing the first item admits the waiting putter.
        await second_put
        assert second_put.done()
        assert queue.qsize() == 1
        assert await queue.get() == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:51:52.627409
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-25 00:51:54.319313
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

# Generated at 2026-10-25 00:52:03.638111
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # Putting into a non-full queue completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1

        # Putting into a full queue waits for space.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert await queue.get() == "first"

        # Removing the first item allows the waiting put to complete.
        assert await second_put is None
        assert queue.qsize() == 1
        assert await queue.get() == "second"

        queue.task_done()
        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:52:10.139338
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)


# Generated at 2026-10-25 00:52:12.657470
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:52:15.075065
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:52:17.609540
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:52:20.025427
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:52:22.439806
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:52:24.857532
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:52:27.276653
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:52:29.689517
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:52:32.104947
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:52:34.519988
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:52:36.934759
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:52:38.329630
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 00:52:49.531557
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is added immediately when capacity is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert queue.full()
    assert not queue.join().done()

    # Adding another item to a full queue raises QueueFull.
    try:
        queue.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("QueueFull was not raised")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.join().done()

    # A waiting getter receives the item directly.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("second")

    assert getter.done()
    assert getter.result() == "second"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-25 00:52:58.928860
# Unit test for method put of class Queue
def test_Queue_put():
    async def exercise_queue():
        queue = Queue(maxsize=1)

        # Putting into a non-full queue completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        await first_put
        assert queue.qsize() == 1
        assert queue.full()

        # A second put must wait because the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item allows the pending put to complete.
        assert await queue.get() == "first"
        queue.task_done()

        await second_put
        assert second_put.done()
        assert queue.qsize() == 1
        assert await queue.get() == "second"
        queue.task_done()

        # Every enqueued item has been marked as processed.
        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(exercise_queue)

# Generated at 2026-10-25 00:53:03.391439
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-25 00:53:04.877505
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

# Generated at 2026-10-25 00:53:15.319153
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=2)

    # Items are added immediately and preserve FIFO order.
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.qsize() == 2
    assert queue.full()
    assert queue._unfinished_tasks == 2

    # Adding an item to a full queue raises QueueFull without modifying it.
    try:
        queue.put_nowait("third")
    except QueueFull:
        pass
    else:
        raise AssertionError("QueueFull was not raised")

    assert queue.qsize() == 2
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.get_nowait() == "second"
    queue.task_done()
    assert queue.empty()

    # A waiting getter receives the item directly.
    waiting_queue = Queue()
    getter = waiting_queue.get()

    assert not getter.done()

    waiting_queue.put_nowait("value")

    assert getter.done()
    assert getter.result() == "value"
    assert waiting_queue.empty()
    assert waiting_queue._unfinished_tasks == 1

    waiting_queue.task_done()
    assert waiting_queue._unfinished_tasks == 0

# Generated at 2026-10-25 00:53:17.737085
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:53:20.333035
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:53:22.857089
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:53:25.275632
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:53:27.691217
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:53:30.110164
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 00:53:32.678235
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:53:35.096048
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:53:37.513214
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 00:53:39.923263
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:53:42.340414
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:53:44.759184
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:53:47.175328
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:53:49.591340
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:53:52.005608
# Unit test for method put of class Queue

# Generated at 2026-10-25 00:53:54.420076
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:53:56.835945
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:53:59.251659
# Unit test for method get of class Queue

# Generated at 2026-10-25 00:54:13.893106
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # Putting into a queue with available capacity completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "first"
        queue.task_done()

        # A put blocks while the queue is full.
        await queue.put("second")
        blocked_put = queue.put("third")
        assert not blocked_put.done()
        assert queue.qsize() == 1

        # Removing an item makes room for the waiting putter.
        assert queue.get_nowait() == "second"
        await blocked_put
        assert queue.qsize() == 1
        assert queue.get_nowait() == "third"

        queue.task_done()
        queue.task_done()
        await queue.join()

        assert queue.empty()
        assert queue._unfinished_tasks == 0

        # A waiting getter receives an item directly from module_0.put().
        getter = queue.get()
        assert not getter.done()

        direct_put = queue.put("fourth")
        await direct_put
        assert await getter == "fourth"
        assert queue.empty()

        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 00:54:18.587435
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)