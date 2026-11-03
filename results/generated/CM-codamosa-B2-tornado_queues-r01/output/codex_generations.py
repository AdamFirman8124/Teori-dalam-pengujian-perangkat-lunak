

# Generated at 2026-11-02 10:38:24.613387
# Unit test for constructor of class LifoQueue
def test_LifoQueue():
    # Default construction: unbounded queue, empty internals.
    q = LifoQueue()
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()
    assert q._queue == []

    # Custom maxsize is stored.
    q2 = LifoQueue(maxsize=3)
    assert q2.maxsize == 3
    assert q2.empty()
    assert not q2.full()

    # maxsize=None is rejected.
    try:
        LifoQueue(maxsize=None)
    except TypeError:
        pass
    else:
        raise AssertionError("TypeError not raised for maxsize=None")

    # Negative maxsize is rejected.
    try:
        LifoQueue(maxsize=-1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError not raised for negative maxsize")

    # LIFO behavior right after construction.
    q3 = LifoQueue()
    q3.put(1)
    q3.put(2)
    assert q3.qsize() == 2
    assert q3.full() is False  # unbounded
    assert q3.get_nowait() == 2
    assert q3.get_nowait() == 1
    assert q3.empty()

    # Bounded queue reports full when maxsize reached.
    q4 = LifoQueue(maxsize=1)
    q4.put_nowait("a")
    assert q4.full()
    try:
        q4.put_nowait("b")
    except QueueFull:
        pass
    else:
        raise AssertionError("QueueFull not raised when full")

# Generated at 2026-11-02 10:39:37.766235
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.queues import Queue, QueueEmpty

    # get_nowait on an empty queue raises QueueEmpty
    q = Queue()
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # get_nowait returns items in FIFO order
    q = Queue(maxsize=3)
    for item in range(3):
        q.put_nowait(item)
    assert q.qsize() == 3
    assert q.get_nowait() == 0
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.empty()

    # empty queue again raises QueueEmpty
    try:
        q.get_nowait()
        assert False, "expected QueueEmpty"
    except QueueEmpty:
        pass

    # When the queue is full and a putter is waiting, get_nowait
    # returns the oldest queued item and resolves the waiting putter.
    q = Queue(maxsize=1)
    q.put_nowait("a")
    putter_future = q.put("b")
    assert not putter_future.done()
    assert q.full()

    assert q.get_nowait() == "a"
    assert putter_future.done()
    assert q.qsize() == 1
    assert not q.full()

    # The item from the waiting putter is now in the queue.
    assert q.get_nowait() == "b"
    assert q.empty()

# Generated at 2026-11-02 10:41:17.364786
# Unit test for constructor of class Queue
def test_Queue():
    # Default constructor: unbounded queue
    q = Queue()
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()

    # Custom maxsize
    q2 = Queue(maxsize=5)
    assert q2.maxsize == 5
    assert q2.empty()
    assert not q2.full()

    # maxsize=1 is allowed
    q3 = Queue(maxsize=1)
    assert q3.maxsize == 1
    assert not q3.full()

    # maxsize=None raises TypeError
    try:
        Queue(maxsize=None)
    except TypeError:
        pass
    else:
        raise AssertionError("expected TypeError for maxsize=None")

    # Negative maxsize raises ValueError
    try:
        Queue(maxsize=-1)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for negative maxsize")

    # Internal state initialized correctly
    q4 = Queue(maxsize=2)
    assert q4._unfinished_tasks == 0
    assert len(q4._getters) == 0
    assert len(q4._putters) == 0
    # _finished event starts set (no pending tasks)
    assert q4._finished.is_set()

# Generated at 2026-11-02 10:43:18.815906
# Unit test for method __repr__ of class Queue
def test_Queue___repr__():
    import datetime

    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    # Empty queue with default (unbounded) maxsize.
    q0 = Queue()
    r0 = repr(q0)
    assert r0.startswith("<Queue at 0x"), r0
    assert r0.endswith(" maxsize=0>"), r0
    assert "queue=" not in r0
    assert "getters" not in r0
    assert "putters" not in r0
    assert "tasks=" not in r0

    # Queue with items, a maxsize, and unfinished tasks.
    q1 = Queue(maxsize=3)
    q1.put_nowait(1)
    q1.put_nowait("x")
    r1 = repr(q1)
    assert r1.startswith("<Queue at 0x"), r1
    assert "maxsize=3" in r1
    assert "queue=deque([1, 'x'])" in r1
    assert "tasks=2" in r1
    assert "getters" not in r1
    assert "putters" not in r1

    # str() omits the id but keeps the same details.
    s1 = str(q1)
    assert s1 == "<Queue maxsize=3 queue=deque([1, 'x']) tasks=2>", s1

    # A timed-out getter is still counted by repr (until consumed).
    q2 = Queue()

    async def getter():
        try:
            await q2.get(timeout=datetime.timedelta(seconds=0.01))
        except gen.TimeoutError:
            pass

    IOLoop.current().run_sync(getter)
    assert "getters[1]" in repr(q2), repr(q2)

    # A timed-out putter is still counted by repr (until consumed).
    q3 = Queue(maxsize=1)
    q3.put_nowait("a")

    async def putter():
        try:
            await q3.put("b", timeout=datetime.timedelta(seconds=0.01))
        except gen.TimeoutError:
            pass

    IOLoop.current().run_sync(putter)
    r3 = repr(q3)
    assert "putters[1]" in r3, r3
    assert "tasks=1" in r3, r3
    assert "queue=deque(['a'])" in r3, r3

    print("test_Queue___repr__ passed")

# Generated at 2026-11-02 10:44:47.288678
# Unit test for method __repr__ of class Queue
def test_Queue___repr__():
    # Empty queue with default maxsize
    q = Queue()
    r = repr(q)
    assert r.startswith("<Queue at 0x"), r
    assert "maxsize=0" in r, r
    assert r.endswith(">"), r
    # No extra fields for an empty, idle queue
    assert "queue=" not in r, r
    assert "getters[" not in r, r
    assert "putters[" not in r, r
    assert "tasks=" not in r, r

    # Queue with maxsize set and items in it
    q2 = Queue(maxsize=5)
    q2.put_nowait("a")
    q2.put_nowait("b")
    r2 = repr(q2)
    assert "maxsize=5" in r2, r2
    assert "queue=deque(['a', 'b'])" in r2, r2
    assert "tasks=2" in r2, r2

    # Queue with waiting getters and putters
    q3 = Queue(maxsize=1)
    q3.put_nowait(1)
    getter_future = q3.get()  # queues a getter (queue is full)
    putter_future = q3.put(2)  # queues a putter (queue is full)
    r3 = repr(q3)
    assert "getters[1]" in r3, r3
    assert "putters[1]" in r3, r3
    assert "maxsize=1" in r3, r3

    # Cleanup: resolve pending futures
    getter_future.cancel()
    putter_future.cancel()
    q3._consume_expired()

# Generated at 2026-11-02 10:47:01.641583
# Unit test for method put of class Queue
def test_Queue_put():
    async def _inner():
        # Unbounded queue: put resolves immediately.
        q = Queue()
        fut = q.put(0)
        assert fut.done()
        await fut
        assert q.qsize() == 1

        # Bounded queue with room: put succeeds.
        q = Queue(maxsize=2)
        await q.put(1)
        await q.put(2)
        assert q.qsize() == 2
        assert q.full()

        # Full queue: put blocks until an item is consumed.
        blocked = q.put(3)
        assert not blocked.done()
        assert len(q._putters) == 1
        assert q.get_nowait() == 1
        await blocked
        assert q.qsize() == 2
        assert list(q._queue) == [2, 3]

        # Full queue with a numeric timeout: raises TimeoutError.
        try:
            await q.put(4, timeout=0.01)
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("expected TimeoutError")
        assert q.qsize() == 2

        # Full queue with a timedelta timeout: raises TimeoutError.
        try:
            await q.put(5, timeout=datetime.timedelta(seconds=0.01))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("expected TimeoutError")
        assert q.qsize() == 2

    ioloop.IOLoop.current().run_sync(_inner)