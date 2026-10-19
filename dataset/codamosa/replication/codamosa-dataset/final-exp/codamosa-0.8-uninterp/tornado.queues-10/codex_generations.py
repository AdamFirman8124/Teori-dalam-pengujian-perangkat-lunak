

# Generated at 2022-06-14 12:46:31.401998
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print(item)
                #await gen.sleep(0.01)
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


# Generated at 2022-06-14 12:46:40.445620
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=1)

    @gen.coroutine
    def consumer():
        item = yield q.get()
        print('Doing work on %s' % item)
        yield gen.sleep(0.01)

    @gen.coroutine
    def producer():
        for item in range(5):
            print(item)
            yield q.put(item)
            print('Put %s' % item)

    @gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        yield producer()     # Wait for producer to put all tasks.
        yield q.join()       # Wait for consumer to finish

# Generated at 2022-06-14 12:46:45.726137
# Unit test for method put of class Queue
def test_Queue_put():
    import asyncio

    q1 = Queue(0)
    q2 = Queue(1)
    q3 = Queue(0)
    q4 = Queue(1)

    async def producer_0():
        await q1.put(10)
        q1._queue

    async def producer_1():
        await q2.put(10)
        q2._queue

    async def consumer_1():
        await q3.get()
        q3._queue

    def run(coroutines, *args, **kwargs):
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(asyncio.wait(coroutines))
        finally:
            loop.close()


# Generated at 2022-06-14 12:46:53.666675
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    item = 'a'
    timeout = None
    try:
        q.put_nowait(item)
    except QueueFull:
        future = Future()
        q._putters.append((item, future))
        _set_timeout(future, timeout)
    else:
        future = Future()
        future.set_result(None)

    print(hex(id(future)))
    print(hex(id(item)))
    print(hex(id(timeout)))

    return future


# Generated at 2022-06-14 12:47:03.761856
# Unit test for method put of class Queue
def test_Queue_put():
    @gen.coroutine
    def test1():
        async def consumer():
            async for item in q:
                print('Doing work on', item)
                await gen.sleep(0.01)

        q = Queue(maxsize=5)
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        for item in range(10):
            await q.put(item)
            print('Put', item)
        await q.join()

    ioloop.IOLoop.current().run_sync(test1)


# Generated at 2022-06-14 12:47:05.825192
# Unit test for method get of class Queue
def test_Queue_get():
    x = Queue()
    x.put(1)
    assert next(x.get()) == 1


# Generated at 2022-06-14 12:47:16.448911
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Test constructor
    q = Queue(maxsize=2)
    if q.maxsize != 2: raise RuntimeError
    # Test put_nowait
    q.put_nowait(3)
    if not q.qsize() == 1: raise RuntimeError
    q.put_nowait(4)
    if not q.qsize() == 2: raise RuntimeError
    # Test get_nowait
    if not q.get_nowait() == 3: raise RuntimeError
    if not q.get_nowait() == 4: raise RuntimeError
    # Test task_done
    q.put_nowait(5)
    q.put_nowait(6)
    if not q.get_nowait() == 5: raise RuntimeError
    if not q.get_nowait() == 6: raise RuntimeError
    q.task

# Generated at 2022-06-14 12:47:20.723928
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    # return the first element in the queue
    # If no free slot is immediately available, raise QueueFull.
    assert q.get_nowait() == NotImplementedError


# Generated at 2022-06-14 12:47:30.898931
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
   # Test the method Queue.get_nowait of class Queue
   q = Queue(maxsize=2)
   q.__put_internal(3)
   ret_3_1 = q.get_nowait()
   assert ret_3_1 == 3
   q.__put_internal(5)
   assert q.maxsize == 2
   q.__put_internal(7)
   assert q.qsize() == 2
   ret_5_1 = q.get_nowait()
   assert ret_5_1 == 5
   q.__put_internal(9)
   assert q.qsize() == 2
   assert q.full()
   ret_7_1 = q.get_nowait()
   assert ret_7_1 == 7
   ret_9_1 = q.get_nowait()


# Generated at 2022-06-14 12:47:40.546601
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Queue with no elements
    q = Queue(maxsize=0)
    with pytest.raises(QueueEmpty) as excinfo:
        q.get_nowait()
    assert "empty" in str(excinfo.value)
    # Queue with elements
    q = Queue(maxsize=10)
    q.put_nowait('0')
    assert q.get_nowait() == '0'
    # Queue with elements but empty
    q.put_nowait('1')
    assert q.get_nowait() == '1'
    with pytest.raises(QueueEmpty) as excinfo:
        q.get_nowait()
    assert "empty" in str(excinfo.value)
    # Empty queue but with maxsize
    q = Queue(maxsize=1)

# Generated at 2022-06-14 12:48:00.505412
# Unit test for method put of class Queue
def test_Queue_put():
    import tornado
    import asyncio
    loop = asyncio.new_event_loop()
    #asyncio.set_event_loop(loop)
    async def main():
        q = Queue(maxsize=2)
        async def consumer():
            while True:
                item = await q.get()
                try:
                    print('Doing work on %s' % item)
                    await asyncio.sleep(0.01)
                finally:
                    q.task_done()
        # Start consumer without waiting (since it never finishes).
        #ioloop.IOLoop.current().spawn_callback(consumer)
        tornado.ioloop.IOLoop.current().spawn_callback(consumer)
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
        await q

# Generated at 2022-06-14 12:48:03.081615
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    try:
        q.put_nowait(1)
        q.put_nowait(2)
    except:
        pass
    try:
        q.put_nowait(3)
    except QueueFull:
        pass

# Generated at 2022-06-14 12:48:04.518934
# Unit test for method get of class Queue
def test_Queue_get():
    pass


# Generated at 2022-06-14 12:48:12.260610
# Unit test for method get of class Queue
def test_Queue_get():
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
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    ioloop.IOLoop.current().run_sync(main)




# Generated at 2022-06-14 12:48:16.279500
# Unit test for method put of class Queue
def test_Queue_put():
    q=Queue()
    f1=q.put(3,timeout=None)
    assert f1.result()==None
    exception_flag=False
    try:
        q.put(5,timeout=None)
    except Exception as e:
        exception_flag=True
    assert exception_flag==True

# Generated at 2022-06-14 12:48:24.890231
# Unit test for method put of class Queue
def test_Queue_put():
    # Queue(int) -> Queue
    q = Queue() 
    # Queue.put_nowait(object) -> None
    q.put_nowait(1)
    # Queue.put(object, timeout=None) -> concurrent.futures._base.Future
    q.put(2,timeout=None)
    # Queue.put(object, timeout=1) -> concurrent.futures._base.Future
    q.put(3,timeout=1)
    # Queue.put(object, timeout=1.0) -> concurrent.futures._base.Future
    q.put(4,timeout=1.0)
    # Queue.put(object, timeout=datetime.timedelta(seconds=1)) -> concurrent.futures._base.Future

# Generated at 2022-06-14 12:48:38.681534
# Unit test for method put of class Queue
def test_Queue_put():
    """
    Unit test for method put of class Queue
    :return: None
    """
    q = Queue(maxsize = 2)
    assert q.maxsize == 2
    assert q.qsize() == 0
    assert q.empty() == True
    assert q.full() == False

    q.put_nowait(2)
    assert q.maxsize == 2
    assert q.qsize() == 1
    assert q.empty() == False
    assert q.full() == False

    q.put_nowait(3)
    assert q.maxsize == 2
    assert q.qsize() == 2
    assert q.empty() == False
    assert q.full() == True
    try:
        q.put_nowait(4)
        assert False
    except QueueFull:
        assert True




# Generated at 2022-06-14 12:48:40.587518
# Unit test for method get of class Queue
def test_Queue_get():
	q = Queue()
	res = q.get()
	print(res)


# Generated at 2022-06-14 12:48:42.552696
# Unit test for method put of class Queue
def test_Queue_put():
    # Arrange
    q = Queue()
    # Act
    q.put("value")
    # Assert
    assert q.get_nowait() == "value"


# Generated at 2022-06-14 12:48:49.483903
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import types
    import warnings
    import random
    import time
    from functools import partial
    from threading import Thread
    from multiprocessing import Process
    from typing import Any, Optional
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue()# type: Queue[Any]
    item = random.randrange(0, 10)
    q.put(item)
    assert q.get_nowait() == item
    assert not q
    with pytest.raises(QueueEmpty):
        q.get_nowait()


# Generated at 2022-06-14 12:49:03.683133
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    item = 1
    timeout = None
    # Put an item into the queue, perhaps waiting until there is room.
    q.put(item = item, timeout = timeout)
    print("Put item into the queue.")
    return

# Generated at 2022-06-14 12:49:10.005918
# Unit test for method get of class Queue
def test_Queue_get():
    async def test_get(q: "Queue[_T]", test_val: _T) -> None:
        get_r = q.get()
        assert isinstance(get_r, Future)
        assert gen.is_coroutine(get_r)
        assert await get_r == test_val
        assert isinstance(get_r.result(), _T)

    q = Queue()
    test_get(q, "test_val")



# Generated at 2022-06-14 12:49:13.452373
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
  q = Queue(maxsize=2)
  q.put_nowait(1)
  q.put_nowait(2)
  assert q.get_nowait() == 1, ValueError
  q.task_done()
  assert q.get_nowait() == 2, ValueError




# Generated at 2022-06-14 12:49:24.724963
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)
    # q is a Queue object

    async def consumer():
        async for item in q:
            try:
                # print('Doing work on %s' % item)
                # await gen.sleep(0.01)
                print('Doing work on {}'.format(item))
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put {}'.format(item))

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q

# Generated at 2022-06-14 12:49:37.150263
# Unit test for method put of class Queue
def test_Queue_put():
    async def test_function():

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

        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')


# Generated at 2022-06-14 12:49:40.551205
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(1)
    q.__put_internal(3)
    assert q.get_nowait() == 3


# Generated at 2022-06-14 12:49:48.294483
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
  q = Queue(maxsize=2)

  print('\n--- Start Unit Test ---\n')
  print('Start to test method "put_nowait" of class "Queue"')
  print('Case 1: put 0 to an empty queue')
  q.put_nowait(0)
  print('Case 2: put 1 to the queue')
  q.put_nowait(1)
  print('Case 3: put 2 to a full queue')
  try:
    q.put_nowait(2)
  except QueueFull:
    print('Case 3: passed')
  print('Case 4: put 2 to a full queue')
  try:
    q.put_nowait(2)
  except QueueFull:
    print('Case 4: passed')




# Generated at 2022-06-14 12:49:54.154550
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    assert q.qsize() == 0

    future = q.put(1)
    assert q.qsize() == 1
    assert future.done()
    assert future.result() == None

    future = q.put(2)
    assert q.qsize() == 2
    assert future.done()
    assert future.result() == None

    future = q.put(3)
    assert q.qsize() == 2
    assert not future.done()



# Generated at 2022-06-14 12:49:57.269961
# Unit test for method put of class Queue
def test_Queue_put():
    async def main():
        q = Queue()
        await q.put(1)
        await q.put(2)

    ioloop.IOLoop.current().run_sync(main)




# Generated at 2022-06-14 12:50:08.511193
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                # print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    # print(consumer)
    # print(consumer.__code__.co_code)
    async def producer():
        for item in range(5):
            await q.put(item)
            # print('Put %s' % item)


# Generated at 2022-06-14 12:50:19.476094
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put_nowait(123)
    assert q.get_nowait() == 123


# Generated at 2022-06-14 12:50:30.162825
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=1)
    q.put(1)
    assert q.get_nowait() == 1
    assert q.empty()

    q = Queue(maxsize=0)
    q.put(2)
    assert q.get_nowait() == 2
    assert q.empty()

    q = Queue()
    q._queue = [1, 2]
    assert q.get_nowait() == 1

    q._queue = [1]
    q._getters.append(None)
    assert q.get_nowait() == 1

    q._queue = []
    f = Future()
    q._getters.append(f)
    assert f in q._getters
    q._put(1)
    assert f.result() == 1
    assert not q._getters

   

# Generated at 2022-06-14 12:50:40.117707
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    future = Future()

    def test():
        assert not future.done()
        assert q._putters
        assert q._putters[0][0] == item
        assert q._putters[0][1] == future
        return future

    try:
        q.put_nowait(item)
    except QueueFull:
        pass
    else:
        raise ValueError("put_nowait must throw QueueFull")

    q.put(item, timeout=None)
    q.put(item, timeout=None).add_done_callback(lambda future: test())

    return future


# Generated at 2022-06-14 12:50:47.854710
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        q.put_nowait(3)
        assert False
    except QueueFull:
        assert True


# Generated at 2022-06-14 12:50:50.402082
# Unit test for method put of class Queue
def test_Queue_put():
	q = Queue(maxsize=2)
	ret = q.put(1)
	assert(not ret.done())
	ret = q.put(2)
	assert(ret.done())


# Generated at 2022-06-14 12:51:00.397239
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import unittest
    import io
    import sys

    class TestQueue(unittest.TestCase):
        def test_put_nowait(self):
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            q = Queue(maxsize=2)
            try:
                q.put_nowait(1)
                q.put_nowait(2)
                self.assertEqual(capturedOutput.getvalue(), '1\n2\n')
            except QueueFull as e:
                self.fail('QueueFull exception should not be raised')

            self.assertRaises(QueueFull, q.put_nowait, 3)
            self.assertEqual(capturedOutput.getvalue(), '1\n2\n3\n')

    unittest.main(exit=False)

# Generated at 2022-06-14 12:51:03.984831
# Unit test for method get of class Queue
def test_Queue_get():
    import pytest 
    from tornado.queues import QueueEmpty, Queue
    testq = Queue()
    testq.put_nowait(1)
    assert testq.get() == 1
    with pytest.raises(QueueEmpty):
        testq.get()



# Generated at 2022-06-14 12:51:06.461956
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put("a")
    q.get_nowait()
    if q.empty() == True:
        print("the queue is empty")
    else:
        print("the queue is not empty")


# Generated at 2022-06-14 12:51:09.877414
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    class Child_Queue(Queue):
        def _init(self):
            pass
        def _get(self):
            return None
        def _put(self,item):
            pass
    Child_Queue(maxsize=2)


# Generated at 2022-06-14 12:51:22.339987
# Unit test for method get of class Queue

# Generated at 2022-06-14 12:51:42.657326
# Unit test for method get of class Queue
def test_Queue_get():
    import unittest
    from tornado.testing import AsyncTestCase
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop
    import asyncio

    class MyTestCase(AsyncTestCase):
        q = Queue()
        def test_put_nowait_get_nowait(self):
            self.q.put_nowait(1)
            assert self.q.get_nowait() == 1
        def test_put_nowait_get(self):
            self.q.put_nowait(2)
            self.add_async_callback(self.q.get, self.stop)
            self.wait()

# Generated at 2022-06-14 12:51:54.427083
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    assert q.qsize() == 0
    q.put_nowait(0)
    assert q.qsize() == 1
    q.put_nowait(1)
    assert q.qsize() == 2
    try:
        q.put_nowait(2)
    except QueueFull:
        print('QueueFull')
    assert q.qsize() == 2

    q = Queue(maxsize=2)
    assert q.qsize() == 0
    q.put_nowait(0)
    assert q.qsize() == 1
    q.put_nowait(1)
    assert q.qsize() == 2
    q.get_nowait()
    assert q.qsize() == 1
    q.put_nowait(1)

# Generated at 2022-06-14 12:52:02.124433
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

# Generated at 2022-06-14 12:52:08.328738
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Create the queue
    q = Queue(maxsize=2)
    # Put an item into the queue without blocking
    assert q.empty() == True
    q.put_nowait(1)
    assert q.empty() == False
    q.put_nowait(2)
    assert q.empty() == False
    try:
        q.put_nowait(3)
    except QueueFull:
        assert type(q.qsize()) == int
        assert q.qsize() == 2


# Generated at 2022-06-14 12:52:11.675653
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue()
    queue.put_nowait(1)
    assert queue.get_nowait() == 1

# Generated at 2022-06-14 12:52:15.544556
# Unit test for method put of class Queue
def test_Queue_put():
    def test_put():
        q = Queue()
        for v in range(10):
            q.put("item" + str(v))
        for v in range(10):
            assert q.get() == "item" + str(v)
    test_put()

# Generated at 2022-06-14 12:52:19.628753
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q1 = Queue()
    q1.put_nowait(5)
    q1.put_nowait(9)
    val1 = q1.get_nowait()
    assert val1 == 5

# Generated at 2022-06-14 12:52:26.536465
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    
    @gen.coroutine
    def test(q):
        while True:
            item = yield q.get()
            print("test:", item)
    
    IOLoop.current().spawn_callback(test, q)
    
    time.sleep(1)
    q.put(1)
    time.sleep(1)
    q.put(2)
    time.sleep(1)
    q.put(3)
    time.sleep(1)
    q.put(4)
    time.sleep(1)
    q.put(5)

# test_Queue_get()

# Generated at 2022-06-14 12:52:37.347875
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    
    q = Queue(maxsize=1)    
    
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0)
            finally:
                q.task_done()
                
    async def producer():
        for item in range(1):
            await q.put(item)
            print('Put %s' % item)    
    
    async def main_test_Queue_get():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       #

# Generated at 2022-06-14 12:52:42.403358
# Unit test for method get of class Queue
def test_Queue_get():
    import typing
    import asyncio
    from tornado.ioloop import IOLoop
    async def func() -> None:
        q = Queue()
        await q.put(1)
        ret_value = await q.get()
        assert ret_value == 1
    IOLoop.current().run_sync(func)


# Generated at 2022-06-14 12:52:58.597764
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


# Unit test

# Generated at 2022-06-14 12:53:06.082484
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=10)

    async def consumer():
        #await q.put(message)
        async for item in q:
            print('Doing work on %s' % item)

    #await q.join()

    loop = IOLoop.current()
    loop.spawn_callback(consumer)
    loop.run_sync(consumer)

    #loop.start()


# Generated at 2022-06-14 12:53:13.528088
# Unit test for method put of class Queue
def test_Queue_put():
    # Test parameters
    maxsize = 0
    item = 0
    timeout = 0
    assert isinstance(item, int)
    assert isinstance(timeout, int) or isinstance(timeout, float) or isinstance(timeout, datetime.timedelta)

    q = Queue(maxsize)
    future = q.put(item, timeout)
    assert future.done()
    assert future.result() is None


# Generated at 2022-06-14 12:53:20.487282
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)

    q.put_nowait(3)
    assert q.qsize() == 1
    q.put_nowait(4)
    assert q.qsize() == 2

    with pytest.raises(QueueFull):
        q.put_nowait(5)
    assert q.qsize() == 2
    print(q)



# Generated at 2022-06-14 12:53:27.200907
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Sample code for the test
    q = Queue(maxsize=2)
    try:
        assert q.qsize() == 0
        val = q.get_nowait()
        sig = "a"
        if val == sig:
            print("Expected: ", sig, "\nGot: ", val)
    except QueueEmpty as e:
        sig = "b"
        if sig == "b":
            print("Expected: ", sig, "\nGot: ", e)
    try:
        assert q.qsize() == 0
        val = q.get_nowait()
        sig = "b"
        if val == sig:
            print("Expected: ", sig, "\nGot: ", val)
    except QueueEmpty as e:
        sig = "a"
        if sig == "b":
            print

# Generated at 2022-06-14 12:53:38.603490
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Queue.get_nowait
    #
    # Removes an item from the queue.
    # If the queue is empty, raises QueueEmpty.
    #
    # @return     the queued item, or the default
    # @exception  Queue.Empty  if the queue is empty
    #

    q = Queue()

    def test_get_empty():
        try:
            # Testing get_nowait of class Queue
            print("Testing.test_Queue_get_nowait.test_get_empty()")
            q.get_nowait()
        except QueueEmpty as e:
            print("test_get_empty(): [OK] Queue is empty, as expected.")
        else:
            raise Exception("test_get_empty(): [ERROR] Queue is not emptry!")


# Generated at 2022-06-14 12:53:48.685098
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    assert q.empty()
    assert not q.full()
    assert q.qsize() == 0
    assert q.get_nowait() == None
    assert q.put_nowait(1) == None
    assert not q.empty()
    assert not q.full()
    assert q.qsize() == 1
    assert q.get_nowait() == 1
    assert q.empty()
    assert not q.full()
    assert q.qsize() == 0
    q = Queue(maxsize = 1)
    assert q.empty()
    assert not q.full()
    assert q.qsize() == 0
    assert q.put_nowait(1) == None
    assert not q.empty()
    assert q.full()
    assert q.qsize() == 1

# Generated at 2022-06-14 12:53:58.619287
# Unit test for method get of class Queue
def test_Queue_get():
    # Create mock instance of Future class
    future = __mock_instance_of(Future)
    future.exception.return_value = None
    future.result.return_value = None
    future.done.return_value = None
    future.set_result.return_value = None
    # Create mock instance of IOLoop class
    ioloop = __mock_instance_of(ioloop.IOLoop)
    ioloop.current.return_value = ioloop
    ioloop.add_callback.return_value = None
    ioloop.time.return_value = None
    ioloop.add_timeout.return_value = None
    ioloop.remove_timeout.return_value = None
    # Create mock instance of _QueueIterator class

# Generated at 2022-06-14 12:54:08.223120
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

# Generated at 2022-06-14 12:54:13.897474
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Checking precondition of the method
    q = Queue(maxsize=2)
    q.__put_internal(0)
    q.__put_internal(1)
    # Checking the method body
    assert(q.qsize() == 2)
    try:
        q.put_nowait(2)
    except QueueFull:
        pass
    assert(q.qsize() == 2)


# Generated at 2022-06-14 12:54:39.045900
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    q.put(1)
    assert q.qsize() == 1
    print(q.get())


# Generated at 2022-06-14 12:54:43.108268
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    future = Future()
    future.set_result(None)
    q._putters.append((2, future))
    q.put_nowait(1)
    assert q._queue == collections.deque([2, 1])

# Generated at 2022-06-14 12:54:46.056644
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # check if it returns None after calling put_nowait with item to be added
    q = Queue(0)
    assert q.put_nowait(10)==None
    assert q.empty()==False
    assert len(q._queue)==1

# Generated at 2022-06-14 12:54:51.164085
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait(): pass
Queue.put_nowait.__doc__ = 'Put an item into the queue without blocking.\n\n        If no free slot is immediately available, raise `QueueFull`.\n        ';



# Generated at 2022-06-14 12:54:55.999488
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    assert q.qsize() == 0
    assert q.empty() == True
    assert q.full() == False
    q.put(item=1)
    assert q.qsize() == 1
    assert q.empty() == False
    assert q.full() == False



# Generated at 2022-06-14 12:55:00.493129
# Unit test for method get of class Queue
def test_Queue_get():
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
    
    q = Queue(maxsize=2)
    ioloop.IOLoop.current().run_sync(main)


# Generated at 2022-06-14 12:55:06.054258
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    def main():
        q = Queue(maxsize=1)
        future = q.get()
        future.set_result(None)
        io_loop = IOLoop.current()
        io_loop.start()
        io_loop.run_sync(main)
test_Queue_get()

# Generated at 2022-06-14 12:55:10.894292
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize = 0)
    future = Future() # type: Future[None]
    try:
        q.put_nowait(item = 1)
    except QueueFull:
        q._putters.append((1, future))
        _set_timeout(future, None)
    else:
        future.set_result(None)
    return future


# Generated at 2022-06-14 12:55:20.862590
# Unit test for method put of class Queue
def test_Queue_put():
    
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)
    @gen.coroutine
    def consumer():
        async for item in q:
            assert item == 0
    @gen.coroutine
    def test():
        await q.put(0)
        await q.put(1)
        IOLoop.current().spawn_callback(consumer)
        #await q.put(2)
    try:
        IOLoop.current().run_sync(test)
    except Exception:
        return True
    else:
        return False

# Generated at 2022-06-14 12:55:22.804493
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    q.get_nowait()
