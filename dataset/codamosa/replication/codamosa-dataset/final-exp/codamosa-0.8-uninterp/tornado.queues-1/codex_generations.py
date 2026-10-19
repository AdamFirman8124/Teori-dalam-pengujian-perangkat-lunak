

# Generated at 2022-06-14 12:46:17.157346
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

# Generated at 2022-06-14 12:46:28.699309
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import sys
    q = Queue(maxsize=2)
    assert q.maxsize == 2
    assert q.qsize() == 0
    assert q.empty() == True
    assert q.full() == False
    assert q.get_nowait() == None
    # Test case where queue is not full but no items are in queue
    q = Queue(maxsize = 2)
    assert q.get_nowait() == None
    # Test case where the queue is full
    q = Queue(maxsize = 2)
    q.__put_internal(1)
    q.__put_internal(2)
    assert q.full() == True
    # Test case where an item is immediately available
    q = Queue(maxsize = 2)
    q.__put_internal(1)
    q.__put_internal

# Generated at 2022-06-14 12:46:38.704237
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    # TODO:
    @gen.coroutine
    def consumer():
        while True:
            item = yield q.get()
            try:
                print('Doing work on %s' % item)
                yield gen.sleep(0.01)
            finally:
                q.task_done()
    # TODO:
    @gen.coroutine
    def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
    # TODO:
    @gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_

# Generated at 2022-06-14 12:46:49.580749
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    assert q.maxsize == 2
    assert q.qsize() == 0
    assert q.empty() == True
    assert q.full() == False
    q.put_nowait(1)
    assert q.qsize() == 1
    assert q.empty() == False
    assert q.full() == False
    q.put_nowait(11)
    assert q.qsize() == 2
    assert q.empty() == False
    assert q.full() == True
    try:
        q.put_nowait(111)
        assert False
    except QueueFull:
        pass



# Generated at 2022-06-14 12:46:57.750977
# Unit test for method get of class Queue
def test_Queue_get():
    data = [ 'a', 'b', 'c' ]

    def func(q):
        for i in data:
            q.put(i)
        q.join()


    # import threading
    from tornado.gen import sleep
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.testing import AsyncTestCase, get_unused_port

    class TestCase(AsyncTestCase):
        def test(self):
            q = Queue()
            t = threading.Thread(target=func, args=(q,))
            t.start()
            while True:
                try:
                    i = q.get(timeout=0.05)
                except Exception as e:
                    print(e)
                    raise
                if i is None:
                    break
                print(i)

# Generated at 2022-06-14 12:47:04.309127
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.full()
    try:
        q.put_nowait(3)
        assert False, "Fail: Should raise QueueFull"
    except QueueFull:
        pass
    
test_Queue_put_nowait()


# Generated at 2022-06-14 12:47:13.383034
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

# Generated at 2022-06-14 12:47:18.133400
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # TODO: Add more tests
    maxsize = 0
    q = Queue(maxsize=maxsize)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.qsize() == 2



# Generated at 2022-06-14 12:47:23.864133
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)

    try:
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        print("Queue is full")
    except QueueFull:
        print("Queue is full")
    finally:
        print(q)

# Generated at 2022-06-14 12:47:33.014703
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

# Generated at 2022-06-14 12:47:54.090247
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

# Generated at 2022-06-14 12:47:55.192259
# Unit test for method get of class Queue
def test_Queue_get():
    return


# Generated at 2022-06-14 12:47:56.176808
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)


# Generated at 2022-06-14 12:48:08.718691
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

# Generated at 2022-06-14 12:48:12.600605
# Unit test for method put of class Queue
def test_Queue_put():
    for isinstance in [Queue]:
        assert isinstance(Queue().put(), Future)
        assert isinstance(Queue().put(), Future)
        assert isinstance(Queue().put(), Future)
        assert isinstance(Queue().put(), Future)

    pass

# Generated at 2022-06-14 12:48:20.319232
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    import asyncio

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
        # await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Generated at 2022-06-14 12:48:22.650826
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    future = q.get()
    print(q.qsize()," ",q._getters)
    print(future)


# Generated at 2022-06-14 12:48:26.996577
# Unit test for method get of class Queue
def test_Queue_get():
	io_loop = ioloop.IOLoop.current()
	q = Queue(maxsize=1)
	q.put(1)
	res = q.get_nowait()
	assert res == 1


# Generated at 2022-06-14 12:48:40.038647
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    #Start consumer without waiting (since it never finishes).
    IOLoop.current().spawn_callback(consumer)
    # Wait for producer to put all tasks.
    #await producer()
    # Wait for consumer to finish all tasks.
    #await q.join()
    print('Done')

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

# Generated at 2022-06-14 12:48:48.023754
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(5)
    q.put_nowait(3)
    assert q._Queue__put_internal(5) == None
    try:
        q.put_nowait(7)
        assert False
    except QueueFull:
        pass
    assert q._Queue__put_internal(3) == None
    assert q.get_nowait() == 5
    assert q.get_nowait() == 3
    try:
        q.get_nowait()
        assert False
    except QueueEmpty:
        pass
    q.task_done()
    assert q.join() == None
    try:
        q.task_done()
        assert False
    except ValueError:
        pass

# Generated at 2022-06-14 12:49:07.926816
# Unit test for method get of class Queue
def test_Queue_get():
    import sys
    import pytest
    import time
    # ! Uncomment following lines for tester
    # from mock import patch
    # from tornado.queues import Queue

    # from tornado.gen import TimeoutError
    # from tornado.ioloop import IOLoop
    # from tornado.platform.asyncio import to_asyncio_future, to_tornado_future
    # from tornado.test.util import unittest

    # from concurrent.futures import Future as std_Future
    # from tornado.platform.asyncio import to_asyncio_future
    # from tornado.platform.asyncio import to_tornado_future, to_std_future

    # import asyncio

    # def function_get(self, timeout=None):

    #     if timeout is not None and not isinstance(timeout, datetime

# Generated at 2022-06-14 12:49:15.917610
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            print('Doing work on %s' % item)
            await gen.sleep(0.01)
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


# Generated at 2022-06-14 12:49:25.248789
# Unit test for method get of class Queue
def test_Queue_get():
    # Initialization of Queue object q
    q = Queue()
    # Check that the qsize method returns 0
    assert q.qsize() == 0
    # Check that putting an object in the Queue increases its size
    q.put('test')
    assert q.qsize() == 1
    # Check that the get_nowait method returns the correct object
    assert q.get_nowait() == 'test'
    # Check that the get_nowait method throws QueueEmpty if there is nothing in the queue
    raised = False
    try:
        q.get_nowait()
    except QueueEmpty:
        raised = True
    assert raised

# Generated at 2022-06-14 12:49:32.389209
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.queues import QueueEmpty
    from tornado.queues import QueueFull

    q = Queue(maxsize=2)
    q.put_nowait(0)
    q.put_nowait(1)
    try:
        q.put_nowait(2)
        assert False, "queue is full"
    except QueueFull:
        pass

    # Exhaust one item
    item = q.get_nowait()
    assert item == 0

    # Add a new item
    q.put_nowait(2)
    try:
        q.put_nowait(3)
        assert False, "queue is full"
    except QueueFull:
        assert q.qsize()

# Generated at 2022-06-14 12:49:33.696361
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    assert q.get_nowait() is None


# Generated at 2022-06-14 12:49:35.083625
# Unit test for method get of class Queue
def test_Queue_get():
    return None

# Generated at 2022-06-14 12:49:45.402693
# Unit test for method get of class Queue
def test_Queue_get():
  from tornado import gen
  from tornado.ioloop import IOLoop
  from tornado.queues import Queue
  object = Queue(maxsize=1)
  object.get()
  object.put()
  object.get_nowait()
  object.put_nowait()
  object.task_done()
  object.join()
  object.__aiter__()
  # test Queue.get
  async def consumer():
    return None
  # test Queue.put
  async def producer():
    # test Queue.join
    await object.join()
    # test Queue.join
  async def main():
    # test Queue.__aiter__
    async for item in object:
      pass
    await consumer()
    await producer()
    print('Done')

  IOLoop.current().run

# Generated at 2022-06-14 12:49:53.918075
# Unit test for method get of class Queue
def test_Queue_get():
    import time
    a = Queue(maxsize=0)
    for i in range (0, 10):
        a.put_nowait(i)
    print(a.qsize())
    b = a.get_nowait()
    print ('b')
    print(a.qsize())
    c = a.get_nowait()
    print ('c')
    print(a.qsize())
    t1 = time.time()
    print (t1)
    # start = time.time()
    d = a.get()
    print ('d')
    print(a.qsize())
    # print (d)
    # duration = time.time() - start
    # print (duration)
    t2 = time.time()
    print (t2)
    print (t2 - t1)
   

# Generated at 2022-06-14 12:50:04.998820
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



# Generated at 2022-06-14 12:50:08.106146
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Initialization
    q = Queue(maxsize=0)

    # Code to be tested
    # q.put_nowait(None)

    # Check results
    assert q.qsize() == 1

# Generated at 2022-06-14 12:50:28.220403
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



# Generated at 2022-06-14 12:50:31.997490
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=5)
    try:
        print(q.get_nowait())
    except QueueEmpty:
        print("Queue is empty!")



# Generated at 2022-06-14 12:50:43.434437
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q._queue = collections.deque(iterable=["a"])
    q._getters = collections.deque(iterable=[])
    q._putters = collections.deque(iterable=[])
    q._unfinished_tasks = 0
    q._finished = Event()
    q._finished.set()
    q.put_nowait("b")
    assert q._queue == collections.deque(iterable=["a","b"])
    assert q._getters == collections.deque(iterable=[])
    assert q._putters == collections.deque(iterable=[])
    assert q._unfinished_tasks == 1
    assert q._finished == Event()
    assert q._finished.is_set() == True


# Generated at 2022-06-14 12:50:48.261880
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    myQueue = Queue(10)
    for i in range(10):
        myQueue.put(i)
    for i in range(10):
        print(myQueue.get_nowait())
        

# Generated at 2022-06-14 12:50:53.306309
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=3)
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    try:
        q.get_nowait()
        assert False
    except QueueEmpty:
        pass



# Generated at 2022-06-14 12:50:55.487372
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    future = q.put(5)
    assert future.done()



# Generated at 2022-06-14 12:50:58.365838
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
	q = Queue()
	q.put(0)
	assert q.get_nowait() == 0
	try:
		q.get_nowait()
	except:
		return
	assert False


# Generated at 2022-06-14 12:51:02.849084
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    # Check the queue is empty
    assert q.empty()
    # Put an item into the queue
    q.put_nowait(1)
    assert q.qsize() == 1
    # Get an item from the queue
    assert q.get_nowait() == 1
    # Check the queue is empty again
    assert q.empty()



# Generated at 2022-06-14 12:51:06.831988
# Unit test for method put of class Queue
def test_Queue_put():
    # Create a Queue object
    q = Queue()
    # Put an item into the queue
    q.put(1)
    # Verify that the item was put into the queue
    if q.qsize() != 1:
        raise Exception("Method put for class Queue did not work as expected")


# Generated at 2022-06-14 12:51:14.805449
# Unit test for method get of class Queue
def test_Queue_get():
    print("*" * 20, "Unit test for method get of class Queue:")
    # Define a test class
    class TestClass:
        def __init__(self):
            pass

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
        await producer()     # Wait for producer to put all tasks

# Generated at 2022-06-14 12:51:29.046117
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    if __name__ == '__main__':
        print('test_Queue_get_nowait')
        q = Queue(maxsize=2)
        print('\t- q.qsize() = ', q.qsize())
        print('\t- q.put(2)')
        print('\t- q.put(3)')
        q.put(2)
        q.put(3)
        print('\t- q.qsize() = ', q.qsize())
        print("\t- assert q.qsize() == 2")
        assert q.qsize() == 2
        print("\t- assert q.get_nowait() == 2")
        assert q.get_nowait() == 2
        print("\t- assert q.get_nowait() == 3")
        assert q.get_

# Generated at 2022-06-14 12:51:31.976649
# Unit test for method put of class Queue
def test_Queue_put():
    # Create an instance of the class Queue
    q = Queue()
    
    # Calling method put of the class Queue
    q.put(1)
    
    
    
    


# Generated at 2022-06-14 12:51:42.634729
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import sys
    import unittest

    from tornado.concurrent import Future
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.util import PY34

    class QueueTest(unittest.TestCase):
        def setUp(self):
            self.io_loop = IOLoop()
            self.queue = Queue(maxsize=2)
            self.getter = self.queue.get()
            self.putter = Future()
            self.put_args = None
            self.put_kwargs = None
            self.consumer = None
            self.producer = None


# Generated at 2022-06-14 12:51:54.286372
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

# Generated at 2022-06-14 12:52:02.000572
# Unit test for method put of class Queue
def test_Queue_put():
    import time
    import random
    import sys
    import os
    import math
    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop
    import threading
    import logging

    # File: queue.py (Python 2.7)

    # For type annotations
    import typing
    if typing.TYPE_CHECKING:
        from typing import List, Callable, Any, Dict
    # Unit test for method join of class Queue

    # Unit test for method get of class Queue

    def test_Queue_get():
        import time
        import random
        import sys
        import os
        import math

# Generated at 2022-06-14 12:52:06.127439
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put_nowait((1, 2))
    q.put_nowait(3)
    assert q.get() == (1, 2)
    assert q.get() == 3
    assert q.empty()

# Generated at 2022-06-14 12:52:16.108148
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():

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

# Generated at 2022-06-14 12:52:20.208629
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=1)
    assert q.full() == False
    q.put(1)
    assert q.full() == True
    q.get()
    assert q.full() == False


# Generated at 2022-06-14 12:52:28.007685
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    assert q.empty()
    assert not q.full()
    q.put_nowait(1)
    assert not q.empty()
    q.put_nowait(2)
    q.put_nowait(3)
    assert not q.empty()
    assert q.full()
    try:
        q.put_nowait(4)
    except QueueFull:
        assert True
    else:
        assert False
    assert not q.empty()
    q.get_nowait()
    q.get_nowait()
    assert not q.full()
    assert not q.empty()
    q.get_nowait()
    assert q.empty()
    q.put_nowait(1)
    q.put_nowait(2)

# Generated at 2022-06-14 12:52:30.808531
# Unit test for method put of class Queue
def test_Queue_put():
    print("\nTest of Queue put method")
    import doctest
    doctest.testmod(Queues)
    
    


# Generated at 2022-06-14 12:52:56.143986
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    q.maxsize = 0
    q._unfinished_tasks = 0
    q._finished = Event()
    q._getters = deque()
    q._putters = deque()
    q._queue = deque()
    functions = {'get': q.get, 'put': q.put, 'qsize': q.qsize, 'full': q.full, 'put_nowait': q.put_nowait, 'empty': q.empty, 'get_nowait': q.get_nowait, 'task_done': q.task_done}
    q.put_nowait(5)
    assert q._queue.pop() == 5
    assert q._unfinished_tasks == 1
    return functions # the actual return statement is for the unit test


# Generated at 2022-06-14 12:53:00.714869
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.__put_internal(1)
    assert q.get_nowait() == 1
    assert q.qsize() == 0
    assert q.empty()

# Generated at 2022-06-14 12:53:09.828011
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
# call the put method of class Queue
    def put1():
        try:
            q.put(1)
        except QueueEmpty as e:
            raise Exception('Queue not empty, why are getters waiting?', e)
    def put2():
        try:
            q.put(2)
        except QueueEmpty as e:
            raise Exception('Queue not empty, why are getters waiting?', e)
    def put3():
        try:
            q.put(3)
        except QueueFull as e:
            print('There is no free slot is immediately available')

# Generated at 2022-06-14 12:53:18.137935
# Unit test for method get of class Queue
def test_Queue_get():
    import time
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=3)
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                time.sleep(0.01)
            finally:
                q.task_done()
    IOLoop.current().spawn_callback(consumer)
    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
    async def main():
        await producer()
        await q.join()
        print('Done')
    IOLoop.current().run_sync(main)


# Generated at 2022-06-14 12:53:18.769407
# Unit test for method get of class Queue
def test_Queue_get():
    pass

# Generated at 2022-06-14 12:53:28.554390
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    import asyncio
    import pytest

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await asyncio.sleep(0.01)
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


# Generated at 2022-06-14 12:53:34.655628
# Unit test for method get of class Queue
def test_Queue_get():
    """
    if timeout is None:
        return future_set_result_unless_cancelled(self._future, result)
    else:
        if self._done.wait(timeout):
            return future_set_result_unless_cancelled(self._future, result)
        else:
            future_set_result_unless_cancelled(self._future, None)
            raise gen.TimeoutError()
    """
    pass

# Generated at 2022-06-14 12:53:35.336305
# Unit test for method put of class Queue
def test_Queue_put():
    pass

# Generated at 2022-06-14 12:53:45.893330
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    """Unit test for method put_nowait of class Queue"""
    class _Test(unittest.TestCase):
        def setUp(self):
            pass
        def tearDown(self):
            pass
        def test_1(self):
            q = Queue(maxsize=2)
            self.assertEqual(q.qsize(),0)
            self.assertEqual(q.empty(),True)
            self.assertEqual(q.full(),False)
            q.put_nowait(1)
            self.assertEqual(q.qsize(),1)
            self.assertEqual(q.empty(),False)
            self.assertEqual(q.full(),False)
            q.put_nowait(2)
            self.assertEqual(q.qsize(),2)

# Generated at 2022-06-14 12:53:49.724343
# Unit test for method put of class Queue
def test_Queue_put():

	def test_timeout():
		pass

	def test_no_timeout():
		pass	

	def test_timeout_None():
		pass	

	def test_timeout_0():
		pass	

	def test_timeout_negative():
		pass	


# Generated at 2022-06-14 12:54:29.455185
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    print(q.get_nowait())


# Generated at 2022-06-14 12:54:35.274398
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=3)
    assert q.empty() == True
    assert q.full() == False
    q.put(1)
    assert q.empty() == False
    assert q.full() == False
    q.put(2)
    q.put(3)
    assert q.empty() == False
    assert q.full() == True
    # q.put(4) # Exception:QueueFull

# Generated at 2022-06-14 12:54:45.723839
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

# Generated at 2022-06-14 12:54:54.383408
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q_maxsize=5
    from tornado.queues import Queue, QueueFull
    q = Queue()
    try:
        for i in range(0, q_maxsize+1):
            q.put_nowait(i)
            assert q.qsize() == i+1
    except QueueFull:
        assert q.qsize() == q_maxsize

test_Queue_put_nowait()

# Generated at 2022-06-14 12:54:57.101026
# Unit test for method get of class Queue
def test_Queue_get():
    # q = Queue(maxsize=2)
    q = Queue()
    q.put(1)
    assert q.get() == 1

# Generated at 2022-06-14 12:55:04.305502
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import time
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
       

# Generated at 2022-06-14 12:55:09.134004
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    print("test_Queue_put_nowait")
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    print("q._queue:",q._queue)
    result = q.qsize()
    answer = 2
    assert (result == answer)

# Generated at 2022-06-14 12:55:15.968970
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.__put_internal(1)
    q.__put_internal(2)
    try:
        q.get_nowait()
    except Exception:
        return # Success
    else:
        return # Failure



# Generated at 2022-06-14 12:55:24.916590
# Unit test for method get of class Queue
def test_Queue_get():
    __tracebackhide__ = True

    q = Queue(maxsize=2)

    # In versions of Python without native coroutines (before 3.5),
    # consumer() could be written as::

    # @gen.coroutine
    # def consumer():
    #     while True:
    #         item = yield q.get()
    #         try:
    #             print('Doing work on %s' % item)
    #             yield gen.sleep(0.01)
    #         finally:
    #             q.task_done()

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()


# Generated at 2022-06-14 12:55:37.272322
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    # Test case 1
    # one getter before putter.
    q._getters.append(None)
    q._unfinished_tasks += 1
    q._finished.clear()
    q._put(1)
    assert(q._unfinished_tasks == 1)
    assert(q._queue == deque([1]))
    assert(q._finished.is_set() == False)
    # Test case 2
    # one getter before putter, not full.
    q._getters.append(None)
    q._unfinished_tasks += 1
    q._finished.clear()
    q._put(1)
    assert(q._unfinished_tasks == 1)
    assert(q._queue == deque([1]))