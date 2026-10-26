

# Generated at 2026-10-25 09:28:59.743258
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

    # task_done without a matching put must raise ValueError.

# Generated at 2026-10-25 09:29:02.161289
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:29:06.319371
# Unit test for method put of class Queue
def test_Queue_put():q = Queue()

# Generated at 2026-10-25 09:29:24.568189
# Unit test for method __aiter__ of class Queue
def test_Queue___aiter__():
    from tornado.queues import Queue, _QueueIterator
    from tornado.ioloop import IOLoop

    q = Queue[int]()

    # __aiter__ must return a _QueueIterator bound to this queue
    it1 = q.__aiter__()
    assert isinstance(it1, _QueueIterator)
    assert it1.q is q

    # Each call must return

# Generated at 2026-10-25 09:29:46.115088
# Unit test for method __aiter__ of class Queue
def test_Queue___aiter__():q = Queue()

# Generated at 2026-10-25 09:29:48.530904
# Unit test for constructor of class QueueFull

# Generated at 2026-10-25 09:29:51.236634
# Unit test for constructor of class QueueFull

# Generated at 2026-10-25 09:29:53.651558
# Unit test for constructor of class QueueFull

# Generated at 2026-10-25 09:29:56.065573
# Unit test for constructor of class Queue

# Generated at 2026-10-25 09:29:58.480679
# Unit test for constructor of class Queue

# Generated at 2026-10-25 09:30:00.895383
# Unit test for constructor of class Queue

# Generated at 2026-10-25 09:30:03.308847
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:30:05.738316
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:30:08.151875
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:30:10.567403
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:30:12.982883
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:30:15.397244
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:30:17.813601
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:30:20.231973
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:30:22.650196
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:30:25.061926
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:30:27.475942
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:30:29.890356
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:30:32.607218
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:30:33.941442
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-25 09:30:35.370425
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

# Generated at 2026-10-25 09:30:38.368361
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

# Generated at 2026-10-25 09:31:57.188717
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():queue = Queue(maxsize=1)


# Generated at 2026-10-25 09:32:00.160312
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

    # task_done without a matching put must raise ValueError.

# Generated at 2026-10-25 09:32:01.568931
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

# Generated at 2026-10-25 09:32:02.994743
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

# Generated at 2026-10-25 09:32:04.378570
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 09:32:05.996807
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 09:32:08.691102
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:32:11.107084
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:32:13.521879
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:32:15.937439
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:32:18.351676
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:32:20.866148
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:32:23.207383
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:32:25.619209
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:32:28.032252
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:32:30.448992
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:32:32.862850
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:32:35.279125
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:32:37.691833
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:32:40.105237
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:32:42.789961
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:32:45.206727
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:32:47.619400
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:32:50.035962
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:32:52.448595
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:32:54.912877
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:32:57.312043
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:32:59.728656
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:33:02.142481
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:33:04.555945
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:33:06.974299
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:33:09.388365
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:33:11.837279
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:33:14.251121
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:33:16.665128
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:33:19.090431
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:33:21.517062
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:33:23.928689
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:33:26.344156
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:33:28.761540
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:33:31.174591
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:33:33.588996
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:33:36.004111
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:33:38.420810
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:33:40.844056
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:33:43.250780
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:33:45.664897
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:33:48.082225
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:33:50.495624
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:33:52.911210
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:33:55.325036
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:33:57.741790
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:34:00.155970
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:34:02.570724
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:34:04.986577
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:34:07.399565
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:34:09.815714
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:34:12.230259
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:34:14.644744
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:34:17.060176
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:34:19.474476
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:34:21.889294
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:34:24.303381
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:34:26.719869
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:34:29.135145
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:34:31.549159
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:34:33.963347
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:34:36.378580
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:34:38.793411
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:34:41.210436
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:34:43.627070
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:34:46.045550
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:34:48.457907
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:34:50.872563
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:34:53.287359
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:34:55.701533
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:34:58.115075
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:35:00.518491
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:35:02.932831
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:35:05.348634
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:35:07.762319
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:35:10.177460
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:35:12.592433
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:35:15.008071
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:35:17.422522
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:35:19.840989
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:35:22.251870
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:35:24.667819
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:35:27.187800
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:35:29.559820
# Unit test for method task_done of class Queue

# Generated at 2026-10-25 09:35:32.381202
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:35:34.791946
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:35:37.206387
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:35:39.622186
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:35:42.035572
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:35:44.448871
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:35:46.861166
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:35:49.273840
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:35:51.689040
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:35:54.102267
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:35:56.515934
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:35:58.929341
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:01.345390
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:03.760982
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:06.177668
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:08.590667
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:36:11.005001
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:36:13.418981
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:36:15.833415
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:18.248726
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:20.662817
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:23.078563
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:36:25.647970
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:36:28.061290
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:36:30.478694
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:36:32.893946
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:36:35.308685
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:36:37.723509
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:40.139340
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:42.585348
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:45.459457
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:47.872451
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:50.286601
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:36:52.704431
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:36:55.118946
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:36:57.533806
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:36:59.947289
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:37:02.362214
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:37:04.776464
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:37:07.220647
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:37:09.635594
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:37:12.048754
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-25 09:37:14.463160
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:37:16.877618
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:37:19.295324
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:37:21.708604
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:37:24.131377
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:37:26.540766
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-25 09:37:28.955257
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:37:31.370089
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:37:33.784053
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:37:36.203516
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:37:38.615886
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:37:41.031361
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:37:43.932098
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

# Generated at 2026-10-25 09:37:45.452438
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

# Generated at 2026-10-25 09:37:48.113783
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

# Generated at 2026-10-25 09:37:49.752684
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 09:37:51.236938
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 09:37:52.621003
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 09:37:54.159109
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 09:37:55.693119
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

# Generated at 2026-10-25 09:37:57.021670
# Unit test for method get of class Queue
def test_Queue_get():bash

# Generated at 2026-10-25 09:37:58.456347
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-25 09:37:59.805101
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

# Generated at 2026-10-25 09:38:02.218411
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:38:04.635171
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:38:07.049439
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:38:09.464067
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:38:11.880054
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:38:14.446199
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:38:16.860903
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:38:19.430318
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:38:21.848851
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:38:24.263369
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:38:26.684589
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:38:29.098771
# Unit test for method get of class Queue

# Generated at 2026-10-25 09:38:32.477720
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:38:34.892116
# Unit test for method put of class Queue

# Generated at 2026-10-25 09:38:37.400495
# Unit test for method put of class Queue