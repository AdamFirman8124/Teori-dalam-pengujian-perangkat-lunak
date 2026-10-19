

# Generated at 2022-06-14 12:46:22.717110
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        q.put_nowait(3)
    except QueueFull:
        pass

# Generated at 2022-06-14 12:46:26.509231
# Unit test for method get of class Queue
def test_Queue_get():
    qsize = 0
    ret_val = None
    q = Queue()
    ret_val = q.get(timeout=None)
    return ret_val

# Generated at 2022-06-14 12:46:32.357950
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():

    q = Queue()

    q.put_nowait(item="a")
    q.put_nowait(item="b")

    assert q.get_nowait() == "a"
    assert q.get_nowait() == "b"
    assert q.empty() == True
    
print("test_Queue_get_nowait Passed")


# Generated at 2022-06-14 12:46:41.049984
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

# Generated at 2022-06-14 12:46:51.266381
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    q = Queue()
    assert q.qsize() == 0
    assert q._unfinished_tasks == 0
    q.put_nowait(1)
    assert q.qsize() == 1
    assert q._unfinished_tasks == 1
    q.task_done()
    assert q.qsize() == 0
    assert q._unfinished_tasks == 0
    q.put_nowait(2)
    assert q.qsize() == 1
    assert q._unfinished_tasks == 1
    q.get_nowait()
    assert q.qsize() == 0
    assert q._unfinished_tasks == 0



# Generated at 2022-06-14 12:46:55.470262
# Unit test for method put of class Queue
def test_Queue_put():
    """ Unit test for method put of class Queue
    """
    future = Future() # type: Future[None]
    timeout = None
    q = Queue()
    item = 1
    assert isinstance(q.put(item, timeout), Future) == True
    assert isinstance(q.put_nowait(item), None) == True



# Generated at 2022-06-14 12:47:08.075054
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        q.put_nowait(3)
        assert 0
    except QueueFull:
        pass
    q.get_nowait()
    q.get_nowait()
    try:
        q.get_nowait()
        assert 0
    except QueueEmpty:
        pass
    q.put_nowait(3)
    assert q.qsize() == 1
    assert q.full() == False
    assert q.empty() == False
    q.put_nowait(4)
    assert q.full() == True
    q.get_nowait()
    q.get_nowait()
    assert q.empty() == True


# Generated at 2022-06-14 12:47:10.141470
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    assert q.queu
test_Queue_put_nowait()



# Generated at 2022-06-14 12:47:23.197624
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

# Generated at 2022-06-14 12:47:32.183929
# Unit test for method get of class Queue
def test_Queue_get():
    import random, string
    q = Queue()
    print(q.qsize())
    print(q.empty())
    print(q.full())

    print(type(q))
    
    if isinstance(q, Queue):
        print("q is a instance of Queue")
    else:
        print("q isn't a instance of Queue")

    if isinstance(q, collections.deque):
        print("q is a instance of collections.deque")
    else:
        print("q isn't a instance of collections.deque")

    for i in random.choices(string.ascii_uppercase + string.digits, k=10):
        print(i, end = ' ')
        q.put_nowait(i)
    print()

    print(q.qsize())
   

# Generated at 2022-06-14 12:47:43.166319
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.queues import Queue
    a = Queue(maxsize=2)
    a.put_nowait(1)
    assert a.get_nowait() == 1


# Generated at 2022-06-14 12:47:54.033948
# Unit test for method task_done of class Queue
def test_Queue_task_done():
    import time
    import asyncio
    q = Queue()
    async def consumer():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s', item)
                time.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s', item)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([consumer(), producer()]))
    q.join()
    print('Done')
    
    
    

# Generated at 2022-06-14 12:47:57.132645
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    try:
        q.get_nowait()
        raise Exception("Should raise QueueEmpty")
    except QueueEmpty:
        pass

# Generated at 2022-06-14 12:47:57.962866
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    pass


# Generated at 2022-06-14 12:48:03.500651
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import datetime
    q = Queue()
    q.put_nowait(1)
    assert q.get_nowait() == 1
    # Suppose get_nowait raises a QueueEmpty exception
    try:
        q.get_nowait()
    except QueueEmpty:
        pass


# Generated at 2022-06-14 12:48:14.330383
# Unit test for method put of class Queue
def test_Queue_put():

    # # put_nowait()
    q = Queue(maxsize=2)
    q.put_nowait(1)
    # put item
    assert q.qsize() == 1
    # queue has size 1 after put
    q.put_nowait(2)
    assert q.qsize() == 2
    # queue has size 2 after put
    try:
        q.put_nowait(3)
        # put_nowait() raise QueueFull
        assert False
    except QueueFull:
        pass

    # # put()
    q = Queue(maxsize=1)
    f = q.put(1)
    # normal put
    assert q.qsize() == 1
    assert f.done()
    assert f.result() is None
    f = q.put(3)
    # try

# Generated at 2022-06-14 12:48:18.845356
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.queues import Queue

    q = Queue()
    assert q.empty()

    q.put_nowait(1)

    assert not q.empty()

    assert q.get_nowait() == 1

    assert q.empty()



# Generated at 2022-06-14 12:48:25.802348
# Unit test for method put of class Queue
def test_Queue_put():
    import ioloop
    import queues
    import coroutines
    import future
    import util
    import types
    q = queues.Queue()
    f = future.Future()
    q.put(1,None)
    f = future.Future()
    q.put(1,None)
    f = future.Future()
    q.put(1,1)
    f = future.Future()
    q.put(1,"1")
    f = future.Future()
    q.put(1,datetime.datetime)
    f = future.Future()
    q.put(1,util.TimeoutError)
    f = future.Future()
    q.put(1,types.GeneratorType)


# Generated at 2022-06-14 12:48:35.830220
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # put_nowait()
    q = Queue(maxsize=2)
    try:
        q.put_nowait(3)
    except QueueFull:
        print('queue is full')
    else:
        print('queue is not full')

    # get_nowait()
    try:
        print(q.get_nowait())
    except QueueEmpty:
        print('queue is empty')
    else:
        print('queue is not empty')

test_Queue_get_nowait()


# Generated at 2022-06-14 12:48:39.378039
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    try:
        q.get_nowait()
        assert False
    except QueueEmpty as e:
        assert True

test_Queue_get_nowait()

# Generated at 2022-06-14 12:48:59.017954
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

# Generated at 2022-06-14 12:49:04.424754
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.__put_internal(1)
    q.__put_internal(2)
    try:
        q.get_nowait()
        q.get_nowait()
        q.get_nowait()
    except QueueEmpty:
        pass
    return

# Generated at 2022-06-14 12:49:11.309515
# Unit test for method put of class Queue
def test_Queue_put():
    import time
    import multiprocessing

    def run_queue_put(q):
        print('[queue_put start]')
        time.sleep(3)
        q.put(1)

    queue = Queue()

    t1 = multiprocessing.Process(target=run_queue_put, args=(queue,))
    t1.start()
    print('[queue_put start finished]')

    print('[main thread] queue.get: ', queue.get())

    t1.join()


# Generated at 2022-06-14 12:49:13.903324
# Unit test for method get of class Queue
def test_Queue_get():
    # Implement this placeholder.
    return


if __name__ == '__main__':
    test_Queue_get()

# Generated at 2022-06-14 12:49:25.122383
# Unit test for method get of class Queue
def test_Queue_get():
    # Testcase 1
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


# Generated at 2022-06-14 12:49:37.065690
# Unit test for method get of class Queue
def test_Queue_get():
    #  __init__(self, maxsize: int = 0) -> None
    q = Queue(maxsize=2)
    # put(self, item: _T, timeout: Optional[Union[float, datetime.timedelta]] = None) -> Future[None]
    q.put(1.0, 0.1)
    q.put(2.0, 0.2)
    q.put(3.0, 0.3)
    # get(self, timeout: Optional[Union[float, datetime.timedelta]] = None) -> Awaitable[_T]
    # get_nowait(self) -> _T
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()


# Generated at 2022-06-14 12:49:46.770763
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    assert q._getters == collections.deque([])
    assert q._putters == collections.deque([])
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


# Generated at 2022-06-14 12:49:56.206288
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.ioloop import IOLoop

    q = Queue(maxsize=2)

    async def producer():
        for item in range(5):
            await q.put(item)
            print("Put %s" % item)

    async def consumer():
        async for item in q:
            try:
                print("Doing work on %s" % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()  # Wait for producer to put all tasks.
        await q.join()  # Wait for consumer to finish all tasks.
        print("Done")

    IOLoop.current().run_sync(main)




# Generated at 2022-06-14 12:50:02.790048
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q_test = Queue(maxsize=0)
    q_test.empty() == True
    q_test.full() == False
    q_test.put_nowait(1)
    q_test.empty() == False
    q_test.full() == False
    q_test.task_done()
    q_test.join()

test_Queue_put_nowait()

# Generated at 2022-06-14 12:50:12.787336
# Unit test for method get of class Queue
def test_Queue_get():
    print("\n\nTest Queue_get")
    def test_Queue_get_helper():
        #Tests if get() blocks an ongoing put()
        q = Queue()
        p = q.put(2)
        q.put(1)
        assert q.get() == 1
        q.put(0)
        assert q.get() == 0
        assert q.get() == 2
    test_Queue_get_helper()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Generated at 2022-06-14 12:50:32.292988
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    q.put_nowait(4)
    return 0


# Generated at 2022-06-14 12:50:35.981027
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado.queues import Queue
    q = Queue()
    t = 1
    q.put(1)
    t = q.get()
    assert t == 1


# Generated at 2022-06-14 12:50:37.041583
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    set_trace()

# Generated at 2022-06-14 12:50:41.647631
# Unit test for method get of class Queue
def test_Queue_get():
    maxsize = 0
    self = Queue(maxsize)
    timeout = None  # type: Optional[Union[float, datetime.timedelta]]
    # Actual result
    future = self.get(timeout)
    # Expected result
    expected = future

    assert expected == future

# Generated at 2022-06-14 12:50:49.420726
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(3)
    assert q.maxsize == 3
    q.put_nowait(1)
    q.put_nowait(2)
    assert q._queue == deque([1, 2])
    assert q.full() == False
    q.put_nowait(3)
    assert q.full() == True
    assert q._queue == deque([1, 2, 3])
    try:
        q.put_nowait(4)
        assert False, "queue must be full"
    except QueueFull:
        pass


# Generated at 2022-06-14 12:50:59.648354
# Unit test for method put of class Queue
def test_Queue_put():
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
            yield q.put(item)
            print('Put %s' % item)

    @gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        yield producer()     # Wait for producer to put all tasks.
        yield q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    ioloop

# Generated at 2022-06-14 12:51:06.203688
# Unit test for method get of class Queue
def test_Queue_get():
    import unittest
    import tornado
    import random
    import time

    class TestQueue(unittest.TestCase):
        def setUp(self):
            self.queue = Queue()
            self.timeout = 0
            # put some elements
            for i in range(10):
                self.queue.put_nowait(i)
            
        def test_get(self):
            for i in range(10):
                a = self.queue.get()
                print(a)
                
    if __name__ == "__main__":
        unittest.main()
test_Queue_get()


# Generated at 2022-06-14 12:51:18.256940
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

# Generated at 2022-06-14 12:51:29.660705
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    from tornado import gen
    from tornado.queues import Queue

    q = Queue(maxsize=2)
    
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer(item):
        await q.put(item)
        print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        for i in range(5):
            IOLoop.current().spawn_callback(producer, i)
        await q.join()       # Wait for consumer to finish all tasks.

# Generated at 2022-06-14 12:51:38.273819
# Unit test for method get of class Queue
def test_Queue_get():
    temp = Queue()
    assert temp.empty() == True
    assert temp.full() == False
    temp.put_nowait(1) #Test that put_nowait adds to the queue
    assert temp.empty() == False
    temp.put_nowait(2) #Test that put_nowait adds to the queue
    temp.put_nowait(3) #Test that put_nowait adds to the queue
    assert temp.full() == True
    temp.get_nowait() #Test that get_nowait removes from the queue
    assert temp.empty() == False
    temp.get_nowait() #Test that get_nowait removes from the queue
    assert temp.empty() == False
    temp.get_nowait() #Test that get_nowait removes from the queue
    assert temp.empty() == True

# Generated at 2022-06-14 12:52:19.769087
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

# Generated at 2022-06-14 12:52:28.341887
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Create an queue object
    q = Queue(maxsize=10)
    # Add data to queue
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    # Get data from queue
    print("Get:", q.get_nowait())
    print("Get:", q.get_nowait())
    print("Get:", q.get_nowait())
    # Check if queue is empty
    if q.empty():
        print("Queue is empty")
    else:
        print("Queue is not empty")

if __name__ == "__main__":
    test_Queue_get_nowait()

# Generated at 2022-06-14 12:52:39.308305
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

test_Queue

# Generated at 2022-06-14 12:52:48.215007
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    assert q.get_nowait() == None
    q.put_nowait(None)
    assert q.get_nowait() == None
    try:
        q.get_nowait()
    except QueueEmpty as e:
        assert True
    else:
        assert False

    try:
        q.put_nowait(None)
        q.put_nowait(None)
        q.put_nowait(None)
    except QueueFull as e:
        assert True
    else:
        assert False

print(test_Queue_get_nowait())


# Generated at 2022-06-14 12:52:54.024899
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    # q.put_nowait(2)
    # q.put_nowait(3)
    q.put_nowait(0)
    q.put_nowait(1)
    # print(q.get())
    # q.put_nowait(2)
    # q.put_nowait('full')
    q.get()
    q.get()
    q.put_nowait(2)


# Generated at 2022-06-14 12:52:57.638905
# Unit test for method get of class Queue
def test_Queue_get():
    def mock_get():
        return 1

    async def go(q1: 'Queue[int]') -> None:
        res = await q1.get()
        return res

    q1 = Queue()
    q1._get = mock_get
    res = ioloop.IOLoop.current().run_sync(lambda: go(q1))
    assert res == 1



# Generated at 2022-06-14 12:53:08.362927
# Unit test for method put of class Queue
def test_Queue_put():
    def test_1(maxsize, item, timeout, result=None, error_type=None):
        q = Queue(maxsize)
        future = q.put(item, timeout)
        if error_type == None:
            future.result()
            assert result == None
        else:
            assert future.exception().__class__ == error_type

    #test case 1
    maxsize = 0
    item, timeout = 3, None
    test_1(maxsize, item, timeout)

    #test case 2
    maxsize = 2
    item, timeout = 3, None
    test_1(maxsize, item, timeout)

    #test case 3
    maxsize = 1
    item, timeout = 1, None
    test_1(maxsize, item, timeout)
    item, timeout = 1, None
    test

# Generated at 2022-06-14 12:53:13.099409
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    object_ = Queue()
    def test_Queue_get_nowait__0():
        try:
            return object_.get_nowait()
        except QueueEmpty:
            return None
    return test_Queue_get_nowait__0


# Generated at 2022-06-14 12:53:22.412184
# Unit test for method get of class Queue
def test_Queue_get():
    def callback(fut: Future[int]) -> None:
        try:
            fut.result()
            print("succeed")
        except gen.TimeoutError:
            print("timeout")

    async def main():
        q = Queue(maxsize = 2)
        q.put_nowait(1)
        q.put_nowait(2)

        fut = q.get()
        fut.add_done_callback(callback)
        await gen.sleep(0.1)
        assert fut.done()
        assert q.qsize() == 1

    ioloop.IOLoop.current().run_sync(main)


# Generated at 2022-06-14 12:53:26.316417
# Unit test for method get of class Queue
def test_Queue_get():
    # Test cases.
    # Each list provide the input of the method get and the expected result.
    test_cases = [
        [None, None]
    ]

    for i, test_case in enumerate(test_cases, 1):
        yield run_test, i, test_case[0], test_case[1]


# Generated at 2022-06-14 12:54:43.506669
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    """
    _queue.clear()
    self._getters.clear()
    self._putters.clear()
    self._finished.clear()
    self._unfinished_tasks = 0
    """
    q = Queue(maxsize=2)
    #items = ['item%d' % i for i in range(100)]
    c = [1,2,3,4,5]
    q._queue.append(1)
    q._queue.append(1)
    for i in c:
        q.get_nowait()
    #a = q.get_nowait()
    #a = q.get_nowait()
    #a = q.get_nowait()


# Generated at 2022-06-14 12:54:49.117713
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # GIVEN
    q = Queue(maxsize=2)
    assert q.empty()
    assert not q.full()

    # WHEN
    q.put_nowait(1)
    q.put_nowait(2)

    # THEN
    assert q.qsize() == 2
    assert not q.empty()
    assert q.full()


# Generated at 2022-06-14 12:54:55.223153
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q._queue = [1, 2]
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    try:
        q.get_nowait()
        assert False
    except QueueEmpty:
        pass

test_Queue_get_nowait()


# Generated at 2022-06-14 12:55:03.119983
# Unit test for method get of class Queue
def test_Queue_get():
    import time
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)
    q.put(0)
    q.put(1)
    q = None
    q = Queue(maxsize=2)
    @gen.coroutine
    def consumer():
        while True:
            item = yield q.get()
            try:
                print('Doing work on %s' % item)
                yield gen.sleep(0.01)
            finally:
                q.task_done()
    def main():
        IOLoop.current().spawn_callback(consumer)
        IOLoop.current().spawn_callback(producer)

    def producer():
        for item in range(2,4):
            q.put_nowait(item)
           

# Generated at 2022-06-14 12:55:06.740084
# Unit test for method get of class Queue
def test_Queue_get():
    from . import queue
    
    q = queue.Queue()
    f = q.get()
    q.put_nowait(1)
    print(f.result())
    print(q.qsize())

# Generated at 2022-06-14 12:55:14.208366
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Test case Variables
    q = Queue(maxsize=2)
    item = 1
    timeout = None

    # Print Initial Values
    print("\nInitial Values")
    print(f"q: {q}")
    print(f"item: {item}")
    print(f"timeout: {timeout}")

    # Print Expected Output
    print("\nExpected Output")
    print("q: <Queue maxsize=2 queue=[1]>")

    # Call Queue.put_nowait(item)
    print("\nResults")
    q.put_nowait(item)
    print(f"q: {q}")

test_Queue_put_nowait()


# Generated at 2022-06-14 12:55:23.743577
# Unit test for method put of class Queue
def test_Queue_put():
    import math
    import sys
    from collections import deque
    from queue import LifoQueue as LQ
    from queue import Queue as Q
    from queue import PriorityQueue as PQ
    from queue import Full, Empty
    from threading import Thread
    from time import time
    from time import sleep
    from time import monotonic
    from time import time_ns
    from time import perf_counter
    from time import process_time
    from random import random
    from random import sample
    from random import random
    from random import seed
    from random import uniform

    def get(inputQueue,expectedQueue):
        while len(expectedQueue) != 0:
            try:
                print('get:',inputQueue.get(True,1))
                expectedQueue.popleft()
            except:
                pass
            # print(expectedQueue)

# Generated at 2022-06-14 12:55:29.332839
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize = 2)
    q._put(1)
    assert q._queue[0] == 1
    q._put(2)
    assert q._queue[0] == 1
    assert q._queue[1] == 2
    assert q.get_nowait() == 1
    assert q._getters == []
    assert q._queue == deque([2])



# Generated at 2022-06-14 12:55:32.045812
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    assert q.get_nowait() == 0



# Generated at 2022-06-14 12:55:42.342615
# Unit test for method put of class Queue
def test_Queue_put():
    # Input unit test
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
