

# Generated at 2026-10-24 22:35:54.658563
# Unit test for constructor of class LifoQueue

# Generated at 2026-10-24 22:35:57.842134
# Unit test for constructor of class LifoQueue
def test_LifoQueue():q = LifoQueue()
assert q.maxsize == 0
assert q.qsize() == 0
assert q.empty()
assert not q.full()

q2 = LifoQueue(maxsize=3)
assert q2.maxsize == 3
assert q2.qsize() == 0
assert q2.empty()
assert not q2.full()

q2.put(1)
q2.put(2)
assert q2.qsize() == 2
assert not q2.empty()
assert not q2.full()

q2.put(3)
assert q2.full()
assert q2.qsize() == 3

# Generated at 2026-10-24 22:36:20.395847
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

# Generated at 2026-10-24 22:36:25.304401
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

# Generated at 2026-10-24 22:36:32.736779
# Unit test for method __repr__ of class Queue
def test_Queue___repr__():
    queue = Queue(maxsize=2)

    assert repr(queue) == (
        f"<Queue at {hex(id(queue))} maxsize=2>"
    )

    queue.put_nowait("item")

    assert repr(queue) == (
        f"<Queue at {hex(id(queue))} "
        "maxsize=2 queue=deque(['item']) tasks=1>"
    )

# Generated at 2026-10-24 22:36:59.975888
# Unit test for method __repr__ of class Queue
def test_Queue___repr__():from tornado.queues import Queue


# Generated at 2026-10-24 22:37:06.945582
# Unit test for method __repr__ of class Queue
def test_Queue___repr__():
    queue = Queue(maxsize=2)

    assert repr(queue) == (
        f"<Queue at {hex(id(queue))} maxsize=2>"
    )

    queue.put_nowait("item")

    assert repr(queue) == (
        f"<Queue at {hex(id(queue))} "
        "maxsize=2 queue=deque(['item']) tasks=1>"
    )

# Generated at 2026-10-24 22:37:09.368079
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-24 22:37:10.688373
# Unit test for method __repr__ of class Queue
def test_Queue___repr__():from tornado.queues import Queue


# Generated at 2026-10-24 22:37:19.675878
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    queue = Queue()
    assert queue.join().done()

    queue.put_nowait("first")
    queue.put_nowait("second")

    join_future = queue.join()
    assert not join_future.done()

    assert queue.get_nowait() == "first"
    queue.task_done()
    assert not join_future.done()

    assert queue.get_nowait() == "second"
    queue.task_done()
    assert join_future.done()
    assert join_future.result() is None

    try:
        queue.task_done()
    except ValueError as error:
        assert str(error) == "module_0.task_done() called too many times"
    else:
        raise AssertionError("module_0.task_done() did not raise ValueError")

# Generated at 2026-10-24 22:37:30.068609
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # An available item is returned immediately.
        queue.put_nowait("first")
        result = queue.get()
        assert isinstance(result, Future)
        assert result.done()
        assert await result == "first"
        queue.task_done()

        # module_0.get() waits until an item is added.
        pending = queue.get()
        assert isinstance(pending, Future)
        assert not pending.done()

        queue.put_nowait("second")
        assert await pending == "second"
        queue.task_done()

        # An empty queue times out when no item becomes available.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The expired getter must not consume subsequently added items.
        queue.put_nowait("third")
        assert await queue.get() == "third"
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:37:36.021364
# Unit test for method __repr__ of class Queue
def test_Queue___repr__():
    queue = Queue(maxsize=2)

    assert repr(queue) == "<Queue at %s maxsize=2>" % hex(id(queue))

    queue.put_nowait("item")
    assert repr(queue) == (
        "<Queue at %s maxsize=2 queue=deque(['item']) tasks=1>"
        % hex(id(queue))
    )

# Generated at 2026-10-24 22:37:37.403991
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

# Generated at 2026-10-24 22:37:51.279233
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is enqueued immediately when capacity is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()

    # Adding another item to a full queue raises QueueFull without
    # modifying the existing queue.
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

    # A waiting getter receives the item immediately.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("third")

    assert getter.done()
    assert getter.result() == "third"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-24 22:37:59.469164
# Unit test for method __repr__ of class Queue
def test_Queue___repr__():
    queue = Queue(maxsize=2)

    assert repr(queue) == "<Queue at %s maxsize=2>" % hex(id(queue))

    queue.put_nowait("item")

    assert repr(queue) == (
        "<Queue at %s maxsize=2 queue=deque(['item']) tasks=1>"
        % hex(id(queue))
    )

# Generated at 2026-10-24 22:38:10.043441
# Unit test for method put of class Queue
def test_Queue_put():
    async def exercise():
        q = Queue(maxsize=1)

        # An item is inserted immediately when capacity is available.
        first_put = q.put("first")
        assert first_put.done()
        await first_put
        assert q.qsize() == 1

        # A second put waits because the queue is full.
        second_put = q.put("second")
        assert not second_put.done()
        assert q.qsize() == 1

        # Removing the first item frees capacity and completes the waiting put.
        assert q.get_nowait() == "first"
        await second_put
        assert q.qsize() == 1
        assert q.get_nowait() == "second"

        # Both accepted puts must be accounted for.
        q.task_done()
        q.task_done()
        await q.join()

    ioloop.IOLoop.current().run_sync(exercise)

# Generated at 2026-10-24 22:38:14.829517
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:38:24.376527
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Enqueue an item immediately.
    queue = Queue(maxsize=1)
    queue.put_nowait("first")

    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()
    assert queue.get_nowait() == "first"

    # A full queue must reject additional items without modifying itself.
    queue.put_nowait("second")
    try:
        queue.put_nowait("third")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "second"

    # Each successful put must be matched by task_done().
    queue.task_done()
    queue.task_done()
    assert queue.join().done()

    # If a getter is waiting, module_0.put_nowait() should satisfy it directly.
    queue = Queue()
    getter = queue.get()

    assert not getter.done()

    queue.put_nowait("item")

    assert getter.done()
    assert getter.result() == "item"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-24 22:38:34.696408
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=2)

    # Items are added immediately while capacity is available.
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.qsize() == 2
    assert queue.full()
    assert queue._unfinished_tasks == 2

    # Adding beyond maxsize raises QueueFull without modifying the queue.
    try:
        queue.put_nowait("third")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 2
    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"

    queue.task_done()
    queue.task_done()
    assert queue.join().done()

    # A waiting getter receives the item directly.
    waiting_queue = Queue(maxsize=1)
    getter = waiting_queue.get()

    assert not getter.done()

    waiting_queue.put_nowait("item")

    assert getter.done()
    assert getter.result() == "item"
    assert waiting_queue.empty()
    assert waiting_queue._unfinished_tasks == 1

    waiting_queue.task_done()
    assert waiting_queue.join().done()

# Generated at 2026-10-24 22:38:41.673115
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    import pytest

    queue = Queue()
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"

    joined = queue.join()
    assert not joined.done()

    queue.task_done()
    assert not joined.done()

    queue.task_done()
    assert joined.done()
    assert joined.result() is None

    with pytest.raises(ValueError, match=r"task_done\(\) called too many times"):
        queue.task_done()

# Generated at 2026-10-24 22:38:51.694706
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=2)

    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.qsize() == 2
    assert queue.full()
    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"

    queue.task_done()
    queue.task_done()

    # A full queue must reject additional items.
    queue.put_nowait("item")
    try:
        queue.put_nowait("overflow")
    except QueueFull:
        pass
    else:
        raise AssertionError("QueueFull was not raised")

    assert queue.get_nowait() == "item"
    queue.task_done()

    # A waiting getter should receive the item immediately.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("waiting-item")

    assert getter.done()
    assert getter.result() == "waiting-item"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-24 22:38:53.109524
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

# Generated at 2026-10-24 22:39:05.006636
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=2)

    # Items are added immediately and retain FIFO order.
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.qsize() == 2
    assert queue.full()
    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"

    queue.task_done()
    queue.task_done()

    # A full queue rejects additional items without modifying its contents.
    queue.put_nowait("existing")
    try:
        queue.put_nowait("extra")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "existing"
    queue.task_done()

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

    # Cancelled getters are discarded instead of receiving new items.
    cancelled_getter = waiting_queue.get()
    cancelled_getter.cancel()

    waiting_queue.put_nowait("retained")

    assert waiting_queue.get_nowait() == "retained"
    waiting_queue.task_done()

# Generated at 2026-10-24 22:39:15.133446
# Unit test for method put of class Queue
def test_Queue_put():
    async def exercise():
        queue = Queue(maxsize=1)

        # An item is inserted immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        await first_put
        assert queue.qsize() == 1

        # A second put waits while the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item admits the waiting putter.
        assert queue.get_nowait() == "first"
        queue.task_done()

        await second_put
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        queue.task_done()

        # Every accepted put has been matched by task_done().
        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(exercise)

# Generated at 2026-10-24 22:39:19.446409
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:39:39.309931
# Unit test for method put of class Queue
def test_Queue_put():
    async def exercise():
        queue = Queue(maxsize=1)

        # An item can be put immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1

        # A second put waits while the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item allows the pending put to complete.
        assert await queue.get() == "first"
        assert await second_put is None
        assert queue.qsize() == 1
        assert await queue.get() == "second"

        queue.task_done()
        queue.task_done()
        await queue.join()

        # A put should deliver directly to an already waiting getter.
        pending_get = queue.get()
        assert not pending_get.done()

        third_put = queue.put("third")
        assert await third_put is None
        assert await pending_get == "third"
        assert queue.empty()

        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(exercise)

# Generated at 2026-10-24 22:39:44.532450
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:40:02.286922
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item is inserted immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1
        assert queue._unfinished_tasks == 1

        # A put waits while the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing an item makes room for the waiting put.
        assert await queue.get() == "first"
        assert await second_put is None
        assert queue.qsize() == 1
        assert await queue.get() == "second"

        queue.task_done()
        queue.task_done()
        assert await queue.join() is None

        # A waiting put raises TimeoutError after its deadline.
        await queue.put("kept")
        timed_put = queue.put(
            "timed-out",
            timeout=ioloop.IOLoop.current().time() - 1,
        )

        try:
            await timed_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.put() did not time out")

        # The timed-out item must never be inserted.
        assert await queue.get() == "kept"
        assert queue.empty()

        queue.task_done()
        assert await queue.join() is None

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:40:06.446516
# Unit test for method put of class Queue
def test_Queue_put():q = Queue(maxsize=1)

# Generated at 2026-10-24 22:40:24.397119
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=2)

    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.qsize() == 2
    assert queue.full()
    assert not queue.empty()

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

    assert queue.empty()
    assert queue.join().done()

    # An item should be delivered directly to a waiting getter.
    waiting_queue = Queue(maxsize=1)
    getter = waiting_queue.get()

    assert not getter.done()

    waiting_queue.put_nowait("item")

    assert getter.done()
    assert getter.result() == "item"
    assert waiting_queue.empty()
    assert not waiting_queue.join().done()

    waiting_queue.task_done()
    assert waiting_queue.join().done()

    # Cancelled getters must not consume subsequently added items.
    cancelled_queue = Queue()
    cancelled_getter = cancelled_queue.get()
    cancelled_getter.cancel()

    cancelled_queue.put_nowait("stored")

    assert cancelled_queue.qsize() == 1
    assert cancelled_queue.get_nowait() == "stored"
    cancelled_queue.task_done()

# Generated at 2026-10-24 22:40:34.094467
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be inserted immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1
        assert queue.full()

        # A second put must wait because the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item makes room for the waiting put.
        assert queue.get_nowait() == "first"
        queue.task_done()

        await second_put
        assert second_put.result() is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"

        queue.task_done()
        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:40:39.523049
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:40:40.924575
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

# Generated at 2026-10-24 22:40:42.388873
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

# Generated at 2026-10-24 22:40:54.368680
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # module_0.get() waits when the queue is empty.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("first")
        assert await pending_get == "first"
        queue.task_done()

        # module_0.get() resolves immediately when an item is available.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        queue.task_done()

        # A timed-out getter must not consume subsequently added items.
        timed_get = queue.get(timeout=datetime.timedelta(milliseconds=1))
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

# Generated at 2026-10-24 22:41:02.638018
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 22:41:13.416168
# Unit test for method get of class Queue
def test_Queue_get():
    async def exercise():
        q = Queue()

        # module_0.get() waits while the queue is empty.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait("first")
        assert await pending_get == "first"
        q.task_done()

        # module_0.get() immediately returns an already queued item.
        q.put_nowait("second")
        assert await q.get() == "second"
        q.task_done()

        # module_0.get() raises TimeoutError if no item arrives before the timeout.
        try:
            await q.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("module_0.get() did not time out")

        # A timed-out getter must not consume a later item.
        q.put_nowait("third")
        assert await q.get() == "third"
        q.task_done()

        await q.join()
        assert q.empty()

    ioloop.IOLoop.current().run_sync(exercise)

# Generated at 2026-10-24 22:41:15.839893
# Unit test for method get of class Queue

# Generated at 2026-10-24 22:41:26.841475
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-24 22:41:38.426668
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import pytest

    queue = Queue(maxsize=1)

    # An item is added immediately when space is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()

    # Adding beyond maxsize fails without modifying the queue.
    with pytest.raises(QueueFull):
        queue.put_nowait("second")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.join().done()

    # A waiting getter receives the item immediately.
    queue = Queue(maxsize=1)
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-24 22:41:48.136044
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # The first put completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        await first_put
        assert queue.qsize() == 1

        # A second put waits because the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item allows the waiting put to complete.
        assert await queue.get() == "first"
        queue.task_done()

        await second_put
        assert queue.qsize() == 1
        assert await queue.get() == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

        # A put should also satisfy a waiting getter directly.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("third")
        assert await pending_get == "third"
        assert queue.empty()

        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:41:52.638777
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:42:02.671575
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        q = Queue(maxsize=1)

        # The first item is inserted immediately.
        await q.put("first")
        assert q.qsize() == 1
        assert q.full()

        # The second put waits because the queue is full.
        pending_put = q.put("second")
        assert not pending_put.done()

        # Removing the first item allows the pending put to complete.
        assert q.get_nowait() == "first"
        q.task_done()

        await pending_put
        assert q.qsize() == 1
        assert q.get_nowait() == "second"
        q.task_done()

        await q.join()
        assert q.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:42:07.690040
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:42:09.058153
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

# Generated at 2026-10-24 22:42:26.030140
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test() -> None:
        q = Queue()

        # An already queued item is returned immediately.
        q.put_nowait("first")
        immediate = q.get()
        assert immediate.done()
        assert await immediate == "first"
        q.task_done()
        assert q.empty()

        # A get on an empty queue waits for a producer.
        pending = q.get()
        assert not pending.done()

        q.put_nowait("second")
        assert await pending == "second"
        q.task_done()
        assert q.empty()

        # A waiting get raises TimeoutError when its timeout expires.
        timed_out = q.get(datetime.timedelta(milliseconds=10))
        try:
            await timed_out
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The expired getter must not consume subsequently added items.
        q.put_nowait("third")
        assert await q.get() == "third"
        q.task_done()
        assert q.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:42:40.765896
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item is inserted immediately when space is available.
        assert queue.put_nowait("first") is None
        assert queue.qsize() == 1
        assert not queue.empty()
        assert queue.full()

        # Inserting into a full queue raises QueueFull.
        try:
            queue.put_nowait("second")
        except QueueFull:
            pass
        else:
            raise AssertionError("QueueFull was not raised")

        assert await queue.get() == "first"
        queue.task_done()
        await queue.join()

        # A waiting getter receives the item directly.
        waiting_queue = Queue()
        getter = waiting_queue.get()
        assert not getter.done()

        waiting_queue.put_nowait("item")

        assert waiting_queue.empty()
        assert await getter == "item"

        waiting_queue.task_done()
        await waiting_queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:42:51.732180
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Enqueues immediately when space is available.
    queue = Queue(maxsize=1)
    queue.put_nowait("first")

    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()
    assert queue.get_nowait() == "first"
    queue.task_done()

    # Raises QueueFull without modifying a full queue.
    queue.put_nowait("existing")
    try:
        queue.put_nowait("extra")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "existing"
    queue.task_done()

    # Delivers directly to a waiting getter.
    waiting_queue = Queue()
    getter = waiting_queue.get()
    assert not getter.done()

    waiting_queue.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert waiting_queue.empty()
    waiting_queue.task_done()

    # Ignores cancelled getters and stores the item normally.
    cancelled_queue = Queue()
    cancelled_getter = cancelled_queue.get()
    cancelled_getter.cancel()

    cancelled_queue.put_nowait("stored")

    assert cancelled_queue.qsize() == 1
    assert cancelled_queue.get_nowait() == "stored"
    cancelled_queue.task_done()

# Generated at 2026-10-24 22:42:53.770234
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

# Generated at 2026-10-24 22:43:11.797078
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    async def run_test():
        q = Queue(maxsize=1)

        # An item is added immediately when space is available.
        q.put_nowait("first")
        assert q.qsize() == 1
        assert q.full()

        # Adding to a full queue raises QueueFull without modifying it.
        try:
            q.put_nowait("second")
        except QueueFull:
            pass
        else:
            raise AssertionError("module_0.put_nowait() did not raise QueueFull")

        assert q.qsize() == 1
        assert q.get_nowait() == "first"
        q.task_done()

        # A waiting getter receives the item immediately.
        getter = q.get()
        assert not getter.done()

        q.put_nowait("third")

        assert getter.done()
        assert await getter == "third"
        assert q.empty()
        q.task_done()

        # Every successfully inserted item has been processed.
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:43:16.056800
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:43:30.409214
# Unit test for method put of class Queue
def test_Queue_put():
    async def exercise():
        queue = Queue(maxsize=1)

        # An item can be inserted immediately while space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1

        # A second put must wait because the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item admits the waiting putter.
        assert queue.get_nowait() == "first"
        await second_put
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"

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
            raise AssertionError("module_0.put() did not time out while the queue was full")

        assert timeout_queue.get_nowait() == "existing"
        assert timeout_queue.empty()
        timeout_queue.task_done()
        await timeout_queue.join()

    ioloop.IOLoop.current().run_sync(exercise)

# Generated at 2026-10-24 22:43:34.343992
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:43:42.499704
# Unit test for method get of class Queue
def test_Queue_get():
    queue = Queue[str]()

    # An available item is returned immediately.
    queue.put_nowait("first")
    result = queue.get()

    assert result.done()
    assert result.result() == "first"
    assert queue.empty()
    queue.task_done()

    # A get on an empty queue waits until an item is added.
    pending = queue.get()

    assert not pending.done()

    queue.put_nowait("second")

    assert pending.done()
    assert pending.result() == "second"
    assert queue.empty()
    queue.task_done()

# Generated at 2026-10-24 22:43:52.648490
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is added immediately when capacity is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()

    # Adding to a full queue raises QueueFull without changing its contents.
    with pytest.raises(QueueFull):
        queue.put_nowait("second")

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

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-24 22:44:01.959479
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be added immediately while space is available.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1

        # A second put waits because the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item makes room and completes the pending put.
        assert queue.get_nowait() == "first"
        queue.task_done()

        await second_put
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:44:07.188703
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:44:16.503387
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue()

        # module_0.get() waits while the queue is empty.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait("first")
        assert await pending_get == "first"
        assert q.empty()
        q.task_done()

        # module_0.get() resolves immediately when an item is available.
        q.put_nowait("second")
        immediate_get = q.get()
        assert await immediate_get == "second"
        assert q.empty()
        q.task_done()

        # module_0.get() raises TimeoutError if no item arrives before the timeout.
        timed_get = q.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("module_0.get() did not time out")

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:44:26.350081
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # Putting into a non-full queue completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        assert await first_put is None
        assert queue.qsize() == 1
        assert queue.full()

        # Putting into a full queue waits for space.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing an item makes room and completes the waiting put.
        assert queue.get_nowait() == "first"
        assert await second_put is None
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        assert queue.empty()

        # Both successfully put items must be marked as completed.
        queue.task_done()
        queue.task_done()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:44:31.160321
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:44:48.254092
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        # An item is inserted immediately when space is available.
        q = Queue(maxsize=1)
        put_future = q.put("first")

        assert put_future.done()
        assert put_future.result() is None
        assert q.qsize() == 1
        assert q.full()

        # A second put waits until the first item is removed.
        blocked_put = q.put("second")
        assert not blocked_put.done()
        assert q.qsize() == 1

        assert await q.get() == "first"
        await blocked_put

        assert q.qsize() == 1
        assert await q.get() == "second"

        q.task_done()
        q.task_done()
        await q.join()

        # A waiting getter receives a newly put item directly.
        direct_q = Queue()
        getter = direct_q.get()
        assert not getter.done()

        await direct_q.put("direct")
        assert await getter == "direct"
        assert direct_q.empty()

        direct_q.task_done()
        await direct_q.join()

        # A blocked put times out without adding its item.
        timeout_q = Queue(maxsize=1)
        await timeout_q.put("held")

        expired_deadline = ioloop.IOLoop.current().time() - 1
        timed_put = timeout_q.put("never-added", timeout=expired_deadline)

        try:
            await timed_put
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("blocked put did not time out")

        assert timeout_q.qsize() == 1
        assert timeout_q.get_nowait() == "held"

        timeout_q.task_done()
        await timeout_q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:44:49.690436
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

# Generated at 2026-10-24 22:45:01.871297
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # Getting from an empty queue should wait for an item.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # Getting an already queued item should complete immediately.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        assert queue.empty()
        queue.task_done()

        # Getting from an empty queue should honor its timeout.
        timed_get = queue.get(datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:45:03.305856
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 22:45:13.020469
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # An item can be put immediately when space is available.
        first_put = queue.put("first")
        assert first_put.done()
        await first_put
        assert queue.qsize() == 1

        # A put waits while the queue is full.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item frees space and completes the waiting put.
        assert queue.get_nowait() == "first"
        queue.task_done()

        assert second_put.done()
        await second_put
        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        queue.task_done()

        # Every successful put has been matched by task_done().
        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:45:17.024456
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)

# Generated at 2026-10-24 22:45:19.446860
# Unit test for method get of class Queue

# Generated at 2026-10-24 22:45:21.867240
# Unit test for method get of class Queue

# Generated at 2026-10-24 22:45:24.429119
# Unit test for method get of class Queue

# Generated at 2026-10-24 22:45:36.175916
# Unit test for method put of class Queue
def test_Queue_put():
    async def run_test():
        queue = Queue(maxsize=1)

        # Putting into a queue with available capacity completes immediately.
        first_put = queue.put("first")
        assert first_put.done()
        assert first_put.result() is None
        assert queue.qsize() == 1
        assert queue.full()

        # Putting into a full queue waits for capacity.
        second_put = queue.put("second")
        assert not second_put.done()
        assert queue.qsize() == 1

        # Removing the first item admits the waiting putter.
        assert queue.get_nowait() == "first"
        await second_put
        queue.task_done()

        assert queue.qsize() == 1
        assert queue.get_nowait() == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-24 22:45:40.667161
# Unit test for method put of class Queue
def test_Queue_put():queue = Queue(maxsize=1)