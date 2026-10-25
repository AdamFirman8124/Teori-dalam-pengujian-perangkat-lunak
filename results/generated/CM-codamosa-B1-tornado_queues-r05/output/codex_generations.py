

# Generated at 2026-10-24 22:59:49.273786
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-24 23:00:06.066764
# Unit test for method __anext__ of class _QueueIterator
def test__QueueIterator___anext__():from tornado.queues import Queue, _QueueIterator

# Generated at 2026-10-24 23:00:22.553389
# Unit test for constructor of class PriorityQueue
def test_PriorityQueue():
    q = PriorityQueue()

    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()

    # Verify that the queue is initialized as a priority heap.
    q.put_nowait((2, "low"))
    q.put_nowait((1, "high"))

    assert q.get_nowait() == (1, "high")
    assert q.get_nowait() == (2, "low")

    with pytest.raises(QueueEmpty):
        q.get_nowait()

# Generated at 2026-10-24 23:00:32.998637
# Unit test for constructor of class _QueueIterator

# Generated at 2026-10-24 23:00:46.617951
# Unit test for constructor of class _QueueIterator
def test__QueueIterator():q = Queue()

# Generated at 2026-10-24 23:00:47.939319
# Unit test for constructor of class Queue
def test_Queue():
    # Valid default construction
    q = Queue()
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()

    # Explicit maxsize
    q2 = Queue(maxsize=5)
    assert q2.maxsize == 5
    assert not q2.full()

    # maxsize=None must raise TypeError
    try:
        Queue(maxsize=None)
        assert False, "expected TypeError"
    except TypeError:
        pass

    # Negative maxsize must raise ValueError
    try:
        Queue(maxsize=-1)
        assert False, "expected ValueError"
    except ValueError:
        pass

    # New queue is in "finished" state (join() returns immediately)
    q3 = Queue()
    assert q3._unfinished_tasks == 0
    assert q3._finished.is_set()

    # Internal containers initialized
    assert len(q3._getters) == 0
    assert len(q3._putters) == 0

    print("test_Queue passed")


if __name__ == "__main__":
    test_Queue()

# Generated at 2026-10-24 23:00:58.393075
# Unit test for constructor of class QueueEmpty
def test_QueueEmpty():
    exc = QueueEmpty()
    assert isinstance(exc, Exception)
    assert exc.args == ()

    with pytest.raises(QueueEmpty):
        raise QueueEmpty

    with pytest.raises(QueueEmpty, match="queue is empty"):
        raise QueueEmpty("queue is empty")

# Generated at 2026-10-24 23:00:59.826979
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

# Generated at 2026-10-24 23:01:01.261509
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

# Generated at 2026-10-24 23:01:16.419454
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item is inserted immediately when capacity is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1

        # A second put must wait because the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item allows the waiting put to complete.
        assert queue.get_nowait() == "first"
        assert await second_put is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"

        queue.task_done()
        queue.task_done()
        await queue.join()

        # A blocked put raises TimeoutError when its timeout expires.
        timeout_queue = Queue(maxsize=1)
        await timeout_queue.put("held")

        timed_put = timeout_queue.put(
            "timed-out", timeout=datetime.timedelta(milliseconds=1)
        )
        try:
            await timed_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("blocked put did not time out")

        # The timed-out item must not be inserted later.
        assert timeout_queue.get_nowait() == "held"
        assert timeout_queue.empty()

        timeout_queue.task_done()
        await timeout_queue.join()

    ioloop.IOLoop.current().run_sync(run_test, timeout=1)

# Generated at 2026-10-24 23:01:17.940163
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

# Generated at 2026-10-24 23:01:26.155020
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # module_0.get() waits when the queue is empty.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # module_0.get() returns immediately when an item is already available.
        await queue.put("second")
        pending_get = queue.get()
        assert pending_get.done()
        assert await pending_get == "second"
        assert queue.empty()
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:01:27.782148
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:01:29.215653
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

# Generated at 2026-10-24 23:01:37.716031
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
        raise AssertionError("module_0.task_done() should raise ValueError when called too often")

# Generated at 2026-10-24 23:01:47.443205
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

        # Putting into a full queue waits until capacity becomes available.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert await queue.get() == "first"
        queue.task_done()

        # Removing the first item admits the waiting putter.
        assert second_put.done()
        assert await second_put is None
        assert queue.qsize() == 1

        assert await queue.get() == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:01:51.743393
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:02:03.790026
# Unit test for method join of class Queue
def test_Queue_join():
    async def run_test():
        queue = Queue()

        # An empty queue has no unfinished tasks.
        await queue.join()

        queue.put_nowait("first")
        queue.put_nowait("second")

        join_future = queue.join()
        assert isinstance(join_future, Future)
        assert not join_future.done()

        assert queue.get_nowait() == "first"
        queue.task_done()
        assert not join_future.done()

        assert queue.get_nowait() == "second"
        queue.task_done()

        await join_future
        assert join_future.done()

        # Adding another item must cause module_0.join() to block again.
        queue.put_nowait("third")
        second_join = queue.join()
        assert not second_join.done()

        assert queue.get_nowait() == "third"
        queue.task_done()
        await second_join

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:02:05.260441
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

# Generated at 2026-10-24 23:02:15.077925
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # Getting from an empty queue should wait.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("first")
        assert await pending_get == "first"
        queue.task_done()

        # Getting an already queued item should complete immediately.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:02:16.523828
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:02:24.227626
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import pytest

    queue = Queue(maxsize=1)

    # An item can be added immediately when space is available.
    assert queue.put_nowait("first") is None
    assert queue.qsize() == 1
    assert queue.full()
    assert queue.get_nowait() == "first"
    queue.task_done()

    # Adding to a full queue raises QueueFull without changing its contents.
    queue.put_nowait("second")
    with pytest.raises(QueueFull):
        queue.put_nowait("third")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "second"
    queue.task_done()

    # A waiting getter receives the item directly.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("fourth")

    assert getter.done()
    assert getter.result() == "fourth"
    assert queue.empty()

    queue.task_done()
    assert queue._unfinished_tasks == 0

# Generated at 2026-10-24 23:02:38.233728
# Unit test for method get of class Queue
def test_Queue_get():
    async def exercise_get():
        queue = Queue()

        # An available item is returned immediately.
        queue.put_nowait("first")
        assert await queue.get() == "first"
        queue.task_done()

        # A get on an empty queue waits until an item is added.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("second")
        assert await pending_get == "second"
        queue.task_done()

        # A pending get raises TimeoutError after its deadline.
        past_deadline = ioloop.IOLoop.current().time() - 1
        try:
            await queue.get(timeout=past_deadline)
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(exercise_get)

# Generated at 2026-10-24 23:02:48.166122
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be put immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1

        # A second put must wait because the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item makes room and completes the waiting put.
        assert await queue.get() == "first"
        assert await second_put is None
        assert queue.qsize() == 1
        assert await queue.get() == "second"

        # Both successfully put items must be marked complete.
        queue.task_done()
        queue.task_done()
        await queue.join()

        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:02:53.857468
# Unit test for method put of class Queue
def test_Queue_put():from tornado.queues import Queue


# Generated at 2026-10-24 23:02:55.334719
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

# Generated at 2026-10-24 23:03:05.023765
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue[str]()

        # module_0.get() should wait while the queue is empty.
        pending_get = q.get()
        assert not pending_get.done()

        # Adding an item should resolve the waiting module_0.get().
        await q.put("first")
        assert await pending_get == "first"
        assert q.empty()

        q.task_done()
        await q.join()

        # module_0.get() should resolve immediately when an item is available.
        await q.put("second")
        immediate_get = q.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        assert q.empty()

        q.task_done()
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:03:06.496005
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:03:17.760563
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # Getting from an empty queue waits for an item.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # Getting an already queued item completes immediately.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        queue.task_done()

        # A get from an empty queue respects its timeout.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The timed-out getter must not consume subsequently added items.
        queue.put_nowait("third")
        assert await queue.get() == "third"
        queue.task_done()

        assert queue.empty()
        assert queue._unfinished_tasks == 0

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:03:19.097572
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:03:27.287740
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    queue = Queue()

    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"

    join_future = queue.join()
    assert not join_future.done()

    queue.task_done()
    assert not join_future.done()

    queue.task_done()
    assert join_future.done()
    assert join_future.result() is None

    try:
        queue.task_done()
    except ValueError as exc:
        assert str(exc) == "module_0.task_done() called too many times"
    else:
        raise AssertionError("module_0.task_done() should raise ValueError when called too many times")

# Generated at 2026-10-24 23:03:39.678838
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue(maxsize=1)

        # An available item is returned immediately.
        await q.put("buffered")
        get_future = q.get()
        assert get_future.done()
        assert await get_future == "buffered"
        assert q.empty()
        q.task_done()

        # When empty, module_0.get() waits until an item is put.
        pending_get = q.get()
        assert not pending_get.done()

        await q.put("delivered")
        assert await pending_get == "delivered"
        assert q.empty()

        q.task_done()
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:03:41.007601
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:03:42.443653
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

# Generated at 2026-10-24 23:03:52.377850
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue(maxsize=2)

        # module_0.get() waits when the queue is empty.
        waiting_get = q.get()
        assert not waiting_get.done()

        await q.put("first")
        assert await waiting_get == "first"
        assert q.empty()
        q.task_done()

        # module_0.get() immediately returns queued items in FIFO order.
        await q.put("second")
        await q.put("third")

        assert await q.get() == "second"
        q.task_done()

        assert await q.get() == "third"
        q.task_done()

        assert q.empty()
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:03:54.801428
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:03:57.215962
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:03:59.631755
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:04:02.050499
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:04:04.479430
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:04:06.887111
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:04:12.646539
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:04:26.272695
# Unit test for method put of class Queue
def test_Queue_put():
    async def test():
        queue = Queue(maxsize=1)

        # Putting into a non-full queue completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1

        # Putting into a full queue waits until space becomes available.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert await queue.get() == "first"
        queue.task_done()

        await second_put
        assert second_put.done()
        assert queue.qsize() == 1

        # A blocked put respects its timeout and does not enqueue the item.
        timed_put = queue.put("third", timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.put() did not time out")

        assert queue.qsize() == 1
        assert await queue.get() == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(test)

# Generated at 2026-10-24 23:04:30.846838
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:04:44.595970
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item is inserted immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1
        assert queue.full()

        # A second put waits while the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item admits the waiting putter.
        assert queue.get_nowait() == "first"
        assert second_put.done()
        assert second_put.result() is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"

        # Both successfully enqueued items must be marked complete.
        queue.task_done()
        queue.task_done()
        await queue.join()

        # A blocked put raises TimeoutError when its timeout expires.
        timeout_queue = Queue(maxsize=1)
        await timeout_queue.put("existing")

        timed_put = timeout_queue.put(
            "timed-out", timeout=datetime.timedelta(milliseconds=10)
        )
        try:
            await timed_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.put() did not time out")

        assert timeout_queue.qsize() == 1
        assert timeout_queue.get_nowait() == "existing"
        timeout_queue.task_done()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:04:47.120701
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:04:49.540503
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:04:51.969341
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:04:54.385857
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:04:56.811285
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:04:59.224009
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:05:01.641391
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:05:04.057615
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:05:06.476381
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:05:08.893060
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:05:11.310283
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:05:13.728636
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:05:16.143650
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:05:17.521185
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:05:27.503150
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # Putting into a queue with available capacity completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        await first_put
        assert queue.qsize() == 1

        # Putting into a full queue waits until space becomes available.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert queue.get_nowait() == "first"
        assert second_put.done()
        await second_put

        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        assert queue.empty()

        queue.task_done()
        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:05:32.950810
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:05:43.375949
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item is added immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1
        assert queue.full()

        # A second put waits while the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item makes room for the waiting put.
        assert queue.get_nowait() == "first"
        await second_put
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"

        # Both successfully put items must be marked complete.
        queue.task_done()
        queue.task_done()
        await queue.join()
        assert queue.empty()

        # A blocked put raises TimeoutError when its timeout expires.
        timeout_queue = Queue(maxsize=1)
        await timeout_queue.put("existing")

        timed_out_put = timeout_queue.put(
            "never-added", timeout=datetime.timedelta(milliseconds=10)
        )
        try:
            await timed_out_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.put() did not time out")

        assert timeout_queue.qsize() == 1
        assert timeout_queue.get_nowait() == "existing"
        timeout_queue.task_done()
        await timeout_queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:05:47.572010
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:05:59.861044
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue[str]()

        # An available item is returned immediately.
        q.put_nowait("first")
        assert await q.get() == "first"
        assert q.empty()
        q.task_done()

        # module_0.get() waits when the queue is empty.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait("second")
        assert await pending_get == "second"
        assert q.empty()
        q.task_done()

        # A waiting module_0.get() raises TimeoutError when its timeout expires.
        try:
            await q.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The expired getter must not consume subsequently added items.
        q.put_nowait("third")
        assert await q.get() == "third"
        q.task_done()

        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:06:02.406692
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:06:04.823119
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:06:07.360522
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:06:09.778069
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:06:12.195262
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:06:14.611835
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:06:21.875712
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()

    # Empty queue raises QueueEmpty
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # FIFO order: first put is first out
    q.put_nowait(10)
    q.put_nowait(20)
    assert q.qsize() == 2
    assert q.get_nowait() == 10
    assert q.get_nowait() == 20
    assert q.empty()

    # Pending putter is consumed by get_nowait when a slot frees up
    q = Queue(maxsize=1)
    q.put_nowait("a")          # queue now full
    putter_future = q.put("b") # putter waits for a free slot
    assert q.full()
    assert q.get_nowait() == "a"   # frees slot, admits waiting item "b"
    assert putter_future.done()
    assert q.get_nowait() == "b"
    assert q.empty()

# Generated at 2026-10-24 23:06:33.141572
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue()

        # An available item is returned immediately.
        q.put_nowait("first")
        assert await q.get() == "first"
        q.task_done()

        # A get on an empty queue waits until an item is added.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait("second")
        assert await pending_get == "second"
        q.task_done()

        # A waiting get raises TimeoutError when its timeout expires.
        timed_get = q.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The expired getter must not consume subsequently added items.
        q.put_nowait("third")
        assert await q.get() == "third"
        q.task_done()

        assert q.empty()
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:06:49.424242
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        q = Queue(maxsize=1)

        # An item can be put immediately when space is available.
        first_put = q.put("first")
        assert first_put.done()
        assert await first_put is None
        assert q.qsize() == 1

        # A second put waits while the queue is full.
        second_put = q.put("second")
        assert not second_put.done()
        assert q.qsize() == 1

        # Removing the first item makes room for the waiting put.
        assert await q.get() == "first"
        q.task_done()

        assert await second_put is None
        assert q.qsize() == 1
        assert await q.get() == "second"
        q.task_done()

        await q.join()
        assert q.empty()

        # A waiting put raises TimeoutError and is not later enqueued.
        assert await q.put("third") is None
        timed_out_put = q.put(
            "fourth", timeout=datetime.timedelta(milliseconds=10)
        )

        try:
            await timed_out_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.put() did not time out")

        assert await q.get() == "third"
        q.task_done()

        try:
            q.get_nowait()
        except QueueEmpty:
            pass
        else:
            raise AssertionError("timed-out item was incorrectly enqueued")

        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:06:54.549538
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:07:10.435519
# Unit test for method get of class Queue
def test_Queue_get():
    async def exercise_get():
        q = Queue[str]()

        # An available item is returned immediately.
        q.put_nowait("ready")
        immediate = q.get()
        assert immediate.done()
        assert await immediate == "ready"
        q.task_done()

        # An empty queue returns a pending future that resolves after put().
        waiting = q.get()
        assert not waiting.done()

        await q.put("delayed")
        assert await waiting == "delayed"
        assert q.empty()
        q.task_done()

        # A timed-out getter must not consume a subsequently added item.
        try:
            await q.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        q.put_nowait("after-timeout")
        assert await q.get() == "after-timeout"
        q.task_done()

        await q.join()

    ioloop.IOLoop.current().run_sync(exercise_get)

# Generated at 2026-10-24 23:07:12.855946
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:07:15.270599
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:07:25.058160
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():q = Queue(maxsize=1)


# Generated at 2026-10-24 23:07:36.221028
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()

    # Getting from an empty queue waits for an item.
    pending_get = q.get()
    assert not pending_get.done()

    q.put_nowait("first")
    assert pending_get.done()
    assert pending_get.result() == "first"
    assert q.empty()
    q.task_done()

    # Getting an already queued item completes immediately.
    q.put_nowait("second")
    immediate_get = q.get()
    assert immediate_get.done()
    assert immediate_get.result() == "second"
    assert q.empty()
    q.task_done()

    assert q.join().done()

# Generated at 2026-10-24 23:07:49.428988
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue(maxsize=2)

        # module_0.get() should immediately return an already queued item in FIFO order.
        queue.put_nowait("first")
        queue.put_nowait("second")

        assert await queue.get() == "first"
        queue.task_done()
        assert await queue.get() == "second"
        queue.task_done()
        assert queue.empty()

        # module_0.get() should wait until an item becomes available.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("later")
        assert await pending_get == "later"
        queue.task_done()

        # A waiting module_0.get() should raise TimeoutError after its timeout.
        timed_get = queue.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The expired getter must not consume subsequently added items.
        queue.put_nowait("after-timeout")
        assert await queue.get() == "after-timeout"
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:07:50.763307
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:08:01.205083
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import pytest

    queue = Queue(maxsize=1)

    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.get_nowait() == "first"

    queue.task_done()
    assert queue._unfinished_tasks == 0

    queue.put_nowait("second")
    with pytest.raises(QueueFull):
        queue.put_nowait("third")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "second"
    queue.task_done()

# Generated at 2026-10-24 23:08:03.628165
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:06.045917
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:08.469558
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:10.885351
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:13.303894
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:15.732150
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:18.150542
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:08:20.568107
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:08:22.987404
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:08:25.409680
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:08:27.828380
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:08:30.244244
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:08:32.660063
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:35.077160
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:37.492251
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:39.912313
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:42.329978
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:08:44.748286
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:09:14.115683
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:09:15.546345
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:09:27.240811
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be added immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        await first_put
        assert queue.qsize() == 1

        # A second put waits until the first item is removed.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert await queue.get() == "first"
        queue.task_done()

        await second_put
        assert queue.qsize() == 1
        assert await queue.get() == "second"
        queue.task_done()
        await queue.join()

        # A blocked put raises TimeoutError when its deadline expires.
        await queue.put("third")
        deadline = ioloop.IOLoop.current().time() + 0.01
        timed_put = queue.put("fourth", timeout=deadline)

        try:
            await timed_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.put() did not time out")

        assert await queue.get() == "third"
        queue.task_done()
        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:09:37.258334
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=1)

    # An item is added immediately when space is available.
    first_put = q.put("first")
    assert first_put.done()
    assert first_put.result() is None
    assert q.qsize() == 1

    # A second put waits while the queue is full.
    second_put = q.put("second")
    assert not second_put.done()
    assert q.qsize() == 1

    # Removing the first item makes room for the pending put.
    assert q.get_nowait() == "first"
    assert second_put.done()
    assert second_put.result() is None
    assert q.qsize() == 1
    assert q.get_nowait() == "second"

    # Both successfully queued items must be marked complete.
    q.task_done()
    q.task_done()
    assert q._unfinished_tasks == 0