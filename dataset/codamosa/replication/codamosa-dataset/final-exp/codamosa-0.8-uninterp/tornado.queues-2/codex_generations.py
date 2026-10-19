

# Generated at 2022-06-14 12:46:36.158995
# Unit test for method put of class Queue
def test_Queue_put():
    import random
    import time
    import asyncio
    async def put(q):
        for i in range(10):
            await q.put(i+1)
        await q.put(None)
    # Test the queue
    q = Queue()
    ioloop.IOLoop.current().run_sync(lambda: put(q))
    while True:
        v = q.get_nowait()
        if v is None:
            break
    assert q.empty()



# Generated at 2022-06-14 12:46:49.015095
# Unit test for method put of class Queue
def test_Queue_put():

    import random
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                await gen.sleep(random.random())
            finally:
                q.task_done()

    async def producer():
        for item in range(1, 5):
            await q.put(item)
            print('Put %s' % item)
            await gen.sleep(random.random())

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.

# Generated at 2022-06-14 12:46:51.266503
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Queue_put_nowait is tested in the Queue class test
    pass

# Generated at 2022-06-14 12:46:55.030954
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize = 2)
    q.put_nowait(3)
    q.put_nowait(4)
    try:
        q.put_nowait(5)
    except QueueFull:
        assert True
    else:
        assert False
    



# Generated at 2022-06-14 12:46:58.173326
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    r = q.get()
    assert r != None

# Generated at 2022-06-14 12:47:09.364289
# Unit test for method get of class Queue
def test_Queue_get():
    ASYNCIO = 0
    FUTURES = 0
    TYPING = 0
    if ASYNCIO:
        import asyncio
        import tornado.platform.asyncio
        asyncio.set_event_loop_policy(tornado.platform.asyncio.AnyThreadEventLoopPolicy())
    else:
        from tornado.concurrent import TracebackFuture
        from tornado.queues import Queue, QueueEmpty
        from tornado.ioloop import IOLoop
        import queue
        import datetime
        import tornado.locks
        import tornado.gen

    if TYPING:
        from typing import Dict, List, Set, Tuple, Union
        from typing_extensions import Protocol

    if FUTURES:
        from concurrent import futures
    import concurrent.futures
    from concurrent.futures import Future


# Generated at 2022-06-14 12:47:14.277986
# Unit test for method get of class Queue
def test_Queue_get():
    """This test verifies the Queue passes a simple get() call

        Bug reported:
            https://github.com/python/mypy/issues/5904#issuecomment-363327149
    """
    q = Queue()
    q.get()

# Generated at 2022-06-14 12:47:26.409746
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

# Generated at 2022-06-14 12:47:35.924359
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import unittest
    import tornado
    import sys
    import os
    import logging

    def print_exc_plus():
        """
        Print the usual traceback information, followed by a listing of all the
        local variables in each frame.
        """
        tb = sys.exc_info()[2]
        while tb.tb_next:
            tb = tb.tb_next
        stack = []
        f = tb.tb_frame
        while f:
            stack.append(f)
            f = f.f_back
        stack.reverse()
        traceback.print_exc()
        print("Locals by frame, innermost last")
        for frame in stack:
            print()

# Generated at 2022-06-14 12:47:36.455737
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    pass

# Generated at 2022-06-14 12:47:58.356573
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    # test if q.put() is waiting
    f = q.put(1)
    assert q.qsize() == 1, "TEST FAILED, q.put() failed or q.put() didn't waiting"
    ret = f.result()
    assert (ret is None), "TEST FAILED, q.put() didn't waiting"
    # test if q.put() is blocking
    q = Queue(2)
    q.put_nowait(1)
    q.put_nowait(2)
    q.get_nowait()
    q.get_nowait()
    f = q.put(1)
    f = q.put(2)
    q.join()
    ret = f.result()

# Generated at 2022-06-14 12:48:10.311945
# Unit test for method get of class Queue
def test_Queue_get():
    result = []
    q = Queue(maxsize=3)
    q.put(1)
    q.put(2)
    q.put(3)

    t = IOLoop.current().spawn_callback(q.get)
    t2 = IOLoop.current().spawn_callback(q.get)
    t3 = IOLoop.current().spawn_callback(q.get)
    t4 = IOLoop.current().spawn_callback(q.get)
    t5 = IOLoop.current().spawn_callback(q.get)

    IOLoop.current().add_future(t, lambda future: result.append(future.result()))
    IOLoop.current().add_future(t2, lambda future: result.append(future.result()))

# Generated at 2022-06-14 12:48:12.739382
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(1)
    q.put_nowait(1)
    assert q.get_nowait() == 1



# Generated at 2022-06-14 12:48:17.178416
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    assert q.get_nowait() == 1, q.get_nowait()
    assert q.get_nowait() == 2, q.get_nowait()
    assert q.get_nowait() == 3, q.get_nowait()


# Generated at 2022-06-14 12:48:20.029288
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Prepare
    import tornado.queues
    q = tornado.queues.Queue(maxsize=2)

    # Execute
    t = q.get_nowait()



# Generated at 2022-06-14 12:48:25.687724
# Unit test for method get of class Queue
def test_Queue_get():
    import asyncio

    async def test_Queue_get_code():
        q = Queue()

        async def consumer():
            async for item in q:
                try:
                    print("Doing work on %s" % item)
                    await asyncio.sleep(0.01)
                finally:
                    q.task_done()

        async def producer():
            for item in range(5):
                await q.put(item)
                print("Put %s" % item)

        async def main():
            # Start consumer without waiting (since it never finishes).
            IOLoop.current().spawn_callback(consumer)
            await producer()  # Wait for producer to put all tasks.
            await q.join()  # Wait for consumer to finish all tasks.
            print("Done")

        IOLoop.current().run_sync(main)

# Generated at 2022-06-14 12:48:32.352768
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put(3)
    assert q.qsize() == 1
    q.put(4)
    assert q.qsize() == 2
    q.put(5)
    q.get()
    q.get()
    assert q.qsize() == 0
    
    

# Generated at 2022-06-14 12:48:41.984235
# Unit test for method put of class Queue
def test_Queue_put():
    # test normal case
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    f1 = q.put(3, timeout = 1)
    f2 = q.put(4)
    assert f1.done() and f1.result() == None
    assert f2.done() and f2.result() == None
    assert q.qsize() == 2
    # test timeout case
    f3 = q.put(5, timeout = 0)
    assert f3.done() and type(f3.exception()) == gen.TimeoutError



# Generated at 2022-06-14 12:48:47.026668
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

# Generated at 2022-06-14 12:48:49.190257
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    future = q.put("test")
    assert isinstance(future, Future)
    assert future.done()
    q.task_done()


# Generated at 2022-06-14 12:49:11.655090
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    if q.empty():
        q.put_nowait(1)
        assert q.full()
        q.task_done()
    else:
        assert False



# Generated at 2022-06-14 12:49:23.490835
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

# Generated at 2022-06-14 12:49:37.107885
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.queues import Queue
    q = Queue(maxsize=2)

    async def producer():
        for item in range(5):
            print('Put {}'.format(item))
            await q.put(item)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on {}'.format(item))
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    ioloop.IOLoop.current().run

# Generated at 2022-06-14 12:49:42.081098
# Unit test for method put of class Queue
def test_Queue_put():
    queue = Queue()
    import asyncio
    async def main():
        await queue.put('test')
        print('test passed')
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(main())


# Generated at 2022-06-14 12:49:46.703919
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    for i in range(5):
        q.put_nowait(i)
        print('Put %s' % i)
    print('Get qsize:' + str(q.qsize()))

    while not q.empty():
        print(q.get_nowait())
        print('Get qsize:' + str(q.qsize()))
    print('Put qsize:' + str(q.qsize()))


# Generated at 2022-06-14 12:49:56.174725
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    test_data = [1,2,3,4,5]
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in test_data:
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

# Generated at 2022-06-14 12:50:07.591383
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Test code
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


# Generated at 2022-06-14 12:50:13.193452
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=5)
    q.__put_internal('test1')
    q.__put_internal('test2')
    q.__put_internal('test3')
    q.__put_internal('test4')
    q.__put_internal('test5')
    if q.qsize() == 5:
        q.put_nowait('test6')

# Generated at 2022-06-14 12:50:24.935592
# Unit test for method put of class Queue
def test_Queue_put():
    import unittest
    import asyncio
    import time
    class test_Queue_put(unittest.TestCase):
        def test__Queue_put(self):
            q = Queue(maxsize=2)
            def producer():
                for item in range(5):
                    yield from q.put(item)
                    print('Put %s' % item)

            def consumer():
                async for item in q:
                    try:
                        print('Doing work on %s' % item)
                        await gen.sleep(0.01)
                    finally:
                        q.task_done()

            async def main():
                # Start consumer without waiting (since it never finishes).
                ioloop.IOLoop.current().spawn_callback(consumer)
                await producer()     # Wait for producer to put all tasks.

# Generated at 2022-06-14 12:50:27.298679
# Unit test for method get of class Queue
def test_Queue_get():
    pass
    # x = Queue()
    # assert type(x.get()) == Awaitable[_T]



# Generated at 2022-06-14 12:51:19.986040
# Unit test for method get of class Queue
def test_Queue_get():
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
       

# Generated at 2022-06-14 12:51:31.146376
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        print("Consumer 1") 
        while True:
            print("Consumer 2")
            item = await q.get()
            print("Consumer 3")
            try:
                print("Doing work on %s" % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        print("Producer 1")
        for item in range(5):
            print("Producer 2")
            await q.put(item)
            print("Put %s" % item)


# Generated at 2022-06-14 12:51:34.914356
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    _queue = Queue()
    _queue.put('a')
    value = _queue.get_nowait()
    assert value == 'a'

# Generated at 2022-06-14 12:51:35.457561
# Unit test for method put of class Queue
def test_Queue_put():
    pass


# Generated at 2022-06-14 12:51:44.063172
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

# Generated at 2022-06-14 12:51:49.319987
# Unit test for method get of class Queue
def test_Queue_get():
    # Create a queue.
    queue = Queue()
    # Enqueue something.
    queue.put("call get")
    # Try to get an item from the queue.
    message = queue.get()
    # Check the item is expected.
    assert message == "call get", "test_Queue_get.1 failed."
    print("test_Queue_get.1 passed.")


# Generated at 2022-06-14 12:51:54.910517
# Unit test for method put of class Queue
def test_Queue_put():
    queue = Queue(maxsize=2)
    print("test_Queue_put: queue.put(1)")
    print("test_Queue_put: queue.put(2)")
    queue.put(1)
    queue.put(2)
    print("test_Queue_put: queue.put(3)")
    queue.put(3)


# Generated at 2022-06-14 12:51:58.787985
# Unit test for method put of class Queue
def test_Queue_put():
    class MyQueue(Queue):
        def __init__(self, maxsize: int = 0) -> None:
            self._queue = collections.deque()
    mq = MyQueue()
    print(mq._queue)
    mq.put('a')
    print(mq._queue)
    mq._put('b')
    print(mq._queue)

# Generated at 2022-06-14 12:52:02.987628
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
  # Implement your test here
  q = Queue()
  assert(q.empty() == True)
  q.put_nowait(1)
  assert(q.empty() == False)
  return True


# Generated at 2022-06-14 12:52:05.855487
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    q.get_nowait()
if __name__ == '__main__':
    test_Queue_get()



# Generated at 2022-06-14 12:52:51.405372
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    @gen.coroutine
    def test_queue_get():
        q.put(2)
        assert (yield q.get()) == 2
        q.put_nowait(3)
        assert (yield q.get()) == 3
    ioloop.IOLoop.current().run_sync(test_queue_get)


# Generated at 2022-06-14 12:52:53.136144
# Unit test for method get of class Queue
def test_Queue_get():
    o = Queue()
    result = o.get()
    assert result is not None


# Generated at 2022-06-14 12:52:56.697145
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.qsize() == 2
    try:
        q.put_nowait(3)
    except QueueFull:
        assert True
    else:
        assert False

# Generated at 2022-06-14 12:53:07.998593
# Unit test for method get of class Queue
def test_Queue_get():
    from typing import Generic, TypeVar, Optional, Awaitable, List
    from tornado.ioloop import IOLoop
    from tornado.gen import coroutine
    from tornado.queues import Queue
    import queue
    import time
    import datetime
    _T = TypeVar("_T")

    def test_Queue_instance_method_get(self: "Queue[_T]", timeout: Optional[Union[float, datetime.timedelta]] = None) -> Awaitable[_T]:
        future = Future()  # type: Future[_T]
        
        try:
            future.set_result(self.get_nowait())
        except QueueEmpty:
            self._getters.append(future)
            _set_timeout(future, timeout)
        return future
    if __name__ == '__main__':
        q

# Generated at 2022-06-14 12:53:16.104392
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Are the code tested below correct?
    # We assume that the code is correct if the IO callback is called in count = 5
    # -> see the callback function in line 67 and the count() function in the class.
    # The code is wrong if the count = 4 and the data race is not handled!
    
    q = Queue(1)
    def put_item(x):
        q.put_nowait(x)
    
    q.put_nowait(1)
    put_item(2)
    put_item(3)
    put_item(4)
    put_item(5)


# Generated at 2022-06-14 12:53:24.249545
# Unit test for method get of class Queue
def test_Queue_get():
    import pytest
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            try:
                assert isinstance(q.qsize(),int)
            finally:
                q.task_done()
    async def producer():
        for item in range(2):
            await q.put(item)
    async def main():
        IOLoop.current().spawn_callback(consumer)
        await producer()
        await q.join()
        print('Done')
    IOLoop.current().run_sync(main)



# Generated at 2022-06-14 12:53:26.024955
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)


# Generated at 2022-06-14 12:53:37.875141
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    print("\ntest_Queue_get_nowait()")
    q = Queue(maxsize=2)
    try:
        q.get_nowait()
        print("not ok")
    except QueueEmpty:
        print("ok")
    q.put(1)
    q.put(2)
    try:
        q.put_nowait(3)
        print("not ok")
    except QueueFull:
        print("ok")
    try:
        q.put_nowait(3)
        print("not ok")
    except QueueFull:
        print("ok")
    assert(q.get_nowait() == 1)
    assert(q.get_nowait() == 2)

# Generated at 2022-06-14 12:53:45.525685
# Unit test for method get of class Queue
def test_Queue_get():
    """

    :return:
    """
    q = Queue(maxsize=0)
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert not q.empty()
    assert not q.full()
    try:
        q.put_nowait(3)
    except QueueFull:
        assert False
    assert q.qsize() == 1
    assert not q.empty()
    assert q.get() == 3
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()



# Generated at 2022-06-14 12:53:48.980714
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    print(q.put([1, 2, 3]))
    print(q.put("hello"))
    print(q.put({1, 2}))
    print("q.qsize:", q.qsize())



# Generated at 2022-06-14 12:55:24.167149
# Unit test for method get of class Queue
def test_Queue_get():
    for _ in range(10):
        q = Queue(maxsize=int(10))
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in expected:
            q.put_nowait(i)

        actual = []
        while not q.empty():
            actual.append(q.get_nowait())

        assert expected == actual

# Generated at 2022-06-14 12:55:28.575069
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import math
    import time
    import asyncio

    async def test():
        q = Queue()
        q.put_nowait(3)
        assert q.qsize() == 1
    asyncio.get_event_loop().run_until_complete(test())



# Generated at 2022-06-14 12:55:39.236369
# Unit test for method put of class Queue
def test_Queue_put():
    test_case = [
        {
            "input": {
                "item": 0,
                "maxsize": 0
            },
            "output": {
                "res": None
            }
        },
        {
            "input": {
                "item": 0,
                "maxsize": 1
            },
            "output": {
                "res": None
            }
        },
    ]
    for t in test_case:
        q = Queue(t["input"]["maxsize"])
        q.put(t["input"]["item"])
        assert q.full() == False
    print("test_Queue_put succeeded!")



# Generated at 2022-06-14 12:55:40.380886
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    f = q.get()
    assert isinstance(f, Future)

# Generated at 2022-06-14 12:55:41.937936
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.get_nowait()


# Generated at 2022-06-14 12:55:53.810746
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

# Generated at 2022-06-14 12:56:01.228531
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=1)
    async def consumer():
        item = await q.get()
        try:
            print('Doing work on %s' % item)
        finally:
            q.task_done()
    loop = ioloop.IOLoop.current()
    loop.spawn_callback(consumer)
    # loop.add_future(q.put(42), lambda f: print('Finished put future'))
    q.put(42)
    loop.start()

