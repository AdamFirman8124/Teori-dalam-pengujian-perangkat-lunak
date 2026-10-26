

# Generated at 2026-10-25 09:58:46.606235
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-25 09:58:49.022790
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-25 09:58:51.436118
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-25 09:58:53.853249
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:58:56.269767
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:58:58.683213
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:59:01.100697
# Unit test for constructor of class Queue

# Generated at 2026-10-25 09:59:03.519626
# Unit test for constructor of class Queue

# Generated at 2026-10-25 09:59:05.927849
# Unit test for constructor of class Queue

# Generated at 2026-10-25 09:59:08.347679
# Unit test for method join of class Queue

# Generated at 2026-10-25 09:59:10.789425
# Unit test for method join of class Queue

# Generated at 2026-10-25 09:59:13.198305
# Unit test for method join of class Queue

# Generated at 2026-10-25 09:59:15.613430
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 09:59:18.030152
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 09:59:33.913263
# Unit test for method __anext__ of class _QueueIterator
def test__QueueIterator___anext__():from tornado.queues import Queue, _QueueIterator

# Generated at 2026-10-25 09:59:52.036825
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 09:59:54.588582
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:59:57.007157
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:59:59.423414
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:01.836404
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:04.347910
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:06.762642
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:09.181172
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:11.598396
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:14.011406
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:16.426715
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:00:18.841851
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:00:21.255390
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:00:23.669513
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:00:26.085684
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:00:28.502428
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:00:30.917406
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:00:33.331048
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:00:35.744233
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:00:38.159846
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:00:40.573641
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:00:42.987763
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:00:45.405535
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:00:47.823187
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:00:50.236616
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:00:52.650383
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:55.064501
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:57.481439
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:00:59.898891
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:01:02.309712
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:01:04.723166
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:01:07.137949
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:01:33.325458
# Unit test for method put of class Queue
def test_Queue_put():q = Queue(maxsize=2)

# Generated at 2026-10-25 10:01:44.896276
# Unit test for method full of class Queue
def test_Queue_full():
    # maxsize=0 means unbounded: never full
    q = Queue(maxsize=0)
    assert q.full() is False
    assert q.empty() is True

    q.put_nowait(1)
    assert q.full() is False
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.qsize() == 3
    assert q.full() is False

    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    assert q.full() is False

    # bounded queue: full when qsize() >= maxsize
    q2 = Queue(maxsize=2)
    assert q2.maxsize == 2
    assert q2.full() is False

    q2.put_nowait("a")
    assert q2.qsize() == 1
    assert q2.full() is False

    q2.put_nowait("b")
    assert q2.qsize() == 2
    assert q2.full() is True

    # removing one item makes it not full again
    assert q2.get_nowait() == "a"
    assert q2.full() is False

    q2.get_nowait()
    assert q2.empty() is True
    assert q2.full() is False

    # maxsize=1 boundary
    q3 = Queue(maxsize=1)
    assert q3.full() is False
    q3.put_nowait("x")
    assert q3.full() is True
    q3.get_nowait()
    assert q3.full() is False

    # subclasses inherit module_0.full()
    pq = PriorityQueue(maxsize=1)
    assert pq.full() is False
    pq.put_nowait(5)
    assert pq.full() is True

    lq = LifoQueue(maxsize=1)
    assert lq.full() is False
    lq.put_nowait(5)
    assert lq.full() is True

# Generated at 2026-10-25 10:01:47.045853
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

# Generated at 2026-10-25 10:01:48.555272
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

# Generated at 2026-10-25 10:01:50.118097
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

# Generated at 2026-10-25 10:01:51.512507
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

# Generated at 2026-10-25 10:02:37.018037
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop
    q = Queue()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()
    try:
        q.task_done()
        raise AssertionError("module_0.task_done() on empty queue should raise ValueError")
    except ValueError:
        pass
    q.put_nowait(1)
    assert q._unfinished_tasks == 1
    assert not q._finished.is_set()
    q.put_nowait(2)
    assert q._unfinished_tasks == 2
    assert not q._finished.is_set()
    assert q.get_nowait() == 1
    assert q._unfinished_tasks == 2
    q.task_done()
    assert q._unfinished_tasks == 1
    assert not q._finished.is_set()
    assert q.get_nowait() == 2
    q.task_done()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()
    try:
        q.task_done()
        raise AssertionError("extra module_0.task_done() should raise ValueError")
    except ValueError:
        pass
    assert q._unfinished_tasks == 0
    async def check_join():
        q2 = Queue()
        await q2.put("a")
        await q2.put("b")
        assert q2._unfinished_tasks == 2
        item1 = await q2.get()
        assert item1 == "a"
        assert q2._unfinished_tasks == 2
        q

# Generated at 2026-10-25 10:02:38.450053
# Unit test for method full of class Queue
def test_Queue_full():
    # maxsize=0 means unbounded: never full
    q = Queue(maxsize=0)
    assert q.full() is False
    assert q.empty() is True

    q.put_nowait(1)
    assert q.full() is False
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.qsize() == 3
    assert q.full() is False

    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    assert q.full() is False

    # bounded queue: full when qsize() >= maxsize
    q2 = Queue(maxsize=2)
    assert q2.maxsize == 2
    assert q2.full() is False

    q2.put_nowait("a")
    assert q2.qsize() == 1
    assert q2.full() is False

    q2.put_nowait("b")
    assert q2.qsize() == 2
    assert q2.full() is True

    # removing one item makes it not full again
    assert q2.get_nowait() == "a"
    assert q2.full() is False

    q2.get_nowait()
    assert q2.empty() is True
    assert q2.full() is False

    # maxsize=1 boundary
    q3 = Queue(maxsize=1)
    assert q3.full() is False
    q3.put_nowait("x")
    assert q3.full() is True
    q3.get_nowait()
    assert q3.full() is False

    # subclasses inherit module_0.full()
    pq = PriorityQueue(maxsize=1)
    assert pq.full() is False
    pq.put_nowait(5)
    assert pq.full() is True

    lq = LifoQueue(maxsize=1)
    assert lq.full() is False
    lq.put_nowait(5)
    assert lq.full() is True

# Generated at 2026-10-25 10:02:39.883990
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

# Generated at 2026-10-25 10:02:45.004449
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 10:02:47.564274
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

# Generated at 2026-10-25 10:02:49.099625
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

# Generated at 2026-10-25 10:03:23.537160
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:03:33.350127
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 10:03:34.873507
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

# Generated at 2026-10-25 10:03:37.842636
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 10:03:39.379607
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

# Generated at 2026-10-25 10:03:40.915482
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

# Generated at 2026-10-25 10:03:55.432670
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():queue = Queue(maxsize=1)


# Generated at 2026-10-25 10:03:58.423967
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:04:06.618524
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 10:04:09.035450
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:04:11.458615
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:04:13.869020
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:04:16.283858
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:04:23.626726
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():q = Queue(maxsize=2)

# Generated at 2026-10-25 10:04:25.151598
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

# Generated at 2026-10-25 10:04:26.701068
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

# Generated at 2026-10-25 10:04:29.554335
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:04:30.988319
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 10:04:47.468040
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

# Generated at 2026-10-25 10:04:50.443772
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 10:04:53.288809
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 10:04:55.705746
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:04:58.241668
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:05:00.657467
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 10:05:03.865432
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:05:06.437422
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:05:08.853395
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:05:11.269119
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:05:13.833134
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:05:16.249569
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:05:18.666972
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:05:40.213645
# Unit test for method get of class Queue
def test_Queue_get():queue = Queue()

# Generated at 2026-10-25 10:05:55.979922
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():q = Queue(maxsize=2)

assert q.empty()
assert q.qsize() == 0

q.put_nowait("first")
q.put_nowait("second")

assert not q.empty()
assert q.qsize() == 2
assert q.full()
assert q.get_nowait() == "first"
assert q.qsize() == 1

q.put_nowait("third")
assert q.qsize() == 2

try:
    q.put_nowait("fourth")
except QueueFull:
    pass
else:
    raise AssertionError("module_0.put_nowait() did not raise QueueFull")

assert q.get_nowait() == "second"
assert q.get_nowait() == "third"
assert q.empty()

waiting_queue = Queue()
getter = waiting_queue.get()

assert not getter.done()
waiting_queue.put_nowait("delivered")
assert getter.result() == "delivered"
assert waiting_queue.empty()

# Generated at 2026-10-25 10:05:59.113842
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 10:06:04.479851
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:06:06.018769
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 10:06:07.484886
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

# Generated at 2026-10-25 10:06:11.650102
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 10:06:17.796062
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:06:20.207860
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:06:30.983615
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 10:06:40.327504
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:06:41.865808
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 10:06:44.724002
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 10:06:49.049275
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

# Generated at 2026-10-25 10:07:48.827408
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

# Generated at 2026-10-25 10:07:51.795153
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:07:53.229900
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 10:07:56.597664
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:07:59.275816
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:08:01.691528
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:08:04.394128
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:08:06.808806
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:08:09.222387
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:08:11.638356
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:08:14.428977
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:08:16.846028
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:08:19.377965
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:08:21.792107
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:08:24.235893
# Unit test for method put of class Queue

# Generated at 2026-10-25 10:08:26.651492
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:08:29.067484
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 10:08:31.046137
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():q = Queue(maxsize=2)

# Generated at 2026-10-25 10:08:33.984594
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull, QueueEmpty
    # basic put into unbounded queue

# Generated at 2026-10-25 10:08:39.002728
# Unit test for method get of class Queue

# Generated at 2026-10-25 10:08:40.435769
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 10:08:58.152653
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