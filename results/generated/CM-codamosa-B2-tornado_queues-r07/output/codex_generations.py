

# Generated at 2026-10-25 02:56:45.340257
# Unit test for method __str__ of class Queue

# Generated at 2026-10-25 02:56:47.752548
# Unit test for method __str__ of class Queue

# Generated at 2026-10-25 02:56:50.168997
# Unit test for method __str__ of class Queue

# Generated at 2026-10-25 02:56:52.581046
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-25 02:56:54.993165
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-25 02:56:57.409983
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-25 02:56:59.832143
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 02:57:02.250005
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 02:57:04.665239
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 02:57:07.078427
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-25 02:57:09.491697
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-25 02:57:11.904647
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-25 02:57:14.318384
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 02:57:16.731640
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 02:57:21.880379
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():queue = Queue(maxsize=1)

# Generated at 2026-10-25 02:57:30.282083
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

# Generated at 2026-10-25 02:57:41.131759
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 02:57:43.559786
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 02:57:45.975729
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 02:57:48.392537
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 02:57:50.809104
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:57:53.224244
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:57:55.640894
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:57:58.060855
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 02:58:00.474979
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 02:58:02.890163
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 02:58:05.305500
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:58:07.722685
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:58:10.139792
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:58:12.555596
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 02:58:14.977197
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 02:58:17.392892
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 02:58:19.807405
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 02:58:22.222397
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 02:58:24.638770
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 02:58:27.053869
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:58:29.471397
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:58:31.888571
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:58:34.305041
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 02:58:36.724549
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 02:58:39.140624
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 02:58:41.557281
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:58:43.972788
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:58:46.386708
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:58:48.804506
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:58:51.218620
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:58:53.632629
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:59:19.335778
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:59:21.752285
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:59:24.167572
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:59:26.582954
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:59:28.998245
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:59:31.412681
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:59:33.827112
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 02:59:36.241895
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 02:59:38.657212
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 02:59:41.071465
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 02:59:43.486958
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 02:59:45.901722
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 02:59:48.316748
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:59:50.731600
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:59:53.146173
# Unit test for method get of class Queue

# Generated at 2026-10-25 02:59:55.561512
# Unit test for method put of class Queue

# Generated at 2026-10-25 02:59:57.977669
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:00:00.392831
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:00:02.807743
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:00:05.224242
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:00:07.638342
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:00:10.051895
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:00:12.466088
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:00:14.881588
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:00:17.296581
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:00:19.717195
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:00:22.136355
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:00:24.550624
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:00:26.966272
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:00:29.380979
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:00:31.796231
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:00:34.211395
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:00:36.628339
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:00:39.041639
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:00:41.456893
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:00:43.873829
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:00:46.290612
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:00:48.706221
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:00:51.121417
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:01:15.228008
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:01:16.608776
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 03:01:24.979295
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue[str]()

        # module_0.get() should wait while the queue is empty.
        pending_get = queue.get()
        assert not pending_get.done()

        queue.put_nowait("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # module_0.get() should return immediately when an item is available.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        assert queue.empty()
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 03:01:27.395985
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:01:29.809246
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:01:32.222911
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:01:34.637618
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:01:37.051123
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:01:39.465017
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:01:41.879584
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:01:44.292949
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:01:46.706748
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:01:49.121671
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:01:51.535464
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:01:53.948842
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:01:56.366357
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:01:58.780228
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:02:01.205615
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:02:03.618261
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:02:06.030706
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:02:08.443866
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:02:10.857686
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:02:13.274790
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:02:15.689121
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:02:18.106491
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:02:20.520444
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:02:22.933744
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:02:25.348490
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:02:27.762102
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:02:30.176010
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:02:32.588948
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:02:35.004998
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:02:37.419583
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:02:39.835609
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:02:42.251819
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:02:52.020470
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=1)

    queue.put_nowait("first")
    pending_put = queue.put("second")

    assert not pending_put.done()
    assert queue.get_nowait() == "first"

    # Removing the first item should admit the waiting putter.
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

# Generated at 2026-10-25 03:02:53.454023
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

# Generated at 2026-10-25 03:02:54.885923
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 03:03:09.838178
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    # An item is added immediately when space is available.
    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert queue.full()
    assert queue.get_nowait() == "first"
    queue.task_done()

    # A full queue raises QueueFull without modifying its contents.
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

    # A waiting getter is fulfilled directly.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("delivered")
    assert getter.done()
    assert getter.result() == "delivered"
    assert queue.empty()
    queue.task_done()

    # Completed/cancelled getters are ignored.
    cancelled_getter = queue.get()
    cancelled_getter.cancel()

    queue.put_nowait("after-cancel")
    assert queue.qsize() == 1
    assert queue.get_nowait() == "after-cancel"
    queue.task_done()

    assert queue.join().done()

# Generated at 2026-10-25 03:03:12.257987
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:03:14.672657
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:03:17.208003
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:03:19.624107
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:03:22.038281
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:03:24.454662
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:03:26.868640
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:03:29.282005
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:03:31.728048
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:03:34.111507
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:03:36.526472
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:03:38.940962
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:03:41.354363
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:03:43.768688
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:03:46.184781
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:03:48.600062
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:03:51.017512
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:03:53.429197
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:03:55.845219
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:03:58.293789
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 03:04:03.523938
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():queue = Queue(maxsize=1)

# Generated at 2026-10-25 03:04:04.861733
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

# Generated at 2026-10-25 03:04:06.249849
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 03:04:21.724863
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # An item is added immediately when capacity is available.
    q = Queue(maxsize=1)
    q.put_nowait("first")

    assert q.qsize() == 1
    assert not q.empty()
    assert q.full()

    join_future = q.join()
    assert not join_future.done()

    # Adding another item to a full queue raises QueueFull and does not
    # modify the existing item.
    try:
        q.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("QueueFull was not raised")

    assert q.qsize() == 1
    assert q.get_nowait() == "first"

    q.task_done()
    assert join_future.done()
    assert join_future.result() is None

    # A waiting getter receives the item directly.
    q = Queue(maxsize=1)
    getter = q.get()
    assert not getter.done()

    q.put_nowait("direct")

    assert getter.done()
    assert getter.result() == "direct"
    assert q.empty()

    q.task_done()
    assert q.join().done()

    # Cancelled getters are discarded before inserting an item.
    cancelled_getter = q.get()
    cancelled_getter.cancel()

    q.put_nowait("queued")

    assert q.qsize() == 1
    assert q.get_nowait() == "queued"
    q.task_done()

# Generated at 2026-10-25 03:04:23.098625
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

# Generated at 2026-10-25 03:04:24.487947
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 03:04:27.031033
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:04:29.445623
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:04:31.871550
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:04:34.626147
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:04:37.042056
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:04:39.458922
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:04:41.873687
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:04:44.288954
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:04:46.703135
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:04:49.118001
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:04:51.532498
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:04:53.946880
# Unit test for method get of class Queue

# Generated at 2026-10-25 03:04:56.362611
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:04:58.777317
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:05:01.191683
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:05:03.606235
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:05:06.022602
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:05:08.435677
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:05:10.851992
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:05:13.270606
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:05:15.686304
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:05:18.108941
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:05:20.519895
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:05:22.933990
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:05:25.352375
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:05:35.962070
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():from tornado.queues import Queue

# Generated at 2026-10-25 03:05:45.624810
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # module_0.get() should wait while the queue is empty.
        pending_get = queue.get()
        assert not pending_get.done()

        # A subsequently added item should satisfy the waiting getter.
        queue.put_nowait("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # Available items should be returned immediately in FIFO order.
        queue.put_nowait("second")
        queue.put_nowait("third")

        assert await queue.get() == "second"
        queue.task_done()

        assert await queue.get() == "third"
        queue.task_done()

        assert queue.empty()
        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 03:05:57.478411
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=2)

    # Items are returned in FIFO order.
    queue.put_nowait("first")
    queue.put_nowait("second")
    assert queue.qsize() == 2
    assert queue.get_nowait() == "first"
    assert queue.get_nowait() == "second"
    assert queue.empty()

    # An empty queue raises QueueEmpty.
    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")

    # A waiting putter is admitted when an item is removed.
    queue = Queue(maxsize=1)
    queue.put_nowait("current")
    pending_put = queue.put("waiting")

    assert not pending_put.done()
    assert queue.get_nowait() == "current"
    assert pending_put.done()
    assert pending_put.result() is None
    assert queue.get_nowait() == "waiting"

    # Both successfully enqueued items must be accounted for.
    queue.task_done()
    queue.task_done()
    assert queue._unfinished_tasks == 0

# Generated at 2026-10-25 03:06:09.448374
# Unit test for method get of class Queue
def test_Queue_get():
    async def run_test():
        queue = Queue()

        # module_0.get() waits when the queue is empty.
        pending_get = queue.get()
        assert not pending_get.done()

        await queue.put("first")
        assert await pending_get == "first"
        assert queue.empty()
        queue.task_done()

        # module_0.get() resolves immediately when an item is available.
        queue.put_nowait("second")
        immediate_get = queue.get()
        assert immediate_get.done()
        assert await immediate_get == "second"
        assert queue.empty()
        queue.task_done()

        # Multiple waiting getters receive items in FIFO order.
        first_getter = queue.get()
        second_getter = queue.get()

        queue.put_nowait(1)
        queue.put_nowait(2)

        assert await first_getter == 1
        assert await second_getter == 2
        queue.task_done()
        queue.task_done()

        await queue.join()

    ioloop.IOLoop.current().run_sync(run_test)

# Generated at 2026-10-25 03:06:10.781658
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

# Generated at 2026-10-25 03:06:13.427163
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:06:15.952598
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:06:18.369949
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:06:20.781403
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:06:23.313566
# Unit test for method put of class Queue

# Generated at 2026-10-25 03:06:25.728933
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 03:06:27.192033
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():from tornado.queues import Queue

# Generated at 2026-10-25 03:06:37.711055
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue(maxsize=1)

    queue.put_nowait("first")
    assert queue.qsize() == 1
    assert not queue.empty()
    assert queue.full()

    try:
        queue.put_nowait("second")
    except QueueFull:
        pass
    else:
        raise AssertionError("module_0.put_nowait() did not raise QueueFull")

    assert queue.get_nowait() == "first"
    queue.task_done()
    assert queue.empty()
    assert queue.join().done()

    # A waiting getter should receive the item immediately.
    getter = queue.get()
    assert not getter.done()

    queue.put_nowait("direct")
    assert getter.done()
    assert getter.result() == "direct"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()

# Generated at 2026-10-25 03:06:48.770445
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

    # Removing an item from a full queue admits the first waiting putter.
    queue.put_nowait("second")
    pending_put = queue.put("third")

    assert not pending_put.done()
    assert queue.get_nowait() == "second"
    assert pending_put.done()
    assert pending_put.result() is None

    # The waiting putter's item is now available.
    assert queue.get_nowait() == "third"
    queue.task_done()
    queue.task_done()
    assert queue.empty()

    # Cancelled putters are ignored.
    queue.put_nowait("fourth")
    cancelled_put = queue.put("cancelled")
    cancelled_put.cancel()

    assert queue.get_nowait() == "fourth"
    queue.task_done()
    assert queue.empty()

    try:
        queue.get_nowait()
    except QueueEmpty:
        pass
    else:
        raise AssertionError("module_0.get_nowait() did not raise QueueEmpty")