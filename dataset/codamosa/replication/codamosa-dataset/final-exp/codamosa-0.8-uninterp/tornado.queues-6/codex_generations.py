

# Generated at 2022-06-14 12:46:12.106710
# Unit test for method put of class Queue
def test_Queue_put():
    def test_put_nowait():
        q = Queue(maxsize=2)
        q.put_nowait(1)
        q.put_nowait(2)
        try:
            q.put_nowait(3)
            assert False
        except QueueFull:
            pass
    test_put_nowait()



# Generated at 2022-06-14 12:46:19.617999
# Unit test for method get of class Queue
def test_Queue_get():
    def queue_put():
        task_done()
        yield q.put(None)

    def no_arg_get():
        yield q.get()
        yield q.task_done()

    def arg_get():
        yield q.get(0.01)
        yield q.task_done()
    q = Queue(2)
    ioloop.IOLoop.current().spawn_callback(queue_put)
    ioloop.IOLoop.current().run_sync(no_arg_get)
    ioloop.IOLoop.current().run_sync(arg_get)



# Generated at 2022-06-14 12:46:31.766068
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

# Generated at 2022-06-14 12:46:40.657130
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from random import randint
    from random import randrange
    from random import choice
    from random import sample
    from random import shuffle
    q = Queue(maxsize=0)
    try:
        y = choice(sample(range(0, 16), 16))
        print("%s != %s" % (q.qsize(), y))
    except Exception:
        pass
    try:
        y = shuffle([choice(sample(range(0, 16), 16)) for i in range(0, 16)])
        print("%s != %s" % (q.empty(), y))
    except Exception:
        pass
    try:
        y = choice(sample(range(0, 16), 16))
        print("%s != %s" % (q.full(), y))
    except Exception:
        pass

# Generated at 2022-06-14 12:46:45.897536
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

# Generated at 2022-06-14 12:46:48.646301
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    print(q.get_nowait())
test_Queue_get_nowait()


# Generated at 2022-06-14 12:46:51.476243
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    q.put(1)
    assert q._queue.__len__() == 1



# Generated at 2022-06-14 12:46:53.258136
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():

    q=Queue()
    q.put_nowait(13)
    assert q.get_nowait() == 13

# Generated at 2022-06-14 12:46:55.489358
# Unit test for method get of class Queue
def test_Queue_get():
    for test in [1, 2, 3]:
        q = Queue()
        q.put(test)
        assert q.get() == test


# Generated at 2022-06-14 12:47:03.874709
# Unit test for method put of class Queue
def test_Queue_put():
    async def consumer():
        print('A consumer begins.')
        await gen.sleep(0.01)
        result = await q.get()
        print('Consumer receives %s' % result)

    q = Queue()
    io_loop = ioloop.IOLoop.current()
    io_loop.spawn_callback(consumer)
    io_loop.run_sync(q.put, '123')


if __name__ == '__main__':
    test_Queue_put()

# Generated at 2022-06-14 12:47:25.423150
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():

    def _assert_queue_full_exception():
        try:
            aQueue._Queue__put_internal(2)
        except Exception as e:
            if not isinstance(e, QueueFull):
                raise ValueError("Exception instance is not QueueFull")


        try:
            aQueue.put_nowait(2)
        except Exception as e:
            if not isinstance(e, QueueFull):
                raise ValueError("Exception instance is not QueueFull")

    def _assert_queue_empty_exception():
        try:
            aQueue._Queue__get_internal()
        except Exception as e:
            if not isinstance(e, QueueEmpty):
                raise ValueError("Exception instance is not QueueEmpty")



# Generated at 2022-06-14 12:47:32.206597
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()

    @gen.coroutine
    def consumer():
        while True:
            item = yield q.get()
            print(item)
            q.task_done()

    @gen.coroutine
    def producer():
        for item in range(5):
            yield q.put(item)

    @gen.coroutine
    def main():
        ioloop.IOLoop.current().spawn_callback(consumer)
        yield producer()
        yield q.join()
        print('Done')

    ioloop.IOLoop.current().run_sync(main)



# Generated at 2022-06-14 12:47:41.370800
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                # await gen.sleep(0.01)
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

    IOLoop

# Generated at 2022-06-14 12:47:47.233972
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(50)
    q.put_nowait(51)
    try:
        q.put_nowait(49)
    except QueueFull:
        assert q.qsize() == 2

# Generated at 2022-06-14 12:47:48.063915
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    pass

# Generated at 2022-06-14 12:47:58.897723
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

# Generated at 2022-06-14 12:48:10.964905
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue() # 0
    q.put_nowait(1) # 1
    q.put_nowait(2) # 2
    i = q.get_nowait() # 3
    j = q.get_nowait() # 4
    q.put_nowait(3) # 5
    q.put_nowait(4) # 6
    q.put_nowait(5) # 7
    q.put_nowait(6) # 8
    q.put_nowait(7) # 9
    k = q.get_nowait() # 10
    l = q.get_nowait() # 11
    m = q.get_nowait() # 12
    n = q.get_nowait() # 13
    o = q.get_nowait() # 14



# Generated at 2022-06-14 12:48:19.346647
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import sys
    import os
    import ctypes
    import inspect
    cur_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    par_dir = os.path.dirname(cur_dir)
    sys.path.insert(0, par_dir)
    from _pytest.monkeypatch import MonkeyPatch
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.platform.asyncio import to_asyncio_future
    from tornado.queues import Queue
    from tornado.escape import utf8
    from tornado.concurrent import Future
    from tornado.platform.asyncio import any_io_executor, AnyThreadEventLoopPolicy
    from tornado.locks import Event



# Generated at 2022-06-14 12:48:21.885864
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    future = Future()
    try:
        q.put_nowait(future)
    except QueueFull:
        print("Queue is full")


# Generated at 2022-06-14 12:48:25.270267
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    print(q.get())
    print(q.get())


# Generated at 2022-06-14 12:48:34.194386
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    try:
        q.put_nowait(1, None)
    except QueueFull:
        raise


# Generated at 2022-06-14 12:48:44.860971
# Unit test for method get of class Queue
def test_Queue_get():
    import time
    import locale
    import sys
    import shutil
    import os
    import ctypes
    import subprocess
    import asyncio
    import asyncio
    import datetime
    import base64
    import contextlib
    import copy
    import email
    import functools
    import gzip
    import hashlib
    import http
    import io
    import json
    import logging
    import math
    import operator
    import pdb
    import pickle
    import random
    import re
    import secrets
    import socket
    import ssl
    import string
    import struct
    import tempfile
    import threading
    import time
    import tornado
    import tracemalloc
    import types
    import typing
    import uuid
    import zlib
    from tornado import testing
    from tornado import gen
   

# Generated at 2022-06-14 12:48:52.247699
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    # cput an item into the queue without blocking
    q.put_nowait(1) # put 1 into the queue
    q.put_nowait(2) # put 2 into the queue
    try:
        q.put_nowait(3) # put 3 into the queue
        q.put_nowait(3) # put 3 into the queue
    except QueueFull:
        pass
    try:
        q.get_nowait() # get the item in the queue
        q.get_nowait() # get the item in the queue
    except QueueEmpty:
        pass
    try:
        q.get_nowait() # get the item in the queue
        q.get_nowait() # get the item in the queue
    except QueueEmpty:
        pass

   

# Generated at 2022-06-14 12:48:59.019520
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    try:
        q.get_nowait()
        assert False
    except QueueEmpty:
        pass
    q.put_nowait(1)
    assert q.get_nowait() == 1
    try:
        q.get_nowait()
        assert False
    except QueueEmpty:
        pass



# Generated at 2022-06-14 12:49:01.434174
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    # assert q.full(), "queue not full"
    # assert_raises(QueueFull, q.put_nowait, 3)
    # time.sleep(1)
    # q.put_nowait(3)
test_Queue_put_nowait()


# Generated at 2022-06-14 12:49:05.412524
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Test that get_nowait() returns the first element
    q = Queue()
    q.put("b")
    q.put("a")
    assert q.get_nowait() == "b"


# Generated at 2022-06-14 12:49:14.284031
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
        #for item in range(5):
        item=0
        while True:
            print(q.qsize())
            await q.put(item)
            print('Put %s' % item)
            item += 1
            if item>=5:
                break
    async def producer1():
        #for item in range(5):
        item=10

# Generated at 2022-06-14 12:49:17.240138
# Unit test for method put of class Queue
def test_Queue_put():
    my_queue = Queue()
    my_queue.put(1,timeout=None)
    print('This is my queue: ', my_queue)


# Generated at 2022-06-14 12:49:27.483208
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





# Generated at 2022-06-14 12:49:30.090438
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=0)
    q.queue = [1, 2, 3]
    q.get_nowait()



# Generated at 2022-06-14 12:49:38.249469
# Unit test for method get of class Queue
def test_Queue_get():
    import asyncio
    async def get_test():
        q = Queue(maxsize=2)
        # put item 5 into the queue
        q.put_nowait(5)
        # get item 5 out of the queue
        item = await q.get()
        print(item)   # expected output: 5
    asyncio.run(get_test())


# Generated at 2022-06-14 12:49:39.178771
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()


# Generated at 2022-06-14 12:49:47.424315
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=10)
    q.put(1)
    assert q.qsize() == 1
    q.put(2)
    assert q.qsize() == 2
    assert q._get() == 1
    assert q._get() == 2
    q.put(3)
    assert q.qsize() == 1
    assert q.empty() == False
    assert q.full() == False
    q.put(4)
    q.put(5)
    q.put(6)
    q.put(7)
    q.put(8)
    q.put(9)
    q.put(10)
    q.put(11)
    assert q.full() == True
    assert q.empty() == False
    assert q.qsize() == 10
    assert q._get

# Generated at 2022-06-14 12:49:50.320921
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put(0)
    q.put(1)
    q.put(2)
    assert q.put(3) == None


# Generated at 2022-06-14 12:49:54.913989
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    maxsize = 1
    q = Queue(maxsize)
    # Test the function under normal conditions
    try:
        q.get_nowait()
    except QueueEmpty:
        print("QueueEmpty was raised since the queue was empty")
        # Test the function when it does not raise QueueEmpty
        q.put_nowait(0)
        q.get_nowait()



# Generated at 2022-06-14 12:50:06.285769
# Unit test for method put of class Queue
def test_Queue_put():
    import asyncio
    import tornado.gen
    import tornado.platform.asyncio
    import tornado.ioloop
    tornado.platform.asyncio.AsyncIOMainLoop().install()
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
        tornado.ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks

# Generated at 2022-06-14 12:50:14.250994
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
  """
  This class is used to test the function Queue.get_nowait
  """
  import queue
  import random
  class myQ(queue.Queue):
    def _get(self):
        return self.queue
  myQ1=myQ(maxsize=10)
  for x in range(10):
    myQ1._put(random.randint(1,10))
  if len(myQ1.get_nowait()) == 1:
    print("Test Passed.")
  else:
    print("Test Failed.")



# Generated at 2022-06-14 12:50:20.303998
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=5)
    # Enqueue all the elements of list1
    for i in range(5):
        q.put_nowait(i)
    # Dequeue all the elements of queue
    while q.empty() != True:
        print(q.get_nowait())
#Unit test for method put_nowait of class Queue

# Generated at 2022-06-14 12:50:30.722492
# Unit test for method get of class Queue
def test_Queue_get():
    # Test if get() works
    q = Queue()
    assert len(q._getters) == 0
    q.put(1)
    assert len(q._getters) == 0
    assert len(q._queue) == 1
    assert q.get() == 1
    assert q.get() == 1
    assert q.get() == 1
    assert len(q._queue) == 1
    assert len(q._getters) == 1
    q.task_done()
    assert len(q._getters) == 0
    assert len(q._queue) == 0

    # Test if get_nowait() works
    q = Queue()
    assert len(q._getters) == 0
    q.put(1)
    assert len(q._getters) == 0
    assert len(q._queue) == 1

# Generated at 2022-06-14 12:50:42.622043
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
		await producer()     # Wait

# Generated at 2022-06-14 12:50:57.402123
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            print('Doing work on %s' % item)

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

# Generated at 2022-06-14 12:51:05.907382
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    # Test for the case that the queue is empty.
    q._queue.clear()
    q._getters.clear()
    q._putters.clear()
    q._unfinished_tasks = 0
    # Put an element into the queue
    q.put_nowait(1)
    assert len(q._queue) == 1
    assert q._unfinished_tasks == 1
    # Put an element into the queue
    q.put_nowait(2)
    assert len(q._queue) == 2
    assert q._unfinished_tasks == 2
    # Test for the case that there is a getter
    q._queue.clear()
    q._getters.clear()
    q._putters.clear()
    q._unfinished_tasks = 0

# Generated at 2022-06-14 12:51:08.573214
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    assert q.qsize() == 1
    assert q.get_nowait() == 1
    assert q.qsize() == 0

# Generated at 2022-06-14 12:51:14.677960
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    try:
        q.put_nowait(1)
    except QueueFull:
        pass
    q.put_nowait(1)
    q.put_nowait(1)
    try:
        q.put_nowait(1)
    except QueueFull:
        pass

# Generated at 2022-06-14 12:51:26.830277
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Dummy values for queue, _getters and _putters
    _queue = collections.deque()
    _getters = collections.deque()
    _putters = collections.deque()
    _unfinished_tasks = 0
    # Create a Queue of size 1
    queue = Queue(maxsize = 1)
    # Use partial to pass concrete arguments to the function
    # Assert that calling the function with no parameters raises QueueFull
    assert_raises(QueueFull, partial(queue.put_nowait, "ab"))
    # Check if the queue is empty
    assert queue.empty() == True
    # Check if the queue is full
    assert queue.full() == False
    # Check if the _getters is empty
    assert len(queue._getters) == 0
    # Check if the _putters is empty

# Generated at 2022-06-14 12:51:36.573455
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
        await q.join()       # Wait for consumer to

# Generated at 2022-06-14 12:51:41.792429
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)
    # Start consumer without waiting (since it never finishes).
    IOLoop.current().spawn_callback(consumer)
    await producer()     # Wait for producer to put all tasks.
    await q.join()       # Wait for consumer to finish all tasks.
    print('Done')


# Generated at 2022-06-14 12:51:52.057277
# Unit test for method put of class Queue
def test_Queue_put():
    a = Queue(maxsize=2)
    f1 = Future()
    f2 = Future()
    f3 = Future()
    f4 = Future()
    f5 = Future()
    f6 = Future()
    f7 = Future()
    f8 = Future()
    a.put_nowait(1)
    a.put_nowait(2)
    a._putters.append((3, f1))
    a._putters.append((4, f2))
    a._putters.append((5, f3))
    a._putters.append((6, f4))
    a._getters.append(f5)
    a._getters.append(f6)
    a._getters.append(f7)
    a._getters.append(f8)

# Generated at 2022-06-14 12:51:52.559259
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    pass

# Generated at 2022-06-14 12:52:03.124060
# Unit test for method get of class Queue
def test_Queue_get():
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # 1, test unit for get with no block
    # 2, test unit for get with block
    # 3, test unit for get with timeout

    q = Queue(maxsize=2)
    print ("start test_Queue_get")
    try:
        q.get_nowait()
    except:
        assert type(QueueEmpty()) is QueueEmpty

    q.put(1)
    assert type(1) is int
    assert q.get_nowait() is 1
    q.put(2)
    assert q.get(timeout=0) is 2

    try:
        q.get(timeout=1)
    except:
        assert type(gen.TimeoutError()) is gen.TimeoutError

    q.task

# Generated at 2022-06-14 12:52:22.547581
# Unit test for method put of class Queue
def test_Queue_put():
    
    q = Queue(maxsize=2)
    q._Queue__queue = []
    q._Queue__put_internal = lambda item: q._Queue__queue.append(item)
    q._finished = Event()
    q.put_nowait(1)
    assert q._Queue__queue == [1], "Fails to add item to queue"
    assert q._finished.is_set() == False, "Fails to unset event" 
    assert q._unfinished_tasks == 1, "Fails to increament unfinished_tasks"

    q = Queue(maxsize=2)
    q._Queue__queue = []
    q._Queue__put_internal = lambda item: q._Queue__queue.append(item)
    q._finished = Event()
    q._getters = []

# Generated at 2022-06-14 12:52:27.342263
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    q.put(1)
    assert q._queue == deque([1])
    q.put_nowait(2)
    assert q._queue == deque([1, 2])
    f = q.put(3)
    assert type(f) == Future
    assert f.result() == None
    q.put(4, timeout = 1)
    assert q._queue == deque([1, 2, 3, 4])

# Generated at 2022-06-14 12:52:38.322065
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




# Generated at 2022-06-14 12:52:49.048940
# Unit test for method get of class Queue
def test_Queue_get():
    # Setup
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

    # Execute
    ioloop.IOLoop.current().run_

# Generated at 2022-06-14 12:52:54.970033
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    assert q.empty() == True
    assert q.full() == False
    q.put(1)
    q.put(2)
    assert q.qsize() == 2
    q.put(3)
    assert q.qsize() == 3
    assert q.full() == True
    q.get_nowait()
    q.get_nowait()
    assert q.empty() == False
    assert q.full() == False
test_Queue_put()

# Generated at 2022-06-14 12:53:01.933949
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    assert q.empty() == True
    assert q.qsize() == 0
    q.put(5)
    assert q.qsize() == 1
    assert q.empty() == False
    q.put(6)
    assert q.qsize() == 2
    assert q.empty() == False

# Generated at 2022-06-14 12:53:06.081744
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(5)
    assert q.put_nowait(1) == None
    assert q.get_nowait() == 1
    assert q.put(1, timeout=1) == None
    assert q.qsize() == 1

test_Queue_put()

# Generated at 2022-06-14 12:53:10.309208
# Unit test for method put of class Queue
def test_Queue_put():
    q=Queue(maxsize=1)
    a=q.put(1,timeout=None)
    assert(a.result()==None)


# Generated at 2022-06-14 12:53:18.235623
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(5)
    assert len(q._queue)==1
    try:
        q.put_nowait(5)
        assert False
    except QueueFull:
        pass
    assert len(q._queue) == 1
    q.maxsize=2
    q.put_nowait(6)
    assert len(q._queue) == 2
    try:
        q.put_nowait(5)
        assert False
    except QueueFull:
        pass
    assert len(q._queue) == 2
    try:
        q.put_nowait(None)
        assert False
    except TypeError as e:
        pass


# Generated at 2022-06-14 12:53:19.337252
# Unit test for method put of class Queue
def test_Queue_put():
    return True



# Generated at 2022-06-14 12:53:44.133458
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import queue
    qu = queue.Queue()
    qu.put(1)
    assert qu.get_nowait() == 1



# Generated at 2022-06-14 12:53:45.570787
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    assert q.get_nowait() == None

# Generated at 2022-06-14 12:53:46.473003
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    pass


# Generated at 2022-06-14 12:53:56.851873
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    # case1: put an item when there is no free slot, but there is a waiting getter
    #        which has not reach its timeout
    future = Future()
    try:
        q.put_nowait(1)
    except QueueFull as e:
        raise Exception(e)
    try:
        q.put_nowait(2)
    except QueueFull as e:
        raise Exception(e)
    try:
        q.put_nowait(3)
    except QueueFull as e:
        raise Exception(e)
    else:
        raise Exception("the queue should be full!")
    # case2: put an item when there is no free slot and there is a waiting getter which reaches its timeout
    future = Future()

# Generated at 2022-06-14 12:53:58.089038
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    result = Queue().put_nowait("x")
    assert result is None

# Generated at 2022-06-14 12:53:58.745973
# Unit test for method put of class Queue
def test_Queue_put():
    pass

# Generated at 2022-06-14 12:54:08.323002
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import random
    max_item = 5
    item_need = 7
    queue = Queue(max_item)
    for i in range(max_item):
        queue.put_nowait(i)
    count = 0
    for i in range(item_need):
        count += 1
        print('第{0}次取队列中的元素'.format(count))
        index = random.randint(0,queue.qsize() - 1)
        print('队列中元素个数为：{0}'.format(queue.qsize()))

# Generated at 2022-06-14 12:54:17.849224
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

# Generated at 2022-06-14 12:54:25.240700
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

# Generated at 2022-06-14 12:54:36.041252
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
		await q.join()       # Wait for consumer to finish all

# Generated at 2022-06-14 12:55:10.311833
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    def get_nowait(q):
        size = q.qsize()
        while True:
            if size == 0:
                try:
                    q.get_nowait()
                except QueueEmpty:
                    return            
            else:
                temp = q.get_nowait()
                assert q.full() == False
                assert q.empty() == False
                size -= 1
                continue
    
    q1 = Queue(0)
    q2 = Queue(1)
    q3 = Queue(2)
    q4 = Queue(3)
    qs = [q1, q2, q3, q4]
    for q in qs:
        get_nowait(q)

# Generated at 2022-06-14 12:55:18.260654
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=0)

    assert q.empty() == True

    try:
        item = q.get_nowait()
    except QueueEmpty:
        print('queue is empty')

    q.put_nowait(1)
    #q.put_nowait(2)

    assert q.empty() == False

    item = q.get_nowait()
    assert item == 1


# Generated at 2022-06-14 12:55:26.139518
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    q._init()
    q._queue = [1, 2]
    q._getters = collections.deque([Future()])
    q._unfinished_tasks = 1
    q._finished = Event()
    q.task_done()
    q._consume_expired()
    assert q._getters == [], "getters not empty"
    assert q._unfinished_tasks == 0, "task not done"
    q._queue = []
    with pytest.raises(QueueEmpty):
        q._getters = collections.deque([Future()])
        q.get_nowait()
    q._getters = collections.deque([Future()])
    q._unfinished_tasks = 1
    f = Future()
    f.set_result(1)

# Generated at 2022-06-14 12:55:27.244753
# Unit test for method get of class Queue
def test_Queue_get():
    pass


# Generated at 2022-06-14 12:55:38.620591
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
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')
    
    IOLoop.current().run_sync(main)

# Generated at 2022-06-14 12:55:41.944521
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import time
    q = Queue()
    q.put(1)
    assert q.get_nowait() == 1
    try:
        q.get_nowait()
    except QueueEmpty:
        pass
    else:
        assert 0, "Failed to raise exception"


# Generated at 2022-06-14 12:55:44.584342
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    f = q.get()
    assert isinstance(f, Future)

# Generated at 2022-06-14 12:55:47.536278
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
	q = Queue()
	q.put_nowait(2)
	q.put_nowait(3)
	return q

# Generated at 2022-06-14 12:55:56.332120
# Unit test for method put of class Queue
def test_Queue_put():
    # Create a queue
    q = Queue(maxsize=5)
    # Test the function put in class Queue
    # Output:
    # Put 0
    # Put 1
    # Doing work on 0
    # Put 2
    # Doing work on 1
    # Put 3
    # Doing work on 2
    # Put 4
    # Doing work on 3
    # Doing work on 4
    # Done
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
