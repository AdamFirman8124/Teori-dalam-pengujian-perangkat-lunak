

# Generated at 2026-10-24 10:41:32.303326
# Unit test for method join of class Queue
def test_Queue_join():
    async def _run():
        q = Queue()

        # Fresh queue: no unfinished tasks, so module_0.join() resolves immediately.
        await q.join(timeout=0.1)

        # module_0.join() blocks while tasks are unfinished, wakes after task_done().
        await q.put(1)
        await q.put(2)

        done = []

        async def joiner():
            await q.join()
            done.append(True)

        IOLoop.current().spawn_callback(joiner)
        await gen.sleep(0.01)  # let joiner start waiting

        with pytest.raises(TimeoutError):
            await q.join(timeout=0.05)  # 2 unfinished tasks

        q.task_done()
        with pytest.raises(TimeoutError):
            await q.join(timeout=0.05)  # 1 unfinished task remains

        q.task_done()
        await gen.sleep(0.05)
        assert done == [True]  # joiner was released

        # task_done() more times than put() raises ValueError.
        with pytest.raises(ValueError):
            q.task_done()

        # datetime.timedelta is accepted as a timeout.
        await q.put(3)
        with pytest.raises(TimeoutError):
            await q.join(timeout=datetime.timedelta(seconds=0.05))
        q.task_done()
        await q.join()

    IOLoop.current().run_sync(_run)

# Generated at 2026-10-24 10:41:46.792068
# Unit test for method __aiter__ of class Queue
def test_Queue___aiter__():
    q = Queue()
    q.put_nowait("item")

    async def consume():
        async for item in q:
            q.task_done()
            return item

    assert ioloop.IOLoop.current().run_sync(consume) == "item"

# Generated at 2026-10-24 10:41:49.211769
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-24 10:41:51.634239
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-24 10:41:54.052612
# Unit test for constructor of class PriorityQueue

# Generated at 2026-10-24 10:41:56.472310
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-24 10:41:59.040917
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-24 10:42:01.626978
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-24 10:42:04.145585
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:42:12.904027
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import pytest
    from tornado.queues import Queue, QueueEmpty

    q = Queue()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    q.put_nowait(1)
    q.put_nowait(2)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # Exercise the putters-waiting branch.
    q = Queue(maxsize=1)
    q.put_nowait("first")
    putter = q.put("second")
    assert not putter.done()
    assert q.get_nowait() == "first"
    assert putter.done()
    assert putter.result() is None
    assert q.get_nowait() == "second"
    assert q.empty()

# Generated at 2026-10-24 10:42:15.899782
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:42:17.226232
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:42:18.637585
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:42:21.505609
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:42:22.873050
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:42:25.714912
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:42:29.091752
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:42:30.495500
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:42:55.917300
# Unit test for constructor of class Queue
def test_Queue():
    # 1. default: maxsize=0 -> unbounded
    q = Queue()
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty() is True
    assert q.full() is False
    assert q._unfinished_tasks == 0
    assert q._finished.is_set() is True
    assert isinstance(q._queue, collections.deque)
    assert len(q._queue) == 0
    assert len(q._getters) == 0
    assert len(q._putters) == 0

    # 2. explicit valid maxsize
    q2 = Queue(maxsize=2)
    assert q2.maxsize == 2
    assert q2.qsize() == 0
    assert q2.empty() is True
    assert q2.full() is False

    q3 = Queue(maxsize=1)
    assert q3.maxsize == 1

    # 3. maxsize=None -> TypeError
    with pytest.raises(TypeError, match="maxsize can't be None"):
        Queue(maxsize=None)

    # 4. negative maxsize -> ValueError
    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-1)

    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-100)

# Generated at 2026-10-24 10:42:58.338616
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:43:00.759257
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:43:03.183787
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:43:05.605456
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:08.024878
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:09.689800
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:43:12.795919
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:14.241174
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:43:17.107515
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:18.434087
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:43:19.767875
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:21.079893
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:43:22.410469
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:23.736358
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:43:25.197581
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty without blocking.
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 2. Returns items FIFO and updates qsize / empty.
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

    # 3. Drains to empty -> raises again.
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 4. get_nowait pairs put with task_done / join accounting.
    q2: Queue[str] = Queue()
    q2.put_nowait("a")
    assert q2.get_nowait() == "a"
    # One unfinished task remains until task_done().
    q2.task_done()

# Generated at 2026-10-24 10:43:27.961789
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:29.400098
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:43:30.829926
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty without blocking.
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 2. Returns items FIFO and updates qsize / empty.
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

    # 3. Drains to empty -> raises again.
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 4. get_nowait pairs put with task_done / join accounting.
    q2: Queue[str] = Queue()
    q2.put_nowait("a")
    assert q2.get_nowait() == "a"
    # One unfinished task remains until task_done().
    q2.task_done()

# Generated at 2026-10-24 10:43:33.582955
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:43:35.032811
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:43:37.792094
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:40.319740
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:42.741427
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:45.166334
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:47.585856
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:50.007677
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:52.430371
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:43:54.848734
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:43:57.280690
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:43:59.703109
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:44:02.121651
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:44:04.674254
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:44:07.095613
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:44:35.264902
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull

    # Basic: put_nowait stores items without blocking.

# Generated at 2026-10-24 10:44:36.713933
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:44:38.209323
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:44:39.642927
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:44:42.399292
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:44:43.842735
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:44:46.267072
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:44:48.689170
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:44:51.108063
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:44:53.532013
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:44:55.952086
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:44:58.370213
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:45:00.787200
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:45:03.204753
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:45:05.621572
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:45:08.039589
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:45:25.837662
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():from tornado.queues import Queue, QueueFull

    # Basic: put_nowait stores items without blocking.

# Generated at 2026-10-24 10:45:27.261480
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:45:28.897858
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:45:30.331582
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:45:31.662674
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:45:33.404640
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:45:36.271858
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:45:37.676384
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:45:39.013157
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:45:40.468165
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:45:42.043980
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty without blocking.
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 2. Returns items FIFO and updates qsize / empty.
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

    # 3. Drains to empty -> raises again.
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 4. get_nowait pairs put with task_done / join accounting.
    q2: Queue[str] = Queue()
    q2.put_nowait("a")
    assert q2.get_nowait() == "a"
    # One unfinished task remains until task_done().
    q2.task_done()

# Generated at 2026-10-24 10:45:44.973830
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:45:46.297469
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:45:48.818652
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:45:51.354196
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:45:53.954676
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:45:56.374295
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:45:58.792073
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:01.211595
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:03.633380
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:06.052586
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:08.472426
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:10.889545
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:13.305403
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:28.391483
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():queue = Queue()

# Generated at 2026-10-24 10:46:31.144652
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:46:33.938271
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:46:35.458969
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:46:38.225608
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:40.735089
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:43.154428
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:45.571301
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:46:48.242068
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:46:50.660033
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:46:53.078954
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:46:55.497143
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:46:57.911706
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:00.330020
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:02.749774
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:05.167815
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:07.583859
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:47:09.999310
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:47:12.416919
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:47:14.831190
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:17.250639
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:19.668212
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:22.085645
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:47:24.501844
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:47:26.920007
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:47:29.340563
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:31.761817
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:34.182469
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:36.600877
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:39.019572
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:41.441700
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:43.862263
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:46.490555
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-24 10:47:47.957525
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:47:51.049741
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:47:52.432988
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:47:55.227697
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:56.557119
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:47:57.952383
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty without blocking.
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 2. Returns items FIFO and updates qsize / empty.
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

    # 3. Drains to empty -> raises again.
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 4. get_nowait pairs put with task_done / join accounting.
    q2: Queue[str] = Queue()
    q2.put_nowait("a")
    assert q2.get_nowait() == "a"
    # One unfinished task remains until task_done().
    q2.task_done()

# Generated at 2026-10-24 10:47:59.529440
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty without blocking.
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 2. Returns items FIFO and updates qsize / empty.
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

    # 3. Drains to empty -> raises again.
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 4. get_nowait pairs put with task_done / join accounting.
    q2: Queue[str] = Queue()
    q2.put_nowait("a")
    assert q2.get_nowait() == "a"
    # One unfinished task remains until task_done().
    q2.task_done()

# Generated at 2026-10-24 10:48:00.970172
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:48:02.498278
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:48:03.932446
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty without blocking.
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 2. Returns items FIFO and updates qsize / empty.
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

    # 3. Drains to empty -> raises again.
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 4. get_nowait pairs put with task_done / join accounting.
    q2: Queue[str] = Queue()
    q2.put_nowait("a")
    assert q2.get_nowait() == "a"
    # One unfinished task remains until task_done().
    q2.task_done()

# Generated at 2026-10-24 10:48:06.901715
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:48:09.719192
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:48:12.533879
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:14.188626
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:48:17.349170
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:48:19.989804
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:22.407651
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:24.931555
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:27.345508
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:29.766902
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:32.337693
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:36.216596
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:38.636502
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:41.058327
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:48:43.480333
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:48:45.898436
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:48:48.310586
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:48:50.728110
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:48:53.150611
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:48:55.561852
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:48:57.980928
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:49:00.396251
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:49:02.815102
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:49:05.231687
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:49:07.648430
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:49:10.066383
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:49:12.483243
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:49:14.899963
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:49:17.317546
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:49:19.734398
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:49:22.151186
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:49:24.568681
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:49:26.987785
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:49:29.403552
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:49:31.830660
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:49:34.249873
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:49:36.668170
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:49:39.085264
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:49:41.502613
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:49:43.918249
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:49:46.334777
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:49:51.689494
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:49:54.108293
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:49:56.529922
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:49:58.946728
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:50:01.368207
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:50:03.783603
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:50:06.203176
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:50:08.624530
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:50:11.040457
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:50:13.460265
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:50:15.878358
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:50:18.294138
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:50:20.707941
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:50:23.123907
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:50:25.557619
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:50:27.974847
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:50:30.393645
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:50:32.810779
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:50:35.240912
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:50:37.655950
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:50:40.074889
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:50:42.496603
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:50:44.912697
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:50:47.330084
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:50:49.747574
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:50:52.163132
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:50:53.579214
# Unit test for method get of class Queue
def test_Queue_get():from tornado.ioloop import IOLoop

# Generated at 2026-10-24 10:50:56.480928
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:51:04.977677
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # 1. Empty queue raises QueueEmpty without blocking.
    q: Queue[int] = Queue()
    assert q.qsize() == 0
    assert q.empty()
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 2. Returns items FIFO and updates qsize / empty.
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

    # 3. Drains to empty -> raises again.
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # 4. get_nowait pairs put with task_done / join accounting.
    q2: Queue[str] = Queue()
    q2.put_nowait("a")
    assert q2.get_nowait() == "a"
    # One unfinished task remains until task_done().
    q2.task_done()

# Generated at 2026-10-24 10:51:07.849330
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:51:09.366988
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:51:10.799967
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:51:13.998238
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:51:15.339412
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:51:16.760403
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:51:18.300470
# Unit test for method get of class Queue
def test_Queue_get():
    import datetime
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    async def main():
        # 1. Immediate result when item already available
        q = Queue()
        q.put_nowait(42)
        fut = q.get()
        assert await fut == 42
        assert q.empty()

        # 2. FIFO order for immediate gets
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        assert await q.get() == 1
        assert await q.get() == 2
        assert await q.get() == 3

        # 3. Blocks when empty, resolves on put_nowait
        q = Queue()
        fut = q.get()
        assert not fut.done()  #

# Generated at 2026-10-24 10:51:21.059040
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:51:23.484761
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:51:25.994609
# Unit test for method put of class Queue