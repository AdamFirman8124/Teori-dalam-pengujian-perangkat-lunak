

# Generated at 2022-06-14 12:46:06.499940
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    assert q.put_nowait(1) is None



# Generated at 2022-06-14 12:46:15.772884
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    def _get():
        element=q.get_nowait()
        summ=summ+element
        q.task_done()
    q = Queue(maxsize=3)
    print('Queue size is '+str(q.qsize()))
    print('Queue is full? '+str(q.full()))
    q.put(1)
    q.put(2)
    q.put(3)
    print('Queue size is '+str(q.qsize()))
    print('Queue is full? '+str(q.full()))
    summ=0
    _get()
    _get()
    _get()
    print('Queue size is '+str(q.qsize()))
    print('Queue is empty? '+str(q.empty()))

# Generated at 2022-06-14 12:46:23.369044
# Unit test for method put of class Queue
def test_Queue_put():
    import time
    import tornado
    import tornado.ioloop
    import tornado.queues
    # the __init__ function of Queue
    q = Queue(maxsize=2)
    # define an async function named consumer
    async def consumer():
        # appply the cycle to repeat the work
        # each work consists of an item
        # which is got from the Queue
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await tornado.gen.sleep(0.01)
            finally:
                # use q.task_done() to indicate that processing
                # the item is complete.
                q.task_done()
    # define another async function named producer

# Generated at 2022-06-14 12:46:35.789981
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():

    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    import pytest
    
    
    q = Queue(maxsize=2)
    # Case 1
    q.put_nowait(10)
    q.put_nowait(20)
    assert q.full() == True
    with pytest.raises(QueueFull):
        q.put_nowait(30)
    # Case 2
    q1 = Queue(maxsize=0)
    q1.put_nowait(10)
    q1.put_nowait(20)
    assert q1.full() == False
    q2 = Queue(maxsize=None)
    q2.put_nowait(10)
    q2.put_nowait(20)
    assert q

# Generated at 2022-06-14 12:46:39.410317
# Unit test for method get of class Queue
def test_Queue_get():
    import asyncio
    async def f():
        pass
    q = Queue()
    q.get()
    q.put(f)
    q.get()
    q.task_done()


# Generated at 2022-06-14 12:46:44.135343
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # test that the Queue raises an exception
    # when an item is not available
    q = Queue(maxsize = 0)
    test = True
    try:
        q.get_nowait()
    except:
        test = False
    assert(not test)

# Generated at 2022-06-14 12:46:55.213626
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
            #print('consumer: ', consumer())
            #print('item: ', item)
            #print('q: ', q)
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait

# Generated at 2022-06-14 12:47:07.944342
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():

    import time
    from tornado.queues import Queue, QueueEmpty

    q = Queue()
    now = time.time()

    assert q.qsize() == 0
    assert q.empty() == True
    assert q.full() == False

    with pytest.raises(QueueEmpty):
        q.get_nowait()

    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    q.put_nowait(4)
    q.put_nowait(5)

    assert q.qsize() == 5
    assert q.empty() == False
    assert q.full() == False

    assert q.get_nowait() == 1
    assert q.get_nowait() == 2

# Generated at 2022-06-14 12:47:19.996794
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    #test when queue has no free slots
    # -> raise QueueFull
    try:
        q.put_nowait(3)
    except Exception as e:
        assert type(e) == QueueFull
    #test when getters are waiting (queue empty)
    q.__put_internal = lambda x: None
    q._get = lambda: 1
    q._getters.append(Future())
    q.put_nowait(1)
    #test when putters are waiting (queue full)
    q = Queue(maxsize=1)
    q.__put_internal = lambda x: None
    q._get = lambda: 1
    q._putters.append((1,Future()))
   

# Generated at 2022-06-14 12:47:29.467073
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)

    @gen.coroutine
    def producer():
        item = 1
        yield q.put(item)
        assert q.qsize() == 1, "Queue put function error"

    @gen.coroutine
    def producer2():
        try:
            yield q.put(1, timeout=1)
            assert False, "Queue put function error"
        except gen.TimeoutError:
            assert q.qsize() == 1, "Queue put function error"
    # Run the unit test
    ioloop.IOLoop.current().run_sync(producer)
    ioloop.IOLoop.current().run_sync(producer2)



# Generated at 2022-06-14 12:47:37.753145
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    q.__put_internal(1)
    assert q._get() == 1


# Generated at 2022-06-14 12:47:46.157998
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.qsize() == 2
    assert q.get_nowait() == 1
    q.task_done()
    assert q.qsize() == 1
    with pytest.raises(QueueEmpty):
        q.get_nowait()
    assert q.get() is None
    q.put_nowait(3)
    q.task_done()



# Generated at 2022-06-14 12:47:58.057259
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # mock of the class
    class MockQueue():
        def _consume_expired(self):
            pass
        def qsize(self):
            return 0
        def __str__(self):
            return ""
    # mock of the function
    def side_effect(*args, **kwargs):
        return True
    def side_effect2(*args, **kwargs):
        return True
    queue = MockQueue()
    queue.full = MagicMock(side_effect=side_effect)
    queue.empty = MagicMock(side_effect=side_effect)
    # mock of the method
    queue._get = MagicMock(side_effect=side_effect2)
    queue.put_nowait = MagicMock(side_effect=side_effect2)

# Generated at 2022-06-14 12:47:59.987888
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    assert q.get_nowait() == None


# Generated at 2022-06-14 12:48:12.040674
# Unit test for method put of class Queue
def test_Queue_put():
    print("\n\nUnit test for method put of class Queue")
    async def test1():
        q = Queue(maxsize=2)
        print("Initial Queue:", q)
        
        future1 = q.put(1)
        print("Queue after put(1):", q)
        print("Future after put(1):", future1)
        await future1
        print("Queue after put(1) await:", q)
        
        future2 = q.put(2)
        print("Queue after put(2):", q)
        print("Future after put(2):", future2)
        await future2
        print("Queue after put(2) await:", q)
        
        future3 = q.put(3)
        print("Queue after put(3):", q)

# Generated at 2022-06-14 12:48:19.966778
# Unit test for method get of class Queue
def test_Queue_get():
    # import asyncio
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop

    q = Queue(maxsize=2)

    loop = IOLoop.current()

    async def consumer():
        # print("begin consumer")
        async for item in q:
            try:
                print("Doing work on %s" % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print("Put %s" % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.

# Generated at 2022-06-14 12:48:23.817847
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=0)
    q.put(1)
    q.put(2)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.qsize() == 0
    assert q.empty() is True
    assert q.full() is False


# Generated at 2022-06-14 12:48:28.594412
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado.queues import Queue 
    q = Queue(maxsize=2)
    q.put_nowait(4)
    q.put_nowait(3)
    assert(q.qsize()==2)

# Generated at 2022-06-14 12:48:41.195661
# Unit test for method get of class Queue
def test_Queue_get():
  import asyncio
  #Initialize the IOLoop
  loop = asyncio.get_event_loop()
  #Create a Queue
  q = Queue(maxsize=2)
  #Initialize a Future
  future = Future()
  try:
    #Call the put_nowait method of q
    q.put_nowait(0)
    #Call the put_nowait method of q
    q.put_nowait(1)
    #Call the get_nowait method of q
    item = q.get_nowait()
    #Set the result of future to the value of item
    future.set_result(item)
  except QueueEmpty:
    pass
  #Get the result of future
  x = future.result()
  #Assert that x has the value returned by get_nowait
  print

# Generated at 2022-06-14 12:48:49.413978
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    assert q.qsize() == 0
    q.put_nowait(0)
    assert q.qsize() == 1
    try:
        q.put_nowait(1)
        assert q.qsize() == 2
    except QueueFull:
        pass

    q = Queue(maxsize=0)
    assert q.qsize() == 0
    q.put_nowait(0)
    assert q.qsize() == 1
    try:
        q.put_nowait(1)
        assert q.qsize() == 2
    except QueueFull:
        pass

    q = Queue(maxsize=1)
    try:
        q.put_nowait(0)
        assert q.qsize() == 1
    except QueueFull:
        pass
   

# Generated at 2022-06-14 12:48:58.383394
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    try:
        q.put(1)
    except QueueFull:
        pass
    else:
        assert False


# Generated at 2022-06-14 12:49:04.481352
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    io_loop = ioloop.IOLoop.current()
    q = Queue(maxsize=2)
    io_loop.run_sync(q.put_nowait, 1)
    io_loop.run_sync(q.put_nowait, 2)
    io_loop.run_sync(q.put_nowait, 3)
    # ...

# Generated at 2022-06-14 12:49:06.923786
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    item = 1
    res = q.put(item)
    assert res is not None
    assert isinstance(res, Future)

# Generated at 2022-06-14 12:49:16.866818
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # test for maxsize = 0
    # normal case
    q = Queue(0)
    q.put_nowait(1)
    assert q.qsize() == 1
    # first do put_nowait then get_nowait
    q = Queue(0)
    q.put_nowait(1)
    assert q.get_nowait() == 1
    # first do put_nowait then get
    q = Queue(0)
    q.put_nowait(1)
    assert q.get().result() == 1
    # test for maxsize = 1
    # normal case
    q = Queue(1)
    q.put_nowait(1)
    assert q.qsize() == 1
    # first do put_nowait then get_nowait
    q = Queue(1)


# Generated at 2022-06-14 12:49:26.994764
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue()
    async def producer():
        for i in range(5):
            await q.put(i)
            print('Put %s' % i)
    async def consumer():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    async def main():
        IOLoop.current().spawn_callback(consumer)
        await producer()
        await q.join()
        print('Done')
    IOLoop.current().run_sync(main)


# Generated at 2022-06-14 12:49:33.848058
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado.ioloop
    import time
    q1 = Queue(maxsize=0)
    q1._queue.append(1)
    q1._queue.append(2)
    result = []
    result.append(q1.get())
    result.append(q1.get())
    tornado.ioloop.IOLoop.current().run_sync(q1.join)
    return result

# Generated at 2022-06-14 12:49:44.479026
# Unit test for method get of class Queue
def test_Queue_get():
    import time
    import random
    import sys
    from tornado.gen import coroutine, Task, Return
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.platform.asyncio import to_tornado_future
    from tornado.platform.asyncio import to_asyncio_future
    ###############################################
    # This function mimics the coroutine function in the test
    def my_get(q:Queue,timeout:float)->Future:
        return to_tornado_future(q.get(timeout=timeout))
    ###############################################
    # This function mimics the function put in the test
    def my_put(q:Queue, x:int)->Future:
        return to_tornado_future(q.put(x))
    ###############################################


# Generated at 2022-06-14 12:49:50.169674
# Unit test for method get of class Queue
def test_Queue_get():
    # test code
    # Test 1: get got the item in the queue
    # queue is empty
    # the result is expected to be __get_item__
    q = Queue(maxsize=2)
    q._queue = collections.deque()
    q._queue.append("__get_item__")
    assert q.get() == "__get_item__"



# Generated at 2022-06-14 12:49:52.618287
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=0)
    try:
        q.get_nowait()
    except QueueEmpty as e:
        print(e)

# Generated at 2022-06-14 12:50:03.698218
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

# Generated at 2022-06-14 12:50:16.925536
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # add some tests for class Queue
    import unittest
    try:
        from unittest.mock import patch, mock_open
    except:
        from unittest import mock
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    import io
    import sys, os

    # Define helper functions
    @gen.coroutine
    def func1(q):
        q.put_nowait(None)

    @gen.coroutine
    def func2(q):
        item = yield q.get()
        q.task_done()

    # Create an instance of a class 
    q = Queue(maxsize = 1)

    # Test the method with the example given in the docstring
    __tracebackhide__ = True

# Generated at 2022-06-14 12:50:22.293488
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    try:
        q.put_nowait(None)
        q.put_nowait(None)
        q.put_nowait(None)
        assert False
    except QueueFull:
        pass

    assert q.qsize() == 2



# Generated at 2022-06-14 12:50:28.399952
# Unit test for method get of class Queue
def test_Queue_get(): 
    q = Queue()
    f = q.get()
    ioloop.IOLoop.current().spawn_callback(f.result())
    q.put(0)

if __name__ == "__main__":
    import tornado
    import asyncio
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    asyncio.get_event_loop().run_until_complete(test_Queue_get())



# Generated at 2022-06-14 12:50:40.646361
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
    # End test
    test_getters = [0, 0, 1]
    test_putters = [0, 0, 1]
    test_tasks = [0, 0, 1]
    if __name__ == '__main__':
        IOLoop.current().spawn_callback(consumer)
        queue = collections.deque()
        _queue = queue
        maxsize = 2
        getters = collections.deque([])


# Generated at 2022-06-14 12:50:46.110426
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    item = 1

    def callback():
        print("callback called")
        print("test_Queue_put finished")

    future = q.put(item)
    assert isinstance(future, Future)
    future.add_done_callback(callback)
    print("test_Queue_put created")


# Generated at 2022-06-14 12:50:49.498903
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue() # queue with fixed size 5
    if q.get() == QueueEmpty():
        print("test_Queue_get: Successful")
    else:
        print("test_Queue_get: Failed")
    

# Generated at 2022-06-14 12:50:57.137247
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            print('Doing work on %s' % item)
            await gen.sleep(0.01)
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

# Generated at 2022-06-14 12:50:59.491716
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    assert not q.empty()
    assert not q.full()
    assert q.qsize() == 0
    q.put('test')
    assert not q.empty()
    assert not q.full()
    assert q.qsize() == 1

# Generated at 2022-06-14 12:51:06.618002
# Unit test for method put of class Queue
def test_Queue_put():
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
        io_loop = ioloop.IOLoop.current()
        io_loop.spawn_callback(consumer)
        await producer()
        await q.join()
        print('Done')

    # IOLoop.current().run_sync(main)

# Generated at 2022-06-14 12:51:18.549953
# Unit test for method get of class Queue
def test_Queue_get():

    def test_timeout(self):

        q = Queue(maxsize=1)

        @gen.coroutine
        def f():
            v1 = yield q.get()
            self.assertEqual(v1, 'foo')
            v2 = yield q.get(timeout=0.01)
            self.assertEqual(v2, 'bar')
            yield q.put('baz')

        io_loop = self.io_loop
        f = f()
        io_loop.add_callback(q.put, 'foo')
        io_loop.add_callback(q.put, 'bar')
        with self.assertRaises(gen.TimeoutError):
            io_loop.run_sync(f, timeout=1)
        # Even though f was cancelled, the getter that was returned by
        # the second get

# Generated at 2022-06-14 12:51:42.026678
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    print(q)        
    q.put_nowait(0)
    q.put_nowait(1)
    print(q)        
    
    print('get_nowait: %s' % q.get_nowait())
    q.task_done()
    print(q)
    print('get_nowait: %s' % q.get_nowait())
    q.task_done()
    print(q)
    print('get_nowait: %s' % q.get_nowait())
    q.task_done()
    q.task_done()
    print(q)
    print('get_nowait: %s' % q.get_nowait())


# Generated at 2022-06-14 12:51:51.951563
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    assert q.qsize() == 0
    q.__put_internal(1)
    assert q.get_nowait() == 1
    q.__put_internal(2)
    q.__put_internal(3)
    assert q.qsize() == 2
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    assert q.qsize() == 0
    try:
        q.get_nowait()
    except QueueEmpty:
        print("Test Pass")
    q.__put_internal(1)
    q.__put_internal(2)
    q.__put_internal(3)
    assert q.qsize() == 3
    assert q.get_nowait() == 1



# Generated at 2022-06-14 12:51:57.187764
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q2 = Queue()
    q3 = Queue()
    q.put(1)
    q2.put(2)
    q3.put(3)
    assert 1 == q.get_nowait()
    assert 2 == q2.get_nowait()
    assert 3 == q3.get_nowait()
#test_Queue_get_nowait()



# Generated at 2022-06-14 12:51:58.659170
# Unit test for method get of class Queue
def test_Queue_get():
    pass


# Generated at 2022-06-14 12:52:02.780033
# Unit test for method put of class Queue
def test_Queue_put():
    queue1 = Queue(maxsize=0)
    queue1.put(5)
    assert queue1.qsize() == 1
    future1 = queue1.put(6)
    assert future1.result() is None


# Generated at 2022-06-14 12:52:13.086951
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

# Generated at 2022-06-14 12:52:21.890283
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    @gen.coroutine
    def get_queue_without_put(q):
        try:
            item = yield q.get_nowait()
            return item
        except QueueEmpty:
            print("Queue is empty")
            return None

    @gen.coroutine
    def empty_queue(q):
        while not q.empty():
            await q.get()
        return True

    @gen.coroutine
    def my_put(q,i):
        await q.put(i)
        print("put",i)    
    
    q = Queue(maxsize=2)


# Generated at 2022-06-14 12:52:23.207581
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)


# Generated at 2022-06-14 12:52:27.263832
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    assert q.empty()
    try:
        q.put_nowait(0)
    except QueueFull:
        assert False
    assert not q.empty()


# Generated at 2022-06-14 12:52:35.363500
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    future_1 = q.get()
    future_2 = q.get()

    q.put_nowait(1)
    assert q.qsize() == 1

    q.put_nowait(2)
    assert q.qsize() == 2

    assert q.join() == None

    assert future_1.get_nowait() == 1
    assert q.qsize() == 1

    assert future_2.get_nowait() == 2
    assert q.qsize() == 0

    q.task_done()


# Generated at 2022-06-14 12:53:06.141452
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

# Generated at 2022-06-14 12:53:10.309449
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    try:
        q.get_nowait()
        return False
    except QueueEmpty:
        return True
test_Queue_put_nowait()



# Generated at 2022-06-14 12:53:19.538735
# Unit test for method put of class Queue
def test_Queue_put():
    # created an Queue
    q = Queue(maxsize=2)
    # create a method to be tested
    def put(self, item, timeout=10):
        future = Future()
        if self.maxsize != None:
            if self.maxsize != 0:
                try:
                    if self.qsize() >= self.maxsize:
                        # put item into a queue and set future result
                        self.put_nowait(item)
                        future.set_result(None)
                except QueueFull:
                    future_set_result_unless_cancelled(putter, None)
        else:
            try:
                # put item into a queue and set future result
                self.put_nowait(item)
                future.set_result(None)
            except QueueFull:
                future_set_result_

# Generated at 2022-06-14 12:53:22.630149
# Unit test for method put of class Queue
def test_Queue_put():
    q=Queue()
    q.put(1)
    if q.full():
        print("Success")
    else:
        print("Fail")

# Generated at 2022-06-14 12:53:30.783831
# Unit test for method put of class Queue
def test_Queue_put():
    import logging
    import tornado
    import asyncio
    from tornado.queues import Queue

    async def consumer():
        async for i in q:
            try:
                logging.info('Doing work on %s' % i)
                await tornado.gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for i in range(5):
            await q.put(i)
            logging.info('Put %s' % i)

    async def main():
        # Start consumer without waiting (since it never finishes).
        tornado.ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        logging.info('Done')

    q

# Generated at 2022-06-14 12:53:39.673229
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    
    assert q.qsize() == 0
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
        q.put_nowait(3)
    except Exception as e:
        assert type(e) == QueueFull


# Generated at 2022-06-14 12:53:49.555356
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop
    import time
    import random

    q = Queue(maxsize=2)

    async def producer():
        for item in range(1, 6):
            print("Put %s" % item)
            await q.put(item)

    async def consumer():
        print("\n")
        while True:
            try:
                item = q.get_nowait()
                print(item)
            except QueueEmpty:
                print('Queue Empty')
                IOLoop.current().stop()
                return

    IOLoop.current().run_sync(producer)
    IOLoop.current().run_sync(consumer)


if __name__ == '__main__':
    test_Queue_get_nowait()

# Generated at 2022-06-14 12:53:57.368506
# Unit test for method put of class Queue
def test_Queue_put():
    import time, sys
    import random
    import asyncio

    def _test_put(q):
        for i in range(100):
            passwd = asyncio.get_event_loop().run_until_complete(q.put(i, 1))
            if passwd != None:
                print("put succ:", i)
            else:
                print("put fail:", i)
                break

    def test_put():

        q = Queue()

        _test_put(q)
    if __name__ == '__main__':
        test_put()

# Generated at 2022-06-14 12:54:03.984953
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

# Generated at 2022-06-14 12:54:04.451383
# Unit test for method get of class Queue
def test_Queue_get():
    pass

# Generated at 2022-06-14 12:55:08.160518
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(0)
    q.put_nowait(1)
    q.put_nowait(2)
    return q



# Generated at 2022-06-14 12:55:16.727692
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    print('queue get test ')
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)

    def consumer():
        for _ in range(4):
            print(q.get().result())

    consumer()
    print('consumer finished')
    

# Generated at 2022-06-14 12:55:25.077804
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import random
    import time
    import unittest
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase

    _q = None
    _q_len = 10
    for i in range(0,_q_len):
        _q.put_nowait(i)

    class MyTest(AsyncTestCase):
        def test_queue(self):
            global _q, _q_len
            for i in range(0,_q_len):
                val = _q.get_nowait()
                self.assertEqual(val, i)

        def tearDown(self):
            global _q
            _q = None

    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-14 12:55:37.325605
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

# Generated at 2022-06-14 12:55:40.148805
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    def callback(f):
        print(1)
    q.put(1, callback)
    q.put(2, callback)
    print(q)


# Generated at 2022-06-14 12:55:52.727083
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