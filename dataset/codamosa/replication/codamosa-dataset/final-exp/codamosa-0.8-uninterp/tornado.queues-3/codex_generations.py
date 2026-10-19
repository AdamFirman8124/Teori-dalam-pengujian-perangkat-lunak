

# Generated at 2022-06-14 12:46:32.648432
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    q.put_nowait(4)
    assert q._queue == collections.deque([1, 2, 3, 4])


# Generated at 2022-06-14 12:46:41.180111
# Unit test for method get of class Queue
def test_Queue_get():
    import asyncio
    import tornado.ioloop
    import tornado.queues
    import types
    import typing
    import pytest

    @typing.overload
    def get(self: tornado.queues.Queue[typing.Any], timeout: typing.Any=...) -> typing.Awaitable[typing.Any]:...
    @typing.overload
    def get(self: tornado.queues.PriorityQueue[typing.Any], timeout: typing.Any=...) -> typing.Awaitable[typing.Any]:...
    @typing.overload
    def get(self: tornado.queues.LifoQueue[typing.Any], timeout: typing.Any=...) -> typing.Awaitable[typing.Any]:...


# Generated at 2022-06-14 12:46:41.810205
# Unit test for method get of class Queue
def test_Queue_get():
    pass

# Generated at 2022-06-14 12:46:49.390620
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    try:
        q.get_nowait()
    except Exception as e:
        assert isinstance(e, QueueEmpty)
    q.put_nowait(3)
    assert q.get_nowait() == 3


# Generated at 2022-06-14 12:46:52.993574
# Unit test for method put of class Queue
def test_Queue_put():
    future = Future()

    if future:
        pass

Queue.put.__annotations__['return']._name = "Future[None]"
Queue.get.__annotations__['return']._name = "Awaitable[_T]"



# Generated at 2022-06-14 12:47:05.223980
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Initializations of the parameters
    maxsize = 5
    timeout = datetime.timedelta(seconds = 1)
    item = "Something"

    # Create an instance of the Queue class
    queue = Queue(maxsize)

    # Call the put_nowait and pass the item, it should return None
    assert queue.put_nowait(item) == None
    assert queue.qsize() == 1

    # Call the put and pass timeout, the item, it should return None
    assert queue.put(item, timeout) == None
    assert queue.qsize() == 2

    # Call the put_nowait, it should raise QueueFull
    try:
        queue.put_nowait(item)
    except Exception as error:
        assert isinstance(error, QueueFull)

# Generated at 2022-06-14 12:47:12.827554
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    assert q.empty() == True
    assert q.full() == False
    q.put_nowait(1)
    assert q.qsize() == 1
    assert q.empty() == False
    assert q.full() == False
    q.put_nowait(2)
    assert q.qsize() == 2
    assert q.empty() == False
    assert q.full() == True
    try:
        assert q.get_nowait() == 1
    except QueueEmpty:
        assert False
    assert q.qsize() == 1
    assert q.empty() == False
    assert q.full() == False
    try:
        assert q.get_nowait() == 2
    except QueueEmpty:
        assert False



# Generated at 2022-06-14 12:47:25.320144
# Unit test for method get of class Queue
def test_Queue_get():
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

priorityqueue_

# Generated at 2022-06-14 12:47:27.809657
# Unit test for method put of class Queue
def test_Queue_put():
    print("test_Queue_put START")
    fut = Future()
    print(fut)
    assert isinstance(fut, Future)
    print("test_Queue_put PASS")
    return


# Generated at 2022-06-14 12:47:35.330141
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
#                await gen.sleep(0.01)
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

# Generated at 2022-06-14 12:47:58.186333
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado
    import tornado.ioloop
    import tornado.queues

    q = tornado.queues.Queue()

    def consumer():
        try:
            while True:
                item = yield q.get()
                try:
                    print('Doing work on %s' % item)
                    yield tornado.gen.sleep(0.01)
                finally:
                    q.task_done()

        except tornado.gen.Return:
            # print('exception caught')
            print('Done')

    def producer():
        for item in range(5):
            yield q.put(item)
            print('Put %s' % item)

    def main():
        # Start consumer without waiting (since it never finishes).
        print('entered main')
        tornado.ioloop.IOLoop.current().spawn_callback(consumer)
       

# Generated at 2022-06-14 12:48:10.219565
# Unit test for method get of class Queue
def test_Queue_get():
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

# Unit test

# Generated at 2022-06-14 12:48:13.772605
# Unit test for method get of class Queue
def test_Queue_get():
    # Test that Queue.get raises an exception with the correct type.
    q = Queue()
    try:
        q.get_nowait()
        raise AssertionError()
    except QueueEmpty:
        pass



# Generated at 2022-06-14 12:48:23.749563
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
        await q.join()       # Wait for consumer to finish all

# Generated at 2022-06-14 12:48:33.805687
# Unit test for method put of class Queue
def test_Queue_put():
  # Input: no input
  # Expected output: QueueFull exception
  q = Queue(maxsize=2)
  try:
    q.put(1)
  except QueueFull as e:
    print("Caught exception: " + str(e))
  try:
    q.put(2)
  except QueueFull as e:
    print("Caught exception: " + str(e))
  try:
    q.put(3)
  except QueueFull as e:
    print("Caught exception: " + str(e))


# Generated at 2022-06-14 12:48:44.620421
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

# Generated at 2022-06-14 12:48:49.014075
# Unit test for method get of class Queue
def test_Queue_get():
    # Test a simple get (queue not empty)
    q = Queue()
    q.put_nowait('item')
    res = q.get()
    assert isinstance(res.result(), str)

    # Test a simple get (queue empty)
    q = Queue()
    try:
        q.get()
    except QueueEmpty:
        res = True
    assert res


# Generated at 2022-06-14 12:49:00.942330
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    assert q.empty() == True
    # maxsize=0
    q.put_nowait(1)
    assert q.empty() == False
    q.get_nowait()
    assert q.empty() == True
    # maxsize=1
    q = Queue(maxsize=1)
    q.put_nowait(1)
    assert q.empty() == False
    q.get_nowait()
    assert q.empty() == True
    # maxsize=2
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.empty() == False
    q.get_nowait()
    assert q.empty() == False
    q.get_nowait()

# Generated at 2022-06-14 12:49:11.525681
# Unit test for method get of class Queue
def test_Queue_get():
    """
    Test Queue.get
    """
    from .base import freeze_time
    import tornado.ioloop
    import datetime
    import time
    from tornado.concurrent import Future
    from tornado import gen
    import io
    import os
    buffer = io.BytesIO()
    log_stdout = os.dup(1)
    os.dup2(buffer.fileno(), 1)
    async def f_test_Queue_get():
        q = Queue()
        f1 = q.get(timeout=datetime.timedelta(seconds=0.3))
        f2 = q.get(timeout=datetime.timedelta(seconds=1.0))
        time.sleep(0.9)
        q.put_nowait(1)
        assert(await f1 == 1)
       

# Generated at 2022-06-14 12:49:23.447486
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

# Generated at 2022-06-14 12:49:36.337226
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    empty_queue = Queue(maxsize=0)
    empty_queue.get_nowait()


# Generated at 2022-06-14 12:49:46.822341
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
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

# Generated at 2022-06-14 12:49:52.292323
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    new_item = "new_item"
    # Create instance of Queue
    q = Queue()
    # Call put_nowait method of Queue with item new_item
    q.put_nowait(new_item)
    # Check if new_item was added to the queue
    assert new_item in q._queue
    # Check if item was added at the end of the queue
    assert list(q._queue)[-1] == new_item


# Generated at 2022-06-14 12:50:01.245934
# Unit test for method put of class Queue
def test_Queue_put():
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

# Generated at 2022-06-14 12:50:04.034912
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    for i in range(5):
        try:
            q.put_nowait((i))
        except QueueFull:
            print('Put ', i, 'Failed')
            break
        else:
            print('Put ', i, 'Success')

# Generated at 2022-06-14 12:50:13.771498
# Unit test for method get of class Queue
def test_Queue_get():
    """
    test for method Queue.get
    """
    import time
    import threading
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    async def consumer1():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    async def consumer2():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

# Generated at 2022-06-14 12:50:15.504518
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=1)
    q.put(1)
    print(q.qsize())


# Generated at 2022-06-14 12:50:28.004577
# Unit test for method put of class Queue
def test_Queue_put():
    _maxsize = 100
    q = Queue(_maxsize)

    q._maxsize = None
    with pytest.raises(TypeError) as excinfo:
        q.put(1)
    assert "maxsize can't be None" in str(excinfo.value)

    q._maxsize = -1
    with pytest.raises(ValueError) as excinfo:
        q.put(1)
    assert "maxsize can't be negative" in str(excinfo.value)

    q._maxsize = _maxsize

    # if _getters:
    # assert self.empty(), "queue non-empty, why are getters waiting?"
    q._getters.append(q._getters)
    assert q.empty() is False, "queue non-empty, why are getters waiting?"
    q._getters

# Generated at 2022-06-14 12:50:38.451684
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=10) # Set the size of queue

    async def producer():
        for item in range(5):
            await q.put(item) # Add an item to the queue, will block if the queue is full
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    ioloop.IOLoop.current().run_sync(main)


# Generated at 2022-06-14 12:50:49.373174
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

# Generated at 2022-06-14 12:51:09.980877
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.testing import AsyncTestCase, get_async_test_timeout

    class MyTestCase(AsyncTestCase):
        def test_my_method(self):
            q = Queue(maxsize=2)
            q.put_nowait(1)
            q.put_nowait(2)
            self.assertEqual(q.get_nowait(), 1)
            self.assertEqual(q.get_nowait(), 2)

    IOLoop.clear_current()
    MyTestCase().test_my_method()
    IOLoop.clear_current()



# Generated at 2022-06-14 12:51:13.199182
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=3)
    res = q.put(1).result()
    assert type(res) == int


# Generated at 2022-06-14 12:51:25.264757
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
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

# Generated at 2022-06-14 12:51:35.463639
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                # time.sleep(0.01)
                # print('Doing work on %s' % item)
                pass
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            # print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.


# Generated at 2022-06-14 12:51:44.088432
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # function type: () -> None
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
        IOLoop.current().spawn_callback

# Generated at 2022-06-14 12:51:53.695518
# Unit test for method put of class Queue
def test_Queue_put():
    # Initializing the queue
    queue = Queue()

    # The first element to put into the queue
    item1 = 1
    # Putting the element into the queue
    queue.put_nowait(item1)

    # The second element to put into the queue
    item2 = 2
    # Putting the element into the queue
    queue.put_nowait(item2)

    # Checking if the queue is not empty
    if not queue.empty():
        # Printing the size of the queue
        print("Queue size is: " + str(queue.qsize()))

        # Getting the first element of the queue
        element1 = queue.get_nowait()
        # Printing the element
        print(element1)
        # Marking the task as done
        queue.task_done()

        # Getting the first element of the queue
        element

# Generated at 2022-06-14 12:51:57.413275
# Unit test for method put of class Queue
def test_Queue_put():
    # Keyword arguments
    q = queue.Queue(maxsize=2)
    result = q.put()
    assert result in [None, True, False]

    # No arguments
    q = queue.Queue()
    result = q.put()
    assert result in [None, True, False]


# Generated at 2022-06-14 12:52:03.716462
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    myQueue = Queue(maxsize=2)
    assert(myQueue.put_nowait(1) == None)
    assert(myQueue.put_nowait(2) == None)
    try:
        assert(myQueue.put_nowait(3) == None)
    except QueueFull:
        print("Queue is full")


# Generated at 2022-06-14 12:52:07.507634
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)

    assert q.empty() == True

    q.put_nowait(1)
    q.put_nowait(2)

    assert q.empty() == False
    assert q.full() == True


# Generated at 2022-06-14 12:52:19.787201
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

# Generated at 2022-06-14 12:52:52.750369
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado.ioloop
    from tornado.queues import Queue
    q = Queue()

    def putter(item=0):
        if item < 5:
            q.put(item)
            tornado.ioloop.IOLoop.instance().add_callback(lambda: putter(item+1))

    tornado.ioloop.IOLoop.instance().add_callback(lambda: putter())

    for i in range(5):
        (tornado.ioloop.IOLoop.instance().add_future(
            q.get(),
            lambda f: (tornado.ioloop.IOLoop.instance().stop()
                       if f.result() == 4
                       else None))).result()
        tornado.ioloop.IOLoop.instance().start()

# Example usage of class Queue

# Generated at 2022-06-14 12:52:56.945545
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    print(q.put(1, timeout=0.1))
    print(q.put(2, timeout=0.1))
    print(q.put(3, timeout=0.1))
    print(q.put(4, timeout=0.1))
    print(q)

if __name__ == "__main__":
    test_Queue_put()

# Generated at 2022-06-14 12:53:05.717916
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=10)
    q.put_nowait("red")
    q.put_nowait("blue")
    q.put_nowait("yellow")
    q.put_nowait("purple")
    q.put_nowait("green")
    q.put_nowait("orange")
    q.put_nowait("black")
    q.put_nowait("white")
    q.put_nowait("grey")
    q.put_nowait("brown")
    q.put_nowait("pink")

# Generated at 2022-06-14 12:53:16.731810
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():

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

# Generated at 2022-06-14 12:53:20.901564
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    for item in range(5):
        try:
            q.put_nowait(item)
            print('Put %s' % item)
        except QueueFull:
            print('Put %s Fail' % item)


# Generated at 2022-06-14 12:53:21.803014
# Unit test for method put of class Queue
def test_Queue_put():
    pass


# Generated at 2022-06-14 12:53:25.105309
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    f = q.get()
    assert f.is_future()
    try:
        assert q.get_nowait().is_future()
    except QueueEmpty:
        pass
    

# Generated at 2022-06-14 12:53:35.433651
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    future = Future()
    timeout = 1
    def on_timeout():
        if not future.done():
            future.set_exception(gen.TimeoutError())

    io_loop = ioloop.IOLoop.current()
    timeout_handle = io_loop.add_timeout(timeout, on_timeout)
    future.add_done_callback(lambda _: io_loop.remove_timeout(timeout_handle))
    try:
        future.set_result(q.get_nowait())
    except QueueEmpty:
        q._getters.append(future)
        _set_timeout(future, timeout)
    return future
########################################################################################################################

# Generated at 2022-06-14 12:53:38.639731
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3) # raises queue full exception


# Generated at 2022-06-14 12:53:44.429553
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import time
    import random
    q = Queue(maxsize=2)

    # consumer
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    # producer
    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()  # Wait for producer to put all tasks.
        await q.join()  # Wait for consumer to finish all tasks.
        print('Done')

    ioloop.I

# Generated at 2022-06-14 12:54:20.598439
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
	# Queue.get_nowait(self, timeout: Optional[Union[float, datetime.timedelta]] = None) -> Any
	from tornado import gen
	from tornado.ioloop import IOLoop
	from tornado.queues import Queue

	q = Queue()

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


# Generated at 2022-06-14 12:54:24.282188
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put(1)
    q.put(2)
    q.put(3)

# Generated at 2022-06-14 12:54:26.026552
# Unit test for method get of class Queue
def test_Queue_get():
    maxsize = 0

    q = Queue(maxsize)
    q.get_nowait()

# Generated at 2022-06-14 12:54:27.138376
# Unit test for method put of class Queue
def test_Queue_put():
    def f1():
        pass

# Generated at 2022-06-14 12:54:37.732001
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # putters = collections.deque([])  # type: Deque[Tuple[_T, Future[None]]]
    # qsize() -> int:

    # qsize() -> int:
    a = Queue(maxsize=0)
    # Empty queue
    b = Queue(maxsize=0)
    # Empty queue
    # Test with an empty queue
    assert a.qsize() == b.qsize()

    # Task done on an empty queue, should raise ValueError
    try:
        a.task_done()
    except:
        assert True
    else:
        assert False

    # Test with a nonempty queue
    c = Queue(maxsize=0)
    d = Queue(maxsize=0)
    c.put_nowait(5)
    d.put_nowait(5)

# Generated at 2022-06-14 12:54:47.331270
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

# Generated at 2022-06-14 12:54:52.628681
# Unit test for method put of class Queue
def test_Queue_put():
    def func(*args, **kwargs):
        pass
    q = Queue(maxsize=2)
    q._put = func
    q.put(1, timeout=None)


# Generated at 2022-06-14 12:55:01.293873
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Create Queue
    q = Queue(maxsize=2)
    q.put_nowait(0)
    q.put_nowait(1)
    
    # Check qsize
    assert q.qsize() == 2
    
    # Get an item from the queue without blocking
    item = q.get_nowait()
    assert item == 0
    
    # Check qsize
    assert q.qsize() == 1
    
    # Get an item from the queue without blocking
    item = q.get_nowait()
    assert item == 1
    
    # Check qsize
    assert q.qsize() == 0
    
    print("[+] Queue_get_nowait() - OK!")


# Generated at 2022-06-14 12:55:01.884921
# Unit test for method get of class Queue
def test_Queue_get():
        pass

# Generated at 2022-06-14 12:55:04.501808
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)


# Generated at 2022-06-14 12:55:57.112104
# Unit test for method get of class Queue
def test_Queue_get():
    return_value = Queue.get(1)
    assert return_value == None


# Generated at 2022-06-14 12:56:06.978514
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import time, random
    q = Queue(maxsize=5)
    assert q.qsize() == 0
    try:
        q.put_nowait(1)
    except QueueFull: pass
    assert q.qsize() == 1
    try:
        q.put_nowait(2)
    except QueueFull: pass
    assert q.qsize() == 2
    q.put_nowait(3)
    q.put_nowait(4)
    q.put_nowait(5)
    q.put_nowait(6) # ERROR here, function put_nowait of class Queue invokes function full() whose return value is False
    assert q.qsize() == 6
    q.put_nowait(7)
    assert q.qsize() == 7