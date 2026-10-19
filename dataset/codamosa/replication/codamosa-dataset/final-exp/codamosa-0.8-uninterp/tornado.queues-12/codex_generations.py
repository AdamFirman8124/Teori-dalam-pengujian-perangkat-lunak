

# Generated at 2022-06-14 12:46:09.229670
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=10)
    assert q.empty() == True
    q.put_nowait(5)
    assert q.empty() == False
    assert q.qsize() == 1
    assert q.full() == False
    print('test_Queue_put_nowait() pass')


# Generated at 2022-06-14 12:46:18.469664
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Generated at 2022-06-14 12:46:30.316279
# Unit test for method put of class Queue
def test_Queue_put():
    import tornado.gen
    import tornado.ioloop
    import tornado.testing
    import asyncio

    async def put(q):
        await q.put(1)
        await q.put(1)
        await q.put(1)
        await q.put(1)
        await q.put(1)

    async def get(q):
        while True:
            print(await q.get())

    async def test():
        q = Queue(maxsize=2)
        asyncio.create_task(put(q))
        asyncio.create_task(get(q))
        await tornado.gen.sleep(1)

    if __name__ == "__main__":
        tornado.testing.run_sync(test, timeout=1)
    

# Generated at 2022-06-14 12:46:39.683323
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Generated at 2022-06-14 12:46:52.145492
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    assert(q.empty() == True)
    assert(q.qsize() == 0)
    assert(q.full() == False)
    q.__put_internal(1)
    assert(q.empty() == False)
    assert(q.qsize() == 1)
    assert(q.full() == False)
    q.__put_internal(2)
    assert(q.empty() == False)
    assert(q.qsize() == 2)
    assert(q.full() == True)
    try:
        q.get_nowait()
    except(QueueEmpty):
        assert(True)
    except():
        assert(False)
    else:
        assert(False)
    assert(q.empty() == False)

# Generated at 2022-06-14 12:47:04.309761
# Unit test for method get of class Queue

# Generated at 2022-06-14 12:47:05.827966
# Unit test for method put of class Queue
def test_Queue_put():
    test_Queue = Queue()
    assert test_Queue.put(2) != None
    assert test_Queue.put(2,timeout=1) != None


# Generated at 2022-06-14 12:47:12.689086
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.gen import sleep

    q = Queue(maxsize=2)

    async def consumer():
        while not q.empty():
            print('Doing work on %s' % await q.get())
            await sleep(0.01)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    IOLoop.current().run_sync(main)



# Generated at 2022-06-14 12:47:25.225473
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.gen import TimeoutError

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            except TimeoutError:
                continue
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       #

# Generated at 2022-06-14 12:47:28.742066
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    q.put(1)
    assert q.qsize() == 1
    q.put(2)
    assert q.qsize() == 2
    q.put(3)
    assert q.qsize() == 3


# Generated at 2022-06-14 12:47:45.302246
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=3)
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    #trying to put when full
    try:
        q.put_nowait(4)
    except QueueFull as e:
        print(e)
        assert True



# Generated at 2022-06-14 12:47:57.329240
# Unit test for method get of class Queue
def test_Queue_get():

    class _QueueIterator(Generic[_T]):
        def __init__(self, q: "Queue[_T]") -> None:
            self.q = q

        def __anext__(self) -> Awaitable[_T]:
            return self.q.get()

    q = Queue(maxsize=2)
    await q.get()
    q.get_nowait()
    q.task_done()
    q.put(None)
    q.put_nowait(None)
    q.join()
    q.join()

    q.get(None)
    q.get_nowait()
    q.task_done()
    q.put(None)
    q.put_nowait(None)
    q.join()
    q.join()

    q.get(1.0)
   

# Generated at 2022-06-14 12:48:04.069753
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop
    queue = Queue()
    queue.put_nowait(1)
    #@asyncio.coroutine
    async def test_get():
        print(await queue.get())

    IOLoop.current().run_sync(test_get)
# test_Queue_get()



# Generated at 2022-06-14 12:48:12.946804
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Setup
    global LOG # type: str
    LOG = ''

    # Test
    q = Queue()  # type: Queue[int]
    q._put(1)
    q._put(2)
    q._put(3)
    q.get_nowait()
    q.task_done()
    q.get_nowait()
    q.task_done()
    q.get_nowait()
    q.task_done()
    assert q.qsize() == 3
    assert q.empty() == False
    assert q.full() == False

    # Verify
    assert LOG == ''


# Generated at 2022-06-14 12:48:13.948103
# Unit test for method get of class Queue
def test_Queue_get():

    # Implement unit test here
    pass



# Generated at 2022-06-14 12:48:20.613480
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop
    q = Queue(maxsize = 2)
    item = 0
    timeout = None
    future = Future()
    try:
        q.put_nowait(item)
    except QueueFull:
        q._putters.append((item, future))
        _set_timeout(future, timeout)
    else:
        future.set_result(None)
    return future


# Generated at 2022-06-14 12:48:27.065561
# Unit test for method put of class Queue
def test_Queue_put():
    io_loop = ioloop.IOLoop.current()
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        io_loop.spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    q = Queue(maxsize=2)
    io_loop.run_sync(main)


# Generated at 2022-06-14 12:48:33.487128
# Unit test for method get of class Queue
def test_Queue_get():
    # Input
    getters = collections.deque([])
    q = Queue()
    getters.append(Future())
    In = (q, getters)
    # Output
    res = q.get()
    Out = (getters, res)
    # Comparison
    assert Out == (In[1], Out[1])

# Generated at 2022-06-14 12:48:44.374601
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Generated at 2022-06-14 12:48:49.378945
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put(item = 666)
    assert q.qsize() == 1
    assert q.maxsize == 2
    assert q.full() == False
    q.put(item = 666)
    assert q.full() == True

    try:
        q.put(item = 666)
    except QueueFull:
        assert True
    future = q.put(item = 666)
    assert True



# Generated at 2022-06-14 12:49:11.138694
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    @gen.coroutine
    def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                yield gen.sleep(0.01)
            finally:
                q.task_done()
    @gen.coroutine
    def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
    @gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        yield producer()     # Wait for producer to put all tasks.
        yield q.join()       # Wait for

# Generated at 2022-06-14 12:49:23.402420
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop

    # Test case 1: put in an item and assert that it is in the queue
    q = Queue()
    q.put(3)
    assert q.qsize() == 1
    assert q.putters == []
    assert q.getters == []
    assert q.unfinished_tasks == 1
    assert q._queue == deque([3])

    # Test case 2: put in multiple items and assert that they are in the queue
    q.put(5)
    assert q.qsize() == 2
    assert q.putters == []
    assert q.getters == []
    assert q.unfinished_tasks == 2
    assert q._queue == deque([3,5])
    q.put(7)
    assert q

# Generated at 2022-06-14 12:49:28.636833
# Unit test for method put of class Queue
def test_Queue_put():
    a = Queue(maxsize=5)
    a.put(1, timeout=10)
    assert(a.__put_internal(2) == None)
    assert(a.qsize() == 2)
    return True

# Generated at 2022-06-14 12:49:32.374891
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.__put_internal(1)
    assert q.qsize() == 1
    assert q._get() == 1

# Generated at 2022-06-14 12:49:39.564212
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    #Test case 1, 2
    q._queue = collections.deque(["a","b"])
    q._unfinished_tasks = 2
    print(q.get_nowait())
    assert len(q._queue) == 1
    q._queue = collections.deque([])
    #Test case 3
    try:
        q.get_nowait()
    except QueueEmpty:
        print("Queue is empty")
        assert True
    else:
        assert False

# Generated at 2022-06-14 12:49:42.176236
# Unit test for method get of class Queue
def test_Queue_get():
    queue = Queue()
    future = Future()  # type: Future[_T]
    future.set_result(queue.get_nowait())
    return future


# Generated at 2022-06-14 12:49:48.289700
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=1)
    try:
        for item in range(5):
            q.put_nowait(item)
            print("Put {}".format(item))
    except QueueFull as e:
        print("QueueFull")
    except QueueEmpty as e:
        print("QueueEmpty")

# Generated at 2022-06-14 12:49:56.773802
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    ioloop.IOLoop.current().run_sync(main)

    #Test output

# Generated at 2022-06-14 12:50:00.769496
# Unit test for method put of class Queue
def test_Queue_put():
    # Set up the test Queue object
    q = Queue(maxsize=2)
    # Call function to be tested
    future = q.put(1, timeout=None)
    # Assert that value returned is as expected
    assert future.result() is None


# Generated at 2022-06-14 12:50:03.184704
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    q.put(1)
    assert q.qsize() == 1, q.qsize()


# Generated at 2022-06-14 12:50:20.092336
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize = 2)
    # We want to test the block case
    q.put_nowait(0)
    q.put_nowait(1)
    # Expect queue to be full so put_nowait raises error
    try:
        q.put_nowait(2)
        assert False, "The queue should have raised the error QueueFull but not"
    except QueueFull:
        pass


# Generated at 2022-06-14 12:50:23.326555
# Unit test for method put of class Queue
def test_Queue_put():
    # Setup code
    q = Queue()

    # Test code
    future = Future()
    result = q.put(item=future)
    assert result is not None


# Generated at 2022-06-14 12:50:25.784687
# Unit test for method get of class Queue
def test_Queue_get():
    # Test get() method of class Queue
    q = Queue()
    assert q.qsize() == 0


# Generated at 2022-06-14 12:50:35.890677
# Unit test for method put of class Queue
def test_Queue_put():
    import pytest

    q = Queue()

    @gen.coroutine
    def run():
        q.put("test")
        raise gen.Return(q.qsize())

    io_loop = ioloop.IOLoop.current()
    task = io_loop.run_sync(run)
    assert task == 1

    # Test QueueFull Exception, when queue becomes full
    with pytest.raises(QueueFull):
        q.put("full")

    # Test timeout
    with pytest.raises(gen.TimeoutError):
        q.put("timeout", timeout=0.01)


# Generated at 2022-06-14 12:50:36.992883
# Unit test for method put of class Queue
def test_Queue_put():
    Queue()



# Generated at 2022-06-14 12:50:44.465667
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    # Queue is empty, get_nowait raises QueueEmpty
    try:
        res = q.get_nowait()
    except QueueEmpty as e:
        assert isinstance(e, QueueEmpty)
    # Queue is not empty, get_nowait returns the first element
    q.getters.append(1)
    q.getters.append(2)
    q.getters.append(3)
    res = q.get_nowait()
    assert res == 1


# Generated at 2022-06-14 12:50:55.553125
# Unit test for method get of class Queue
def test_Queue_get():
    import time
    import random
    import threading
    from queue import Queue
    from multiprocessing import Process
    from multiprocessing import Queue as mQueue

    from queue import PriorityQueue

    mp_queue = mQueue()
    mp_queue.put(1)
    mp_queue.put(2)
    x = mp_queue.get()
    y = mp_queue.get()
    print(x, y)

    thread_queue = Queue()
    thread_queue.put(1)
    thread_queue.put(2)
    x = thread_queue.get()
    y = thread_queue.get()
    print(x, y)

    priorityQueue = PriorityQueue()
    priorityQueue.put((1, 1))
    priorityQueue.put((2, 2))

# Generated at 2022-06-14 12:50:58.452906
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.put(2)
    q.put(3)
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3



# Generated at 2022-06-14 12:51:01.294313
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    @gen.coroutine
    def test_method():
        future = Future()
        future.set_result("1")
        assert future.result() == "1"

    @gen.coroutine
    def test():
        ret = yield test_method()
        assert ret == "1"
    test()


# Generated at 2022-06-14 12:51:10.062047
# Unit test for method put of class Queue
def test_Queue_put():
    # Test Case 1
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
    async def main():
        IOLoop.current().spawn_callback(consumer)
        await producer()
        await q.join()
        print('Done')
    IOLoop.current().run_sync(main)
    assert True



# Generated at 2022-06-14 12:51:28.413365
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert len(q._queue) == 2

    async def put_many():
        await gen.sleep(10)
        await q.put(3)
        await gen.sleep(10)
        await q.put(4)

    IOLoop.current().run_sync(put_many)
    assert len(q._queue) == 2

# Generated at 2022-06-14 12:51:36.806931
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import tornado
    import tornado.testing
    import unittest

    class QueueNowaitTest(unittest.TestCase):
        def setUp(self):
            self.q = tornado.queues.Queue(maxsize=2)

        def test_get_nowait(self):
            with self.assertRaises(tornado.queues.QueueEmpty):
                self.q.get_nowait()

        def test_get_nowait_nonempty(self):
            self.q.put_nowait('foo')
            self.assertEqual('foo', self.q.get_nowait())

    if __name__ == '__main__':
        tornado.testing.main()

# Generated at 2022-06-14 12:51:47.457090
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop

    q = Queue()

    async def putter():
        for i in range(10):
            q.put_nowait(i)

    async def getter():
        for i in range(10):
            item = q.get_nowait()
            print("got %s" % item)

    IOLoop.current().spawn_callback(putter)
    IOLoop.current().spawn_callback(getter)

    IOLoop.current().start()

    print("Finish!!!")


# Generated at 2022-06-14 12:51:57.769800
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    # Normal case
    q = Queue(maxsize=2)
    IOLoop.current().run_sync(lambda: q.put(1))
    IOLoop.current().run_sync(lambda: q.put(2))
    assert IOLoop.current().run_sync(lambda: q.get()) == 1
    assert IOLoop.current().run_sync(lambda: q.get()) == 2
    IOLoop.current().run_sync(lambda: q.put(3))
    assert IOLoop.current().run_sync(lambda: q.get_nowait()) == 3

    # Case with error
    q1 = Queue(maxsize=0)

# Generated at 2022-06-14 12:52:03.912837
# Unit test for method get of class Queue
def test_Queue_get():
    # Create a queue object
    q = Queue(maxsize=2)
    # Put an item into the queue.
    q.put_nowait(3)
    # Remove and return an item from the queue.
    get_item = q.get_nowait()
    if get_item == 3:
        return True
    else:
        return False


# Generated at 2022-06-14 12:52:11.515419
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Generated at 2022-06-14 12:52:20.943783
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Generated at 2022-06-14 12:52:26.396209
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)

    f = q.put(1)
    assert f.done()
    assert f.result() is None

    f = q.put(2)
    assert f.done()
    assert f.result() is None

    f = q.put(3)
    assert (not f.done())

    q.task_done()
    f = q.put(4)
    assert f.done()
    assert f.result() is None


# Generated at 2022-06-14 12:52:37.238020
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    async def consumer():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.

# Generated at 2022-06-14 12:52:40.356988
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.__put_internal(1)
    q.__put_internal(2)
    assert q.get_nowait() == 1

# Generated at 2022-06-14 12:52:52.602683
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    assert q.get() == None
    assert q.get_nowait() == None



# Generated at 2022-06-14 12:52:59.497066
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
        
    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    IOL

# Generated at 2022-06-14 12:53:09.199516
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    a = Queue(0)
    a.put_nowait(10)
    a.put_nowait(30)
    a.put_nowait(20)
    b = Queue(1)
    b.put_nowait(10)
    b.put_nowait(30)
    b.put_nowait(20)
    c = Queue(3)
    c.put_nowait(10)
    c.put_nowait(30)
    c.put_nowait(20)
    d = Queue(4)
    d.put_nowait(10)
    d.put_nowait(30)
    d.put_nowait(20)
    e = Queue(None)
    e.put_nowait(10)
    e.put_nowait(30)


# Generated at 2022-06-14 12:53:18.444521
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.testing import AsyncTestCase, gen_test

    class TestQueuePut(AsyncTestCase):
    
        @gen_test
        async def test_put(self):
            q = Queue(maxsize=2)
            self.assertEqual(q.qsize(), 0)
            self.assertFalse(q.full())
            await q.put(1)
            self.assertEqual(q.qsize(), 1)
            self.assertFalse(q.empty())
            self.assertFalse(q.full())
            await q.put(2)
            self.assertEqual(q.qsize(), 2)
            self.assertFalse(q.empty())

# Generated at 2022-06-14 12:53:28.321788
# Unit test for method put of class Queue
def test_Queue_put():
    # Test 1: Checking if queue is full
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer

# Generated at 2022-06-14 12:53:31.971122
# Unit test for method get of class Queue
def test_Queue_get():
    '''
    Test Queue.get()
    '''
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    IOLoop.current().spawn_callback(consumer)
    q.get(0)


# Generated at 2022-06-14 12:53:32.953862
# Unit test for method get of class Queue
def test_Queue_get():
    Queue()


# Generated at 2022-06-14 12:53:35.379087
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    print(q.get())


if __name__ == "__main__":
    test_Queue_get()

# Generated at 2022-06-14 12:53:45.937901
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.

        print('Done')

# Generated at 2022-06-14 12:53:54.982801
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    print("\n**********\nUnit test results for method get of class Queue:\n")
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Generated at 2022-06-14 12:54:27.139137
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    try:
        q.put_nowait(1)
    except QueueFull:
        pass
    else:
        assert False
    try:
        q.put_nowait(1)
    except QueueFull:
        pass
    else:
        assert False

# Generated at 2022-06-14 12:54:33.829008
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
	import collections, types, random

	if hasattr(Queue, "_init"):
		Queue._init = types.MethodType(Queue._init.__func__, Queue)
	if hasattr(Queue, "_put"):
		Queue._put = types.MethodType(Queue._put.__func__, Queue)
	if hasattr(Queue, "_get"):
		Queue._get = types.MethodType(Queue._get.__func__, Queue)
	if hasattr(Queue, "_consume_expired"):
		Queue._consume_expired = types.MethodType(Queue._consume_expired.__func__, Queue)
	

	q = Queue(0)


# Generated at 2022-06-14 12:54:44.635276
# Unit test for method get of class Queue
def test_Queue_get():
    # This unit test function tests the method get of class Queue
    # method get(self, timeout=None) -> Awaitable[_T]:
    # Return an item if one is immediately available, else raise
    #     `QueueEmpty`.

    class QueueEmpty(Exception):
        """Raised by `.Queue.get_nowait` when the queue has no items."""

        pass

    class QueueFull(Exception):
        """Raised by `.Queue.put_nowait` when a queue is at its maximum size."""

        pass
    def _set_timeout(
        future: Future, timeout: Union[None, float, datetime.timedelta]
    ) -> None:
        if timeout:

            def on_timeout() -> None:
                if not future.done():
                    future.set_exception(gen.TimeoutError())

# Generated at 2022-06-14 12:54:50.892194
# Unit test for method get of class Queue
def test_Queue_get():
    #from tornado import gen
    #from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    import time

    q = Queue(maxsize=2)

    async def consumer():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                time.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        #IOLoop.current().spawn_callback(consumer)
        consumer()
        await producer()     # Wait for producer to put all tasks.
        await q.join()

# Generated at 2022-06-14 12:54:53.202641
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=100)
    q.put(0)
    q.put(1)
    return q

# Generated at 2022-06-14 12:54:55.950790
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado.queues import Queue
    q = Queue(0)
    print(q.put(0))


test_Queue_put_nowait()

# Generated at 2022-06-14 12:54:57.419218
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    result = q.get_nowait()

# Generated at 2022-06-14 12:55:00.787145
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        q.put_nowait(3)
        assert False, "An exception should be raised."
    except:
        pass
    q.get_nowait()
    q.get_nowait()
    q.put_nowait(4)
    assert q.get_nowait() == 4


# Generated at 2022-06-14 12:55:10.997185
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Generated at 2022-06-14 12:55:22.275255
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    IOLoop.current().run_sync(main)
