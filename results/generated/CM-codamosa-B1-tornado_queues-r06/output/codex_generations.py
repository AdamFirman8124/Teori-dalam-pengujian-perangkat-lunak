

# Generated at 2026-10-25 04:15:58.126400
# Unit test for constructor of class QueueFull

# Generated at 2026-10-25 04:16:00.691548
# Unit test for constructor of class QueueFull

# Generated at 2026-10-25 04:16:03.221079
# Unit test for constructor of class QueueFull

# Generated at 2026-10-25 04:16:05.635546
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:16:08.250734
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:16:10.666797
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:16:13.078380
# Unit test for method join of class Queue

# Generated at 2026-10-25 04:16:15.494218
# Unit test for method join of class Queue

# Generated at 2026-10-25 04:16:17.909370
# Unit test for method join of class Queue

# Generated at 2026-10-25 04:16:20.324131
# Unit test for method join of class Queue

# Generated at 2026-10-25 04:16:22.739545
# Unit test for method join of class Queue

# Generated at 2026-10-25 04:16:25.154623
# Unit test for method join of class Queue

# Generated at 2026-10-25 04:16:27.570555
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 04:16:29.984814
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 04:16:37.601734
# Unit test for method __anext__ of class _QueueIterator

# Generated at 2026-10-25 04:16:48.214795
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is inserted immediately when space is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()

    # Inserting into a full queue raises QueueFull without changing it.
    try:
        queue.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("QueueFull was not raised")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.empty()

    # A waiting getter receives the item directly.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert queue.empty()

    queue.task_done()

# Generated at 2026-10-25 04:16:56.714147
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # Getting an already queued item resolves immediately.
        queue.put_nowait("first")
        result = await queue.get()
        assert result == "first"
        assert queue.empty()
        queue.task_done()

        # Getting from an empty queue waits for the next item.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("second")

        assert await pending_get == "second"
        assert queue.empty()
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:17:11.868475
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Items are added immediately when capacity is available.
    queue = Queue(maxsize=2)
    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.qsize() == 2
    assert queue.full()
    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"

    queue.task_done()
    queue.task_done()
    assert queue.join().done()

    # QueueFull is raised without modifying a full queue.
    queue = Queue(maxsize=1)
    queue.put_nowait("existing")

    try:
        queue.put_nowait("rejected")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "existing"
    queue.task_done()
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

# Generated at 2026-10-25 04:17:14.285016
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:17:16.712757
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:17:19.138982
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:17:21.554774
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 04:17:23.969538
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 04:17:26.386239
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 04:17:28.800878
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 04:17:31.216633
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 04:17:33.631993
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 04:17:36.048701
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:17:37.470173
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 04:17:47.520747
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
        assert queue.empty()

        # module_0.get() returns immediately when an item is available.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        queue.task_done()
        assert queue.empty()

        # module_0.get() raises TimeoutError if no item arrives in time.
        try:
            await queue.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:17:57.541445
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

    queue.put_nowait("first")

    # A second put must wait because the queue is full.
    pending_put = queue.put("second")
    assert not pending_put.done()

    # Getting the first item admits the waiting putter.
    assert queue.get_nowait() == "first"
    assert pending_put.done()
    assert pending_put.result() is None

    assert queue.get_nowait() == "second"
    assert queue.empty()

    queue.task_done()
    queue.task_done()

    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")

# Generated at 2026-10-25 04:17:58.868028
# Unit test for method put of class Queue
def test_Queue_put():
    async def run():
        # 1. put on a non-full queue resolves immediately
        q = Queue(maxsize=2)
        await q.put(1)
        assert q.qsize() == 1
        assert not q.empty()

        # 2. put fills it up to maxsize
        await q.put(2)
        assert q.full()

        # 3. put on a full queue blocks, then succeeds after a get
        put_future = q.put(3)
        assert not put_future.done()          # blocked, queue is full
        assert q.qsize() == 2                 # item not yet in the queue
        assert q.get_nowait() == 1
        await gen.sleep(0)                    # let the putter's callback run
        assert put_future.done()
        assert q.qsize() == 2                 # item 3 is now in the queue
        assert q.get_nowait() == 2
        assert q.get_nowait() == 3

        # 4. put with an expired timeout raises TimeoutError
        q2 = Queue(maxsize=1)
        await q2.put("a")
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=0.01)

        # 5. put with timeout=timedelta works too
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=datetime.timedelta(milliseconds=10))

        # 6. blocked put is fulfilled when a getter arrives
        q3 = Queue(maxsize=1)
        await q3.put("a")
        put_future = q3.put("b", timeout=10)
        assert (await q3.get()) == "a"
        await gen.sleep(0)
        assert put_future.done()
        assert q3.get_nowait() == "b"

    IOLoop.current().run_sync(run)

# Generated at 2026-10-25 04:18:00.203430
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 04:18:09.755061
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is added immediately when space is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert queue.full()
    assert not queue.empty()

    # Adding to a full queue raises QueueFull without modifying it.
    try:
        queue.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"
    queue.task_done()

    # A waiting getter receives the item immediately.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("third")

    assert getter.done()
    assert getter.result() == "third"
    assert queue.empty()
    queue.task_done()

    # Cancelled getters are discarded before the item is enqueued.
    cancelled_getter = queue.get()
    cancelled_getter.cancel()

    queue.put_nowait("fourth")
    assert queue.qsize() == 1
    assert queue.get_nowait() == "fourth"
    queue.task_done()

    assert queue.join().done()

# Generated at 2026-10-25 04:18:12.171824
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:18:14.585848
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:18:16.999550
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:18:19.421993
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:18:21.837481
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:18:24.500656
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:18:26.919167
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:18:29.335174
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:18:31.762765
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:18:34.179800
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:18:36.593834
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:18:39.008662
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:18:41.424291
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:18:43.840076
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:18:46.270484
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:18:48.710391
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:18:51.126839
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:18:53.539520
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:18:55.956572
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:18:57.337842
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 04:19:08.249187
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
    assert queue.full()

    # A put on a full queue waits.
    pending_put = queue.put("second")
    assert not pending_put.done()

    # Getting the first item frees space and admits the pending item.
    assert queue.get_nowait() == "first"
    assert pending_put.done()
    assert pending_put.result() is None
    assert queue.full()

    assert queue.get_nowait() == "second"
    assert queue.empty()

    # Both accepted items must be marked as processed.
    queue.task_done()
    queue.task_done()
    assert queue.join().done()

    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() should raise QueueEmpty")

# Generated at 2026-10-25 04:19:18.253742
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # Getting from an empty queue should wait for an item.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # Getting an already queued item should complete immediately.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        queue.task_done()

        # A waiting get should raise TimeoutError when its timeout expires.
        timed_get = queue.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:19:29.290685
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import pytest

    queue = Queue(maxsize=2)

    with pytest.raises(QueueEmpty):
        queue.get_nowait()

    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.get_nowait() == "first"
    assert queue.qsize() == 1
    queue.task_done()

    assert queue.get_nowait() == "second"
    assert queue.empty()
    queue.task_done()

    with pytest.raises(QueueEmpty):
        queue.get_nowait()

    # A waiting putter should be admitted when an item is removed.
    bounded_queue = Queue(maxsize=1)
    bounded_queue.put_nowait("existing")
    pending_put = bounded_queue.put("waiting")

    assert not pending_put.done()
    assert bounded_queue.get_nowait() == "existing"
    assert pending_put.done()
    assert pending_put.result() is None
    assert bounded_queue.get_nowait() == "waiting"

    bounded_queue.task_done()
    bounded_queue.task_done()

# Generated at 2026-10-25 04:19:30.726296
# Unit test for method put of class Queue
def test_Queue_put():
    async def run():
        # 1. put on a non-full queue resolves immediately
        q = Queue(maxsize=2)
        await q.put(1)
        assert q.qsize() == 1
        assert not q.empty()

        # 2. put fills it up to maxsize
        await q.put(2)
        assert q.full()

        # 3. put on a full queue blocks, then succeeds after a get
        put_future = q.put(3)
        assert not put_future.done()          # blocked, queue is full
        assert q.qsize() == 2                 # item not yet in the queue
        assert q.get_nowait() == 1
        await gen.sleep(0)                    # let the putter's callback run
        assert put_future.done()
        assert q.qsize() == 2                 # item 3 is now in the queue
        assert q.get_nowait() == 2
        assert q.get_nowait() == 3

        # 4. put with an expired timeout raises TimeoutError
        q2 = Queue(maxsize=1)
        await q2.put("a")
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=0.01)

        # 5. put with timeout=timedelta works too
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=datetime.timedelta(milliseconds=10))

        # 6. blocked put is fulfilled when a getter arrives
        q3 = Queue(maxsize=1)
        await q3.put("a")
        put_future = q3.put("b", timeout=10)
        assert (await q3.get()) == "a"
        await gen.sleep(0)
        assert put_future.done()
        assert q3.get_nowait() == "b"

    IOLoop.current().run_sync(run)

# Generated at 2026-10-25 04:19:32.082163
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 04:19:42.086588
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue[str]()

        # module_0.get() waits while the queue is empty.
        pending_get = q.get()
        assert not pending_get.done()

        await q.put("first")
        assert await pending_get == "first"
        q.task_done()

        # module_0.get() immediately returns an already queued item.
        await q.put("second")
        immediate_get = q.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        q.task_done()

        assert q.empty()
        await q.join()

        # module_0.get() raises TimeoutError if no item arrives in time.
        try:
            await q.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # A timed-out getter must not consume a subsequently added item.
        await q.put("third")
        assert await q.get() == "third"
        q.task_done()
        await q.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:19:44.505268
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:19:46.920614
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:19:49.334367
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:19:51.748934
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:19:54.164612
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:19:56.581822
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:19:58.996523
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:20:01.411471
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:20:04.006634
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:20:05.342798
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 04:20:06.767175
# Unit test for method put of class Queue
def test_Queue_put():
    async def run():
        # 1. put on a non-full queue resolves immediately
        q = Queue(maxsize=2)
        await q.put(1)
        assert q.qsize() == 1
        assert not q.empty()

        # 2. put fills it up to maxsize
        await q.put(2)
        assert q.full()

        # 3. put on a full queue blocks, then succeeds after a get
        put_future = q.put(3)
        assert not put_future.done()          # blocked, queue is full
        assert q.qsize() == 2                 # item not yet in the queue
        assert q.get_nowait() == 1
        await gen.sleep(0)                    # let the putter's callback run
        assert put_future.done()
        assert q.qsize() == 2                 # item 3 is now in the queue
        assert q.get_nowait() == 2
        assert q.get_nowait() == 3

        # 4. put with an expired timeout raises TimeoutError
        q2 = Queue(maxsize=1)
        await q2.put("a")
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=0.01)

        # 5. put with timeout=timedelta works too
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=datetime.timedelta(milliseconds=10))

        # 6. blocked put is fulfilled when a getter arrives
        q3 = Queue(maxsize=1)
        await q3.put("a")
        put_future = q3.put("b", timeout=10)
        assert (await q3.get()) == "a"
        await gen.sleep(0)
        assert put_future.done()
        assert q3.get_nowait() == "b"

    IOLoop.current().run_sync(run)

# Generated at 2026-10-25 04:20:08.117800
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 04:20:09.532520
# Unit test for method put of class Queue
def test_Queue_put():
    async def run():
        # 1. put on a non-full queue resolves immediately
        q = Queue(maxsize=2)
        await q.put(1)
        assert q.qsize() == 1
        assert not q.empty()

        # 2. put fills it up to maxsize
        await q.put(2)
        assert q.full()

        # 3. put on a full queue blocks, then succeeds after a get
        put_future = q.put(3)
        assert not put_future.done()          # blocked, queue is full
        assert q.qsize() == 2                 # item not yet in the queue
        assert q.get_nowait() == 1
        await gen.sleep(0)                    # let the putter's callback run
        assert put_future.done()
        assert q.qsize() == 2                 # item 3 is now in the queue
        assert q.get_nowait() == 2
        assert q.get_nowait() == 3

        # 4. put with an expired timeout raises TimeoutError
        q2 = Queue(maxsize=1)
        await q2.put("a")
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=0.01)

        # 5. put with timeout=timedelta works too
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=datetime.timedelta(milliseconds=10))

        # 6. blocked put is fulfilled when a getter arrives
        q3 = Queue(maxsize=1)
        await q3.put("a")
        put_future = q3.put("b", timeout=10)
        assert (await q3.get()) == "a"
        await gen.sleep(0)
        assert put_future.done()
        assert q3.get_nowait() == "b"

    IOLoop.current().run_sync(run)

# Generated at 2026-10-25 04:20:10.964850
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 04:20:27.458710
# Unit test for method get of class Queue
def test_Queue_get():
    async def exercise():
        q = Queue()

        # Getting from an empty queue waits until an item is available.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait("first")
        assert await pending_get == "first"
        assert q.empty()
        q.task_done()

        # Getting an already queued item completes immediately.
        q.put_nowait("second")
        immediate_get = q.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        q.task_done()

        await q.join()

        # An empty queue honors the timeout.
        deadline = ioloop.IOLoop.current().time() - 1
        try:
            await q.get(timeout=deadline)
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # A timed-out getter must not consume subsequent items.
        q.put_nowait("third")
        assert await q.get() == "third"
        q.task_done()

    ioloop.IOLoop.current().run_sync(exercise)

# Generated at 2026-10-25 04:20:36.566841
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue(maxsize=1)

        # module_0.get() should immediately return an already queued item.
        await queue.put("first")
        assert await queue.get() == "first"
        queue.task_done()

        # module_0.get() should wait until a new item is available.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("second")
        assert await pending_get == "second"
        queue.task_done()

        await queue.join()
        assert queue.empty()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:20:38.997425
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:20:41.416510
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:20:43.831499
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:20:46.258997
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:20:48.672105
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:20:51.087400
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:20:53.504690
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:20:55.919210
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:20:58.334398
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:21:00.758183
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:21:03.173589
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:21:20.616092
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 04:21:22.014920
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():from tornado.queues import Queue

# Generated at 2026-10-25 04:21:23.352753
# Unit test for method put of class Queue
def test_Queue_put():
    async def run():
        # 1. put on a non-full queue resolves immediately
        q = Queue(maxsize=2)
        await q.put(1)
        assert q.qsize() == 1
        assert not q.empty()

        # 2. put fills it up to maxsize
        await q.put(2)
        assert q.full()

        # 3. put on a full queue blocks, then succeeds after a get
        put_future = q.put(3)
        assert not put_future.done()          # blocked, queue is full
        assert q.qsize() == 2                 # item not yet in the queue
        assert q.get_nowait() == 1
        await gen.sleep(0)                    # let the putter's callback run
        assert put_future.done()
        assert q.qsize() == 2                 # item 3 is now in the queue
        assert q.get_nowait() == 2
        assert q.get_nowait() == 3

        # 4. put with an expired timeout raises TimeoutError
        q2 = Queue(maxsize=1)
        await q2.put("a")
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=0.01)

        # 5. put with timeout=timedelta works too
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=datetime.timedelta(milliseconds=10))

        # 6. blocked put is fulfilled when a getter arrives
        q3 = Queue(maxsize=1)
        await q3.put("a")
        put_future = q3.put("b", timeout=10)
        assert (await q3.get()) == "a"
        await gen.sleep(0)
        assert put_future.done()
        assert q3.get_nowait() == "b"

    IOLoop.current().run_sync(run)

# Generated at 2026-10-25 04:21:24.797134
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 04:21:36.030623
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        q = Queue[str]()

        # module_0.get() returns an already-resolved awaitable when an item is queued.
        q.put_nowait("queued")
        assert await q.get() == "queued"
        assert q.empty()
        q.task_done()

        # module_0.get() waits when the queue is empty and is resolved by a later put.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait("delayed")
        assert await pending_get == "delayed"
        assert q.empty()
        q.task_done()

        # A timed-out getter must not consume subsequently added items.
        try:
            await q.get(timeout=datetime.timedelta(milliseconds=1))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        q.put_nowait("after-timeout")
        assert await q.get() == "after-timeout"
        q.task_done()

        assert q.empty()
        assert q._unfinished_tasks == 0

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:21:37.372210
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 04:21:38.728786
# Unit test for method put of class Queue
def test_Queue_put():
    async def run():
        # 1. put on a non-full queue resolves immediately
        q = Queue(maxsize=2)
        await q.put(1)
        assert q.qsize() == 1
        assert not q.empty()

        # 2. put fills it up to maxsize
        await q.put(2)
        assert q.full()

        # 3. put on a full queue blocks, then succeeds after a get
        put_future = q.put(3)
        assert not put_future.done()          # blocked, queue is full
        assert q.qsize() == 2                 # item not yet in the queue
        assert q.get_nowait() == 1
        await gen.sleep(0)                    # let the putter's callback run
        assert put_future.done()
        assert q.qsize() == 2                 # item 3 is now in the queue
        assert q.get_nowait() == 2
        assert q.get_nowait() == 3

        # 4. put with an expired timeout raises TimeoutError
        q2 = Queue(maxsize=1)
        await q2.put("a")
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=0.01)

        # 5. put with timeout=timedelta works too
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=datetime.timedelta(milliseconds=10))

        # 6. blocked put is fulfilled when a getter arrives
        q3 = Queue(maxsize=1)
        await q3.put("a")
        put_future = q3.put("b", timeout=10)
        assert (await q3.get()) == "a"
        await gen.sleep(0)
        assert put_future.done()
        assert q3.get_nowait() == "b"

    IOLoop.current().run_sync(run)

# Generated at 2026-10-25 04:21:40.068306
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 04:21:50.511959
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

    queue.put_nowait("first")

    # A put on a full queue waits.
    pending_put = queue.put("second")
    assert not pending_put.done()

    # Removing the first item makes room for the waiting put.
    assert queue.get_nowait() == "first"
    queue.task_done()
    assert pending_put.done()
    assert pending_put.result() is None

    assert queue.get_nowait() == "second"
    queue.task_done()
    assert queue.empty()

    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")

# Generated at 2026-10-25 04:21:52.945860
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:21:55.379040
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:21:57.812405
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:22:00.475942
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 04:22:02.890143
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 04:22:05.304801
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 04:22:07.720061
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:22:10.134585
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:22:12.550370
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:22:14.965046
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:22:16.354341
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 04:22:26.954763
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

        # If the queue is empty, module_0.get() waits for the next item.
        waiting = queue.get()
        assert isinstance(waiting, Future)
        assert not waiting.done()

        queue.put_nowait("second")
        assert waiting.done()
        assert await waiting == "second"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:22:28.300032
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 04:22:41.392150
# Unit test for method get of class Queue
def test_Queue_get():
    async def exercise_get():
        q = Queue[str]()

        # An available item is returned immediately.
        q.put_nowait("first")
        assert await q.get() == "first"
        q.task_done()

        # module_0.get() waits when the queue is empty and resolves after a put.
        pending_get = q.get()
        assert not pending_get.done()

        q.put_nowait("second")
        assert await pending_get == "second"
        q.task_done()

        # A waiting get raises TimeoutError after its timeout expires.
        try:
            await q.get(timeout=datetime.timedelta(milliseconds=10))
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

        # The expired getter must not consume subsequently inserted items.
        q.put_nowait("third")
        assert await q.get() == "third"
        q.task_done()

        await q.join()
        assert q.empty()

    ioloop.IOLoop.current().run_sync(exercise_get)

# Generated at 2026-10-25 04:22:42.825171
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 04:22:52.862223
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=2)

    queue.put_nowait("first")
    queue.put_nowait("second")

    assert queue.qsize() == 2
    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"
    assert queue.empty()

    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")

# Generated at 2026-10-25 04:22:54.294345
# Unit test for method put of class Queue
def test_Queue_put():
    async def run():
        # 1. put on a non-full queue resolves immediately
        q = Queue(maxsize=2)
        await q.put(1)
        assert q.qsize() == 1
        assert not q.empty()

        # 2. put fills it up to maxsize
        await q.put(2)
        assert q.full()

        # 3. put on a full queue blocks, then succeeds after a get
        put_future = q.put(3)
        assert not put_future.done()          # blocked, queue is full
        assert q.qsize() == 2                 # item not yet in the queue
        assert q.get_nowait() == 1
        await gen.sleep(0)                    # let the putter's callback run
        assert put_future.done()
        assert q.qsize() == 2                 # item 3 is now in the queue
        assert q.get_nowait() == 2
        assert q.get_nowait() == 3

        # 4. put with an expired timeout raises TimeoutError
        q2 = Queue(maxsize=1)
        await q2.put("a")
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=0.01)

        # 5. put with timeout=timedelta works too
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=datetime.timedelta(milliseconds=10))

        # 6. blocked put is fulfilled when a getter arrives
        q3 = Queue(maxsize=1)
        await q3.put("a")
        put_future = q3.put("b", timeout=10)
        assert (await q3.get()) == "a"
        await gen.sleep(0)
        assert put_future.done()
        assert q3.get_nowait() == "b"

    IOLoop.current().run_sync(run)

# Generated at 2026-10-25 04:22:56.715424
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:22:59.233845
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:23:01.650531
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:23:04.064631
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:23:06.480432
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:23:08.897682
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:23:11.311960
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:23:13.726178
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:23:16.272614
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:23:17.744171
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 04:23:28.497798
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # module_0.get() should wait while the queue is empty.
        pending_get = queue.get()
        assert not pending_get.done()

        # Putting an item should satisfy the waiting getter.
        await queue.put("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # module_0.get() should immediately return an already queued item.
        await queue.put("second")
        assert await queue.get() == "second"
        assert queue.empty()
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:23:42.398642
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # Adds an item immediately when capacity is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert queue.full()
    assert not queue.empty()

    # Raises QueueFull without modifying the queue.
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

    # Delivers directly to a waiting getter.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("second")

    assert getter.done()
    assert getter.result() == "second"
    assert queue.empty()
    queue.task_done()

    # Cancelled getters are ignored.
    cancelled_getter = queue.get()
    cancelled_getter.cancel()
    active_getter = queue.get()

    queue.put_nowait("third")

    assert active_getter.done()
    assert active_getter.result() == "third"
    assert queue.empty()
    queue.task_done()

    assert queue.join().done()

# Generated at 2026-10-25 04:23:52.459619
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # An item already in the queue is returned immediately.
        queue.put_nowait("first")
        assert await queue.get() == "first"
        assert queue.empty()
        queue.task_done()

        # A get on an empty queue waits until an item is added.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("second")
        assert await pending_get == "second"
        queue.task_done()

        # A waiting get raises TimeoutError when its timeout expires.
        timed_get = queue.get(timeout=datetime.timedelta(milliseconds=10))
        try:
            await timed_get
        except gen.TimeoutError:
            pass
        else:
            raise AssertionError("Queue.get() did not time out")

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:23:53.793275
# Unit test for method put of class Queue
def test_Queue_put():
    async def run():
        # 1. put on a non-full queue resolves immediately
        q = Queue(maxsize=2)
        await q.put(1)
        assert q.qsize() == 1
        assert not q.empty()

        # 2. put fills it up to maxsize
        await q.put(2)
        assert q.full()

        # 3. put on a full queue blocks, then succeeds after a get
        put_future = q.put(3)
        assert not put_future.done()          # blocked, queue is full
        assert q.qsize() == 2                 # item not yet in the queue
        assert q.get_nowait() == 1
        await gen.sleep(0)                    # let the putter's callback run
        assert put_future.done()
        assert q.qsize() == 2                 # item 3 is now in the queue
        assert q.get_nowait() == 2
        assert q.get_nowait() == 3

        # 4. put with an expired timeout raises TimeoutError
        q2 = Queue(maxsize=1)
        await q2.put("a")
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=0.01)

        # 5. put with timeout=timedelta works too
        with pytest.raises(TimeoutError):
            await q2.put("b", timeout=datetime.timedelta(milliseconds=10))

        # 6. blocked put is fulfilled when a getter arrives
        q3 = Queue(maxsize=1)
        await q3.put("a")
        put_future = q3.put("b", timeout=10)
        assert (await q3.get()) == "a"
        await gen.sleep(0)
        assert put_future.done()
        assert q3.get_nowait() == "b"

    IOLoop.current().run_sync(run)

# Generated at 2026-10-25 04:23:56.213328
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:23:58.625603
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:24:01.042661
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:03.467786
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:05.884494
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:08.298436
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:24:10.712576
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:24:13.128764
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:24:15.543762
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:17.959552
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:20.387631
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:22.804639
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:25.221484
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:27.637147
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:30.051954
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:24:32.471438
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:24:34.887357
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:24:37.304263
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:24:39.722576
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:24:42.137671
# Unit test for method put of class Queue

# Generated at 2026-10-25 04:24:44.549729
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:46.964853
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:49.392405
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:24:52.804135
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:24:55.220337
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:24:57.635471
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:25:00.049898
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:25:02.467182
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:25:04.883962
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:25:07.301185
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:25:09.716810
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:25:12.133217
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 04:25:14.547213
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:25:16.961868
# Unit test for method get of class Queue

# Generated at 2026-10-25 04:25:19.804965
# Unit test for method get of class Queue
def test_Queue_get():from tornado.queues import Queue

# Generated at 2026-10-25 04:25:30.088929
# Unit test for method get of class Queue
def test_Queue_get():
    queue = Queue()

    # Getting from an empty queue should wait for an item.
    pending_get = queue.get()
    assert not pending_get.done()

    queue.put_nowait("first")
    assert pending_get.done()
    assert pending_get.result() == "first"
    assert queue.empty()
    queue.task_done()

    # Getting an already queued item should complete immediately.
    queue.put_nowait("second")
    immediate_get = queue.get()
    assert immediate_get.done()
    assert immediate_get.result() == "second"
    assert queue.empty()
    queue.task_done()

    assert queue._unfinished_tasks == 0

# Generated at 2026-10-25 04:25:38.648274
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # Getting from an empty queue waits for a producer.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # Getting an already queued item completes immediately.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        assert queue.empty()
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 04:25:40.082764
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 04:25:50.014004
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

    # A put on a full queue waits.
    pending_put = queue.put("second")
    assert not pending_put.done()

    # Retrieving the first item creates room for the pending put.
    assert queue.get_nowait() == "first"
    assert pending_put.done()
    assert pending_put.result() is None

    # The pending item was inserted and can now be retrieved.
    assert queue.get_nowait() == "second"
    assert queue.empty()

    queue.task_done()
    queue.task_done()
    assert queue.join().done()