

# Generated at 2026-10-24 23:23:31.105449
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is inserted immediately when space is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()

    # Inserting into a full queue raises QueueFull without changing it.
    try:
        queue.put_nowait("overflow")
    except QueueFull:
        pass
    else:
        raise AssertionError("QueueFull was not raised")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()

    # A waiting getter receives the item directly.
    getter = queue.get()
    queue.put_nowait("second")

    assert getter.done()
    assert getter.result() == "second"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-24 23:23:33.633765
# Unit test for method join of class Queue

# Generated at 2026-10-24 23:23:36.049625
# Unit test for method join of class Queue

# Generated at 2026-10-24 23:23:38.468820
# Unit test for method join of class Queue

# Generated at 2026-10-24 23:23:40.885706
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 23:23:43.303032
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 23:23:45.723683
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 23:23:48.139259
# Unit test for method full of class Queue

# Generated at 2026-10-24 23:23:50.557536
# Unit test for method full of class Queue

# Generated at 2026-10-24 23:23:52.974492
# Unit test for method full of class Queue

# Generated at 2026-10-24 23:23:55.398091
# Unit test for method empty of class Queue

# Generated at 2026-10-24 23:24:03.153910
# Unit test for method empty of class Queue
def test_Queue_empty():from tornado.queues import Queue


# Generated at 2026-10-24 23:24:12.576077
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    assert queue.put_nowait("first") is None
    assert queue.qsize() == 1
    assert queue.full()

    try:
        queue.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()

    # Verify that put_nowait satisfies an already-waiting getter.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("second")

    assert getter.done()
    assert getter.result() == "second"
    assert queue.empty()

    queue.task_done()
    assert queue._unfinished_tasks == 0

# Generated at 2026-10-24 23:24:21.795064
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        q = Queue(maxsize=1)

        # An item is inserted immediately when space is available.
        first_put = q.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert q.qsize() == 1

        # A second put waits while the queue is full.
        second_put = q.put("second")
        assert not second_put.done()
        assert q.qsize() == 1

        # Removing the first item allows the pending put to complete.
        assert await q.get() == "first"
        q.task_done()

        await second_put
        assert second_put.result() is None
        assert q.qsize() == 1

        assert await q.get() == "second"
        q.task_done()

        await q.join()
        assert q.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:24:29.846541
# Unit test for method put of class Queue
def test_Queue_put():from tornado.queues import Queue


# Generated at 2026-10-24 23:24:38.892433
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert queue.full()
    assert not queue.empty()

    try:
        queue.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.join().done()

    # A waiting getter should receive the item immediately.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("second")

    assert getter.done()
    assert getter.result() == "second"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-24 23:24:48.831259
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # module_0.get() waits when the queue is empty.
        waiting_get = queue.get()
        assert not waiting_get.done()

        queue.put_nowait("first")
        assert await waiting_get == "first"
        assert queue.empty()
        queue.task_done()

        # module_0.get() resolves immediately when an item is available.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        assert queue.empty()
        queue.task_done()

        # A waiting get raises TimeoutError when its timeout expires.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # A timed-out getter must not consume subsequently added items.
        queue.put_nowait("third")
        assert await queue.get() == "third"
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:24:50.198471
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:24:51.522988
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

# Generated at 2026-10-24 23:25:01.424996
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # The first put completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1

        # A put on a full queue waits for space.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item makes room and completes the waiting put.
        assert queue.get_nowait() == "first"
        queue.task_done()

        await second_put
        assert second_put.result() is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        queue.task_done()

        # Every successfully put item has been processed.
        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:25:11.253805
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-24 23:25:12.707819
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

# Generated at 2026-10-24 23:25:22.108217
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be inserted immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1

        # A second put waits because the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item allows the pending put to complete.
        assert queue.get_nowait() == "first"
        queue.task_done()

        assert second_put.done()
        assert await second_put is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:25:26.007715
# Unit test for method put of class Queue
def test_Queue_put():q = Queue(maxsize=1)

# Generated at 2026-10-24 23:25:27.429263
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

# Generated at 2026-10-24 23:25:37.162699
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be added immediately when space is available.
        first_put = queue.put("first")
        await first_put
        assert first_put.done()
        assert queue.qsize() == 1
        assert queue.full()

        # A second put waits while the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item frees space and completes the waiting put.
        assert queue.get_nowait() == "first"
        await second_put
        queue.task_done()

        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:25:40.867254
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:25:42.278293
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

# Generated at 2026-10-24 23:25:43.697573
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

# Generated at 2026-10-24 23:25:55.130302
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item is inserted immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        await first_put
        assert queue.qsize() == 1
        assert queue.full()

        # A second put waits until space becomes available.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert await queue.get() == "first"
        queue.task_done()

        await second_put
        assert second_put.done()
        assert queue.qsize() == 1
        assert await queue.get() == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

        # A blocked put raises TimeoutError and does not enqueue its item.
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
        assert await timeout_queue.get() == "existing"
        timeout_queue.task_done()
        await timeout_queue.join()
        assert timeout_queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:25:59.689649
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:26:10.030545
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be put immediately when space is available.
        first_put = queue.put("first")
        await first_put
        assert first_put.done()
        assert queue.qsize() == 1
        assert queue.full()

        # A second put waits until the first item is removed.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert queue.get_nowait() == "first"
        await second_put
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"

        queue.task_done()
        queue.task_done()
        await queue.join()

        # Putting directly satisfies a waiting getter.
        waiting_get = queue.get()
        assert not waiting_get.done()

        await queue.put("third")
        assert await waiting_get == "third"
        assert queue.empty()

        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:26:14.226742
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:26:15.661768
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

# Generated at 2026-10-24 23:26:24.159833
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # An item is added immediately when space is available.
    queue = Queue(maxsize=1)
    queue.put_nowait("first")

    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()
    assert queue.get_nowait() == "first"
    queue.task_done()

    # QueueFull is raised without modifying a full queue.
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
    waiting_queue = Queue()
    getter = waiting_queue.get()

    assert not getter.done()

    waiting_queue.put_nowait("delivered")

    assert getter.done()
    assert getter.result() == "delivered"
    assert waiting_queue.empty()

    waiting_queue.task_done()
    assert waiting_queue._unfinished_tasks == 0

# Generated at 2026-10-24 23:26:33.990261
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue[int]()

        # Items already in the queue are returned in FIFO order.
        q.put_nowait(1)
        q.put_nowait(2)
        assert await q.get() == 1
        assert await q.get() == 2

        # A get on an empty queue waits for a producer.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait(3)
        assert await pending_get == 3
        assert q.empty()

        # Every enqueued item must be marked complete.
        q.task_done()
        q.task_done()
        q.task_done()
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test, timeout=1)

# Generated at 2026-10-24 23:26:48.838612
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        q = Queue(maxsize=1)

        # An item can be inserted immediately when space is available.
        first_put = q.put("first")
        assert first_put.done()
        assert await first_put is None
        assert q.qsize() == 1

        # A second put waits while the queue is full.
        second_put = q.put("second")
        assert not second_put.done()
        assert q.qsize() == 1

        # Removing the first item allows the pending put to complete.
        assert q.get_nowait() == "first"
        q.task_done()

        assert await second_put is None
        assert q.qsize() == 1
        assert q.get_nowait() == "second"
        q.task_done()

        # A pending put raises TimeoutError when its timeout expires.
        await q.put("third")
        timed_put = q.put(
            "fourth", timeout=datetime.timedelta(milliseconds=10)
        )

        try:
            await timed_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.put() did not time out")

        # The timed-out item must not have been added.
        assert q.qsize() == 1
        assert q.get_nowait() == "third"
        q.task_done()

        assert q.empty()
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:26:53.651212
# Unit test for method put of class Queue
def test_Queue_put():q = Queue(maxsize=1)

# Generated at 2026-10-24 23:27:04.608236
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import pytest

    queue = Queue(maxsize=2)

    # Items are added immediately and preserve FIFO ordering.
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.qsize() == 2
    assert queue.full()
    assert not queue.empty()

    # Adding an item to a full queue fails without modifying it.
    with pytest.raises(QueueFull):
        queue.put_nowait("third")

    assert queue.qsize() == 2
    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"

    queue.task_done()
    queue.task_done()
    assert queue.empty()

    # A waiting getter receives the item immediately.
    waiting_queue = Queue(maxsize=1)
    getter = waiting_queue.get()

    assert not getter.done()

    waiting_queue.put_nowait("item")

    assert getter.done()
    assert getter.result() == "item"
    assert waiting_queue.empty()

    waiting_queue.task_done()

# Generated at 2026-10-24 23:27:13.925859
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # An available item is returned immediately.
        queue.put_nowait("first")
        immediate = queue.get()
        assert await immediate == "first"
        queue.task_done()

        # When empty, module_0.get() waits until an item is added.
        pending = queue.get()
        assert not pending.done()

        queue.put_nowait("second")
        assert await pending == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

        # An empty queue respects the timeout.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:27:15.264135
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:27:25.597515
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

    # A failed put must not modify the queue.
    assert queue.qsize() == 2
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.get_nowait() == "second"
    queue.task_done()

    assert queue.empty()
    assert queue.join().done()

    # A waiting getter should receive the item immediately.
    waiting_queue = Queue()
    getter = waiting_queue.get()
    assert not getter.done()

    waiting_queue.put_nowait("item")

    assert getter.done()
    assert getter.result() == "item"
    assert waiting_queue.empty()

    waiting_queue.task_done()
    assert waiting_queue.join().done()

# Generated at 2026-10-24 23:27:35.739452
# Unit test for method put of class Queue
def test_Queue_put():
    async def test():
        queue = Queue(maxsize=1)

        # Putting into a queue with available capacity completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1

        # Putting into a full queue waits until space becomes available.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert await queue.get() == "first"
        assert second_put.done()
        assert second_put.result() is None
        assert queue.qsize() == 1
        queue.task_done()

        assert await queue.get() == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(test)

# Generated at 2026-10-24 23:27:39.925639
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 23:27:48.027908
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

    # Removing the first item makes room and completes the pending put.
    assert queue.get_nowait() == "first"
    assert second_put.done()
    assert second_put.result() is None
    assert queue.qsize() == 1
    assert queue.get_nowait() == "second"

    queue.task_done()
    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-24 23:27:57.448638
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # Getting from an empty queue waits for a producer.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("first")
        assert await pending_get == "first"
        queue.task_done()

        # Getting an already queued item completes immediately.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

        # A waiting get raises TimeoutError when its timeout expires.
        timed_get = queue.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:27:59.869737
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:28:01.337915
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:28:13.110179
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be inserted immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "first"
        queue.task_done()

        # A put waits while the queue is full.
        await queue.put("second")
        blocked_put = queue.put("third")
        assert not blocked_put.done()
        assert queue.qsize() == 1

        # Removing an item admits the waiting putter.
        assert queue.get_nowait() == "second"
        assert await blocked_put is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "third"

        queue.task_done()
        queue.task_done()
        await queue.join()

        # A waiting put raises TimeoutError when its timeout expires.
        await queue.put("fourth")
        timed_put = queue.put(
            "fifth", timeout=datetime.timedelta(milliseconds=10)
        )

        try:
            await timed_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.put() did not time out")

        assert queue.qsize() == 1
        assert queue.get_nowait() == "fourth"
        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:28:17.516321
# Unit test for method put of class Queue
def test_Queue_put():q = Queue(maxsize=1)

# Generated at 2026-10-24 23:28:31.296174
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import pytest

    q = Queue(maxsize=1)

    # An item is added immediately when space is available.
    q.put_nowait("first")
    assert q.qsize() == 1
    assert not q.empty()
    assert q.full()

    # A full queue rejects additional items without modifying the queue.
    with pytest.raises(QueueFull):
        q.put_nowait("second")
    assert q.qsize() == 1
    assert q.get_nowait() == "first"
    q.task_done()

    # A waiting getter receives the item directly.
    getter = q.get()
    assert not getter.done()

    q.put_nowait("third")

    assert getter.done()
    assert getter.result() == "third"
    assert q.empty()

    q.task_done()
    assert q.join().done()

# Generated at 2026-10-24 23:28:33.718926
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:28:36.138814
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:28:38.554670
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:28:40.970440
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:28:43.390866
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:28:45.808690
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:28:48.386935
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:28:50.806073
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:28:53.397170
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:28:55.813770
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 23:28:58.231667
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 23:29:00.648794
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 23:29:03.065599
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:29:05.482654
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:29:07.149205
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:29:18.346102
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=2)

    # Items are inserted immediately while capacity is available.
    assert queue.put_nowait("first") is None
    assert queue.put_nowait("second") is None
    assert queue.qsize() == 2
    assert queue.full()

    # Inserting into a full queue raises QueueFull without modifying it.
    try:
        queue.put_nowait("third")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 2
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.get_nowait() == "second"
    queue.task_done()

    # A waiting getter receives the item directly.
    getter = queue.get()
    assert not getter.done()

    assert queue.put_nowait("third") is None
    assert getter.done()
    assert getter.result() == "third"
    assert queue.empty()

    queue.task_done()
    joined = queue.join()
    assert joined.done()
    assert joined.result() is None

# Generated at 2026-10-24 23:29:29.636113
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # An available item is returned immediately.
        queue.put_nowait("first")
        assert await queue.get() == "first"
        assert queue.empty()
        queue.task_done()

        # A get on an empty queue waits until an item is added.
        pending_get = queue.get()
        assert not pending_get.done()  # type: ignore[attr-defined]

        queue.put_nowait("second")
        assert await pending_get == "second"
        assert queue.empty()
        queue.task_done()

        # A timed-out getter is discarded and does not consume later items.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
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

# Generated at 2026-10-24 23:29:30.967698
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:29:40.770649
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # An available item is returned immediately.
        queue.put_nowait("first")
        assert await queue.get() == "first"
        queue.task_done()

        # An empty queue waits until an item is added.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("second")
        assert await pending_get == "second"
        queue.task_done()

        # An empty queue honors the timeout.
        timed_get = queue.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        assert queue.empty()
        assert queue._unfinished_tasks == 0

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:29:42.189822
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:29:51.896799
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        first_put = queue.put("first")
        await first_put

        assert first_put.done()
        assert queue.qsize() == 1
        assert queue.full()

        second_put = queue.put("second")
        assert not second_put.done()

        assert queue.get_nowait() == "first"
        await second_put

        assert second_put.done()
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"

        queue.task_done()
        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:29:54.316421
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:29:56.731504
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:29:59.149417
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:01.567950
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:03.985129
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:06.401953
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:30:08.819612
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:30:11.236663
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:30:13.653511
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:16.071423
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:18.487547
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:20.905190
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:23.322409
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:25.739582
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:28.157519
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:30.573675
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:32.989357
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:35.460071
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:30:37.877549
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:30:40.294296
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:30:42.712882
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:45.132602
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:47.553542
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:49.970449
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:30:52.386730
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:30:54.802736
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:30:57.221104
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:30:59.641184
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:31:02.057960
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:31:04.473614
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:31:05.994613
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

# Generated at 2026-10-24 23:31:16.808425
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue(maxsize=1)

        # Getting from an empty queue waits until an item is available.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait("first")
        assert await pending_get == "first"
        q.task_done()

        # Getting an already queued item completes immediately.
        q.put_nowait("second")
        immediate_get = q.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        q.task_done()

        # A get on an empty queue respects its timeout.
        timed_get = q.get(timeout=datetime.timedelta(milliseconds=1))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The expired getter must not consume subsequently added items.
        next_get = q.get()
        q.put_nowait("third")
        assert await next_get == "third"
        q.task_done()

        await q.join()
        assert q.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:31:18.140921
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:31:29.864216
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is added immediately when capacity is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()
    assert queue._unfinished_tasks == 1

    # Adding to a full queue raises QueueFull without modifying it.
    try:
        queue.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("QueueFull was not raised")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()

    # A waiting getter receives the item directly.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("second")

    assert getter.done()
    assert getter.result() == "second"
    assert queue.empty()
    assert queue._unfinished_tasks == 1
    queue.task_done()

    # Cancelled getters are discarded before the item is enqueued.
    cancelled_getter = queue.get()
    cancelled_getter.cancel()

    queue.put_nowait("third")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "third"
    queue.task_done()
    assert queue._unfinished_tasks == 0

# Generated at 2026-10-24 23:31:42.526003
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be added immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1

        # A second put must wait because the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item makes room for the waiting put.
        assert await queue.get() == "first"
        queue.task_done()

        await second_put
        assert queue.qsize() == 1
        assert await queue.get() == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:31:51.432017
# Unit test for method put of class Queue
def test_Queue_put():from tornado.queues import Queue


# Generated at 2026-10-24 23:31:53.851136
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:31:56.267709
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:31:58.687020
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:32:01.105590
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:32:03.521420
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:32:05.941319
# Unit test for method put of class Queue

# Generated at 2026-10-24 23:32:09.891762
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:32:12.307392
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:32:14.725339
# Unit test for method get of class Queue

# Generated at 2026-10-24 23:32:17.143353
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:32:19.559335
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 23:32:20.950626
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

# Generated at 2026-10-24 23:32:32.084768
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
        raise AssertionError("QueueFull was not raised for a full queue")

    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.get_nowait() == "second"
    queue.task_done()
    assert queue.empty()

    # An item should be delivered directly to a waiting getter.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-24 23:32:44.269810
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue[str]()

        # An available item is returned immediately.
        q.put_nowait("first")
        assert await q.get() == "first"
        q.task_done()

        # An empty queue waits until an item is added.
        pending = q.get()
        assert not pending.done()

        q.put_nowait("second")
        assert await pending == "second"
        q.task_done()

        # A timed-out getter must not consume a later item.
        try:
            await q.get(timeout=datetime.timedelta(milliseconds=1))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        q.put_nowait("third")
        assert await q.get() == "third"
        q.task_done()

        assert q.empty()
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:32:45.703243
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 23:32:55.257524
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # Putting into a queue with available capacity completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        await first_put
        assert queue.qsize() == 1
        assert queue.full()

        # Putting into a full queue waits until space becomes available.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        assert queue.get_nowait() == "first"

        # Removing the first item admits the waiting putter.
        await second_put
        assert second_put.done()
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"

        # Both successfully put items must be marked complete.
        queue.task_done()
        queue.task_done()
        await queue.join()

        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:33:00.043826
# Unit test for method put of class Queue
def test_Queue_put():q = Queue(maxsize=1)

# Generated at 2026-10-24 23:33:08.436911
# Unit test for method get of class Queue
def test_Queue_get():
    queue = Queue()

    # module_0.get() should wait when the queue is empty.
    pending_get = queue.get()
    assert not pending_get.done()

    queue.put_nowait("first")
    assert pending_get.done()
    assert pending_get.result() == "first"
    queue.task_done()

    # module_0.get() should resolve immediately when an item is available.
    queue.put_nowait("second")
    immediate_get = queue.get()
    assert immediate_get.done()
    assert immediate_get.result() == "second"
    queue.task_done()

    assert queue.empty()
    assert queue.join().done()

# Generated at 2026-10-24 23:33:17.219372
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test() -> None:
        q = Queue()  # type: Queue[int]

        # module_0.get() should wait when the queue is empty.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait(10)
        assert await pending_get == 10
        assert q.empty()
        q.task_done()

        # Available items should be returned immediately in FIFO order.
        q.put_nowait(20)
        q.put_nowait(30)

        assert await q.get() == 20
        assert await q.get() == 30
        assert q.empty()

        q.task_done()
        q.task_done()
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:33:24.740522
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue[int]()

        # module_0.get() waits when the queue is empty.
        pending_get = q.get()
        assert not pending_get.done()

        await q.put(42)
        assert await pending_get == 42
        assert q.empty()
        q.task_done()

        # module_0.get() resolves immediately when an item is available.
        await q.put(7)
        immediate_get = q.get()
        assert immediate_get.done()
        assert await immediate_get == 7
        assert q.empty()
        q.task_done()

        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 23:33:26.101864
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen