

# Generated at 2026-10-24 10:37:48.301760
# Unit test for constructor of class QueueFull
def test_QueueFull():
    # is an Exception subclass
    assert issubclass(QueueFull, Exception)

    # constructor with no args
    e = QueueFull()
    assert isinstance(e, QueueFull)
    assert isinstance(e, Exception)
    assert e.args == ()

    # constructor preserves message
    e2 = QueueFull("queue full")
    assert isinstance(e2, QueueFull)
    assert e2.args == ("queue full",)
    assert str(e2) == "queue full"

    # can be raised and caught
    try:
        raise QueueFull("full")
    except QueueFull as caught:
        assert str(caught) == "full"
    else:
        assert False, "QueueFull was not raised"

    # can be caught as generic Exception
    try:
        raise QueueFull()
    except Exception as caught:
        assert isinstance(caught, QueueFull)
    else:
        assert False, "QueueFull was not caught as Exception"

# Generated at 2026-10-24 10:37:50.721430
# Unit test for constructor of class QueueFull

# Generated at 2026-10-24 10:37:53.139559
# Unit test for constructor of class QueueFull

# Generated at 2026-10-24 10:37:55.557921
# Unit test for constructor of class QueueFull

# Generated at 2026-10-24 10:37:57.979152
# Unit test for constructor of class QueueEmpty

# Generated at 2026-10-24 10:38:13.605953
# Unit test for constructor of class QueueEmpty
def test_QueueEmpty():error = QueueEmpty()

# Generated at 2026-10-24 10:38:23.121111
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:38:48.463499
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:38:50.977064
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-24 10:38:53.396234
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-24 10:38:55.816268
# Unit test for method __repr__ of class Queue

# Generated at 2026-10-24 10:38:58.235460
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:39:00.655943
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:39:15.547026
# Unit test for method get of class Queue
def test_Queue_get():from tornado.ioloop import IOLoop

# Generated at 2026-10-24 10:39:33.079549
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

# Generated at 2026-10-24 10:39:34.594545
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

# Generated at 2026-10-24 10:39:36.129384
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

# Generated at 2026-10-24 10:39:54.768241
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

# Generated at 2026-10-24 10:39:57.190148
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:39:59.611070
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:40:02.030741
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:40:04.452966
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:40:22.711940
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:40:24.020193
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:40:30.644556
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:41:02.261662
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:41:04.684314
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:41:11.566613
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():q = Queue(maxsize=2)

# Generated at 2026-10-24 10:41:12.998728
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:41:14.434496
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:41:15.961736
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

# Generated at 2026-10-24 10:41:17.402083
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

# Generated at 2026-10-24 10:41:51.717800
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:41:54.372044
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:41:56.789804
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:41:59.208570
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:42:01.632232
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:42:04.168511
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:42:26.626806
# Unit test for method get of class Queue
def test_Queue_get():from tornado import gen

# Generated at 2026-10-24 10:42:30.436330
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:42:33.159963
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:42:35.943282
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:42:37.265651
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:42:40.780528
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:42:43.830328
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:42:45.373570
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

# Generated at 2026-10-24 10:42:48.236417
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:42:50.666522
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:42:53.085158
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:42:55.643265
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:42:58.179086
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:00.605871
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:03.033050
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:43:05.453119
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:43:07.872420
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:43:10.646223
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:12.126466
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:43:13.481203
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:14.808689
# Unit test for method task_done of class Queue
def test_Queue_task_done():q = Queue()

# Generated at 2026-10-24 10:43:17.600784
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:43:20.383315
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:21.704474
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:43:24.479696
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:25.846415
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:43:27.347837
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

# Generated at 2026-10-24 10:43:30.418743
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:31.754914
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:43:34.518055
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:43:35.951594
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:43:37.383429
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:39.809192
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:42.233942
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:43:44.815374
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:43:47.232832
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:43:49.657299
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:43:52.077098
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:43:54.498340
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:43:56.936831
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:43:59.357196
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:44:01.779199
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:44:04.199540
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:44:06.621803
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:44:09.206591
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:44:10.563882
# Unit test for method get of class Queue
def test_Queue_get():from tornado.ioloop import IOLoop

# Generated at 2026-10-24 10:44:12.098330
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

# Generated at 2026-10-24 10:44:13.490168
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

# Generated at 2026-10-24 10:44:16.626967
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:44:18.009090
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

# Generated at 2026-10-24 10:44:19.470135
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

# Generated at 2026-10-24 10:44:20.850297
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

# Generated at 2026-10-24 10:44:24.076836
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:25.424824
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:44:28.275229
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:29.710856
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:44:32.475039
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:33.793924
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:44:36.569323
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:37.891006
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:44:39.340204
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

# Generated at 2026-10-24 10:44:42.103985
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:43.516111
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:44:45.950196
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:48.484908
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:50.907397
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:53.330417
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:55.750715
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:44:58.302414
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:45:00.720467
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:45:03.136635
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:45:05.555105
# Unit test for method task_done of class Queue

# Generated at 2026-10-24 10:45:07.972379
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:45:36.990809
# Unit test for method put of class Queue
def test_Queue_put():from tornado.ioloop import IOLoop

# Generated at 2026-10-24 10:45:39.852715
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:45:41.288630
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:45:44.156666
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:45:45.481829
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:45:48.231697
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:45:50.650287
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:45:53.066840
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:45:55.486003
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:45:57.905515
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:46:00.324508
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:46:02.745136
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:46:05.164670
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:46:07.582678
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:46:10.004135
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:46:12.418966
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:46:14.837846
# Unit test for method get_nowait of class Queue

# Generated at 2026-10-24 10:46:16.618951
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

# Generated at 2026-10-24 10:46:19.390576
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:46:20.731299
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:46:23.682003
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:46:25.117119
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:46:27.982674
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:46:29.312271
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:46:30.747757
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

# Generated at 2026-10-24 10:46:33.622190
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():import asyncio

# Generated at 2026-10-24 10:46:36.379151
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:46:37.712905
# Unit test for method put of class Queue
def test_Queue_put():import datetime


# Generated at 2026-10-24 10:46:40.132652
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:42.550385
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:44.971527
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:47.389416
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:49.897666
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:52.313782
# Unit test for method put_nowait of class Queue

# Generated at 2026-10-24 10:46:54.733209
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:46:57.150166
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:46:59.568032
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:01.984335
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:04.401487
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:06.957679
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:09.375007
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:11.789753
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:14.205341
# Unit test for method put of class Queue

# Generated at 2026-10-24 10:47:16.637287
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:19.049684
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:21.467270
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:23.883991
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:26.344806
# Unit test for method get of class Queue

# Generated at 2026-10-24 10:47:28.763422
# Unit test for method get of class Queue