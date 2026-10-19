

# Generated at 2022-06-14 12:46:22.754612
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    assert q.empty() == True
    q.put_nowait(1)
    assert q.qsize() == 1
    q.put(2, timeout=0.1)
    assert q.full() == True
    assert q.qsize() == 2



# Generated at 2022-06-14 12:46:26.558682
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    item = 1
    q.put(item)
    assert q.qsize() == 1
    assert q._queue[0] == item


# Generated at 2022-06-14 12:46:28.298711
# Unit test for method get of class Queue
def test_Queue_get():

    return None



# Generated at 2022-06-14 12:46:32.998907
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import pytest
    q = Queue(maxsize=2)
    assert q.maxsize == 2
    q.put_nowait(1)
    q.put_nowait(2)
    #for i in range(1, 3):
    #    q.put_nowait(i)
    for i in range(1, 3):
        assert q.qsize() == 2 - i
        assert q.get_nowait() == i
    with pytest.raises(QueueEmpty):
        q.empty()
        q.get_nowait()

test_Queue_get_nowait()


# Generated at 2022-06-14 12:46:38.173370
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    x = q.put_nowait(3)
    assert x == None
    x = q.put_nowait(4)
    assert x == None
    assert q.empty() == False
    assert q.full() == True
    


# Generated at 2022-06-14 12:46:42.909014
# Unit test for method put of class Queue
def test_Queue_put():
    try:
        import asyncio
    except ImportError:
        msg = "the asyncio module is not available"
        raise unittest.SkipTest(msg)
    # pass
    raise NotImplementedError()

# Generated at 2022-06-14 12:46:54.137398
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    def consumer():
        try:
            while True:
                print('Doing work on %s' % item)
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


# Generated at 2022-06-14 12:47:06.963543
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

# Generated at 2022-06-14 12:47:08.950131
# Unit test for method get of class Queue
def test_Queue_get():
    myQueue = Queue()
    myQueue.get()
    expected = 1
    actual = myQueue.qsize()
    assert expected == actual


# Generated at 2022-06-14 12:47:21.622896
# Unit test for method get of class Queue
def test_Queue_get():
    import time
    import random
    import asyncio
    import tornado.queues
    import tornado.ioloop
    import tornado.gen

    async def producer(id, q):
        while True:
            ans = await q.put(id)
            await asyncio.sleep(random.random())
            print("producer %s: put %s" % (id, ans))

    async def consumer(id, q):
        while True:
            ans = await q.get()
            await asyncio.sleep(random.random())
            print("consumer %s: got %s" % (id, ans))
            q.task_done()

    async def main():
        for i in range(4):
            q = tornado.queues.Queue(maxsize=2)
            for j in range(3):
                tornado.ioloop.I

# Generated at 2022-06-14 12:47:35.510243
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    assert q.empty()
    q.put_nowait(1)
    assert not q.empty()
    q.put_nowait(2)
    assert not q.empty()
    try:
        q.put_nowait(3)
        assert False
    except QueueFull:
        assert True

# Generated at 2022-06-14 12:47:42.313568
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    assert q.qsize() == 1
    assert q.empty() == False
    assert q.full() == False

    q.put_nowait(2)
    assert q.qsize() == 2
    assert q.empty() == False
    assert q.full() == True
    try:
        q.put_nowait(1)
    except QueueFull as e:
        assert str(e) == 'queue full'
    else:
        assert False, 'put_nowait does not raise QueueFull when full'

test_Queue_put_nowait()



# Generated at 2022-06-14 12:47:46.211578
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put(1)
    q.put(2)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2


# Generated at 2022-06-14 12:47:55.784363
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)

    assert(q.get_nowait() == 1)
    assert(q.get_nowait() == 2)
    assert(q.get_nowait() == 3)
    assert(q.get_nowait() == 4)
    assert(q.get_nowait() == 5)
    q.put(6)
    assert(q.get_nowait() == 6)


# Generated at 2022-06-14 12:47:59.293102
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    def t():
        for i in range(3):
            q.put_nowait(str(i))
    t()
    L= [i for i in q._queue]
    return L == ['0','1','2']


# Generated at 2022-06-14 12:48:02.130673
# Unit test for method put of class Queue
def test_Queue_put():
    # A test for method put of class Queue
    # No value was given for parameter timeout. The default value 1 was assumed.
    pass

# Generated at 2022-06-14 12:48:13.550291
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

# Generated at 2022-06-14 12:48:23.643885
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

# Generated at 2022-06-14 12:48:27.056722
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    q.put(1)
    assert q.get_nowait()==1
    assert q.qsize()==0


# Generated at 2022-06-14 12:48:30.396761
# Unit test for method put of class Queue
def test_Queue_put():
    import queue
    #test_Queue_put_0
    myQueue = queue.Queue()
    myQueue.put(1)


# Generated at 2022-06-14 12:48:40.291374
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    pass

# Generated at 2022-06-14 12:48:48.298787
# Unit test for method get of class Queue
def test_Queue_get():
    # Test 1
    q = Queue()
    item = q.get()
    # Test 2
    q = Queue()
    q.qsize()
    # Test 3
    q = Queue()
    q.empty()
    # Test 4
    q = Queue()
    q.full()
    # Test 5
    q = Queue()
    item = q.put(1)
    # Test 6
    q = Queue()
    q.put_nowait(1)
    # Test 7
    q = Queue()
    q.full()
    # Test 8
    q = Queue()
    q.qsize()
    # Test 9
    q = Queue()
    q.empty()
    # Test 10
    q = Queue()
    q.qsize()
    # Test 11


# Generated at 2022-06-14 12:48:51.516653
# Unit test for method get of class Queue
def test_Queue_get():
    a = tornado.ioloop.IOLoop.current()
    q = Queue(maxsize=1)
    item = q.get()
    if q._getters > 1:
        return True
    else:
        return False

# Generated at 2022-06-14 12:48:55.693516
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    test_q = Queue()
    try:
        test_q.put_nowait({"aaa" : "bbb"})
    except Exception as e:
        print(e)
    else:
        print("put success")


# Generated at 2022-06-14 12:49:07.700192
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

# Generated at 2022-06-14 12:49:09.495203
# Unit test for method put of class Queue
def test_Queue_put():
    my_queue = Queue()
    my_queue.put("test")



# Generated at 2022-06-14 12:49:12.786346
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    q.put(1)
    q.put(2)
    q.qsize()
    q.put_nowait(5)
    q.empty()
    q.full()
    test_Queue_put()


# Generated at 2022-06-14 12:49:15.763562
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    q.put(2)
    q.put(3)
    assert q.get() == 2
    assert q.get() == 3
    assert q.qsize() == 0

# Generated at 2022-06-14 12:49:18.975591
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    q.put(1)
    assert q.get()==1

# Generated at 2022-06-14 12:49:28.067708
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():

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



# Generated at 2022-06-14 12:49:48.241917
# Unit test for method get of class Queue
def test_Queue_get():
    starttime = datetime.datetime.now()
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


# Generated at 2022-06-14 12:49:56.740735
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    print(q.maxsize)
    q.put("a")
    q.put("b")
    assert not q.empty()     # queue not full, why are putters waiting?
    q.get_nowait()
    q.get_nowait()
    assert q.empty()
    try:
        q.get_nowait()
    except QueueEmpty:
        print("Queue is empty!")
    q.put("c")
    q.put("d")
    try:
        q.put_nowait("e")
    except QueueFull:
        print("Queue is full!")
    # q.clear()
    print(q._queue)
    print(q.qsize())
    q.get_nowait()
    q.get_nowait()

# Generated at 2022-06-14 12:50:08.106950
# Unit test for method put of class Queue
def test_Queue_put():
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

    q=Queue(maxsize=2)
    ioloop.IOLoop.current().run_sync(main)




# Generated at 2022-06-14 12:50:11.064206
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    q.put(3)
    assert(q.get_nowait() == 3)
    q.put(3)
    assert(q.get_nowait() == 3)

# Generated at 2022-06-14 12:50:17.349933
# Unit test for method get of class Queue
def test_Queue_get():
    #test 1
    #description: This test checks the right behavior of get function in case of empty queue
    #AssertionError: expected QueueEmpty but got None
    q = Queue()
    assert q.get() == None

    #test 2
    #description: This test checks the right behavior of get function in case of not empty queue
    #AssertionError: expected 2 but got 3
    q = Queue()
    q.put(5)
    q.put(3)
    q.get()
    assert q.get() == 2

    #test 3
    #description: This test checks the right behavior of get function in case of full queue
    #AssertionError: expected QueueFull but got None
    q = Queue()
    q.put(5)
    q.put(3)
    assert q.get()

# Generated at 2022-06-14 12:50:28.748832
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import unittest
    import random
    class Test_Queue_get_nowait(unittest.TestCase):

        def setUp(self):
            self.queue = Queue(10)

        def test_in_empty_queue(self):
            x = random.randint(1,10)
            self.queue.__put_internal(x)
            self.assertEqual(self.queue.get_nowait(), x)

        def test_in_queue_with_one_element(self):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            self.queue.__put_internal(x)
            self.queue.__put_internal(y)
            self.assertEqual(self.queue.get_nowait(), x)


# Generated at 2022-06-14 12:50:35.802333
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado.gen import TimeoutError
    from tornado.ioloop import IOLoop
    q = Queue()
    async def put():
        await q.put(1)
    async def main():
        IOLoop.current().spawn_callback(put)
        await q.join()
    try:
        IOLoop.current().run_sync(main)
    except TimeoutError:
        print("Time out error")

# Generated at 2022-06-14 12:50:38.820912
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    print(q.empty())
    print(q.full())
    print(q.qsize())
    

# Generated at 2022-06-14 12:50:41.920956
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    q._queue.append(1)
    q._queue.append(2)
    assert q.get() == 1



# Generated at 2022-06-14 12:50:46.524196
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    with pytest.raises(QueueEmpty):
        Queue().get_nowait()
    q = Queue()
    q.put_nowait(1)
    assert q.get_nowait() == 1
    with pytest.raises(QueueEmpty):
        q.get_nowait()

# Generated at 2022-06-14 12:50:57.865082
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    q.put(1)
    q.put(2)
    assert q.get() == 1, "Error return value of method get"


# Generated at 2022-06-14 12:51:05.504627
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=5)
    print(q.qsize())
    q.put(6)
    print(q.qsize())
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.qsize())
    q.put_nowait(4)
    print(q.qsize())
    q.put_nowait(5)
    print(q.qsize())
    q.put_nowait(6)
    print("q full")
    print(q.qsize())
    q.put_nowait(6)
    print("q full")
    print(q.qsize())


# Generated at 2022-06-14 12:51:13.755201
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def main():
        # Start consumer without waiting (since it never finishes).
        io_loop = ioloop.IOLoop.current()
        io_loop.spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    io_loop = ioloop.IOLoop

# Generated at 2022-06-14 12:51:14.781320
# Unit test for method get of class Queue
def test_Queue_get():
    return True


# Generated at 2022-06-14 12:51:26.928282
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    from tornado.gen import sleep
    from tornado import gen
    def say_hello() -> None:
        print("hello")
    # IOLoop.current() returns a handle to the current IOLoop instance
    # run_sync() method launches the IOLoop.
    ioloop = IOLoop.current()
    q = Queue()
    @gen.coroutine
    def put_item() -> None:
        for item in range(5):
            yield q.put(item)
    @gen.coroutine
    def get_item() -> None:
        while True:
            item = yield q.get()
            print('Get %s' % item)
    # ioloop.spawn_callback will run the callback in the IOLoop thread.
    ioloop.spawn_callback

# Generated at 2022-06-14 12:51:28.853264
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put(1)
    q.get_nowait()


# Generated at 2022-06-14 12:51:33.731621
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    queue = Queue(maxsize=2)
    queue._queue = []
    queue._getters = []
    queue._putters = []
    queue._unfinished_tasks = 0
    queue._finished = Event()
    queue._finished.set()

    item = 1
    try:
        queue.put_nowait(item)
    except QueueFull:
        print("Invalid")

    print(queue._queue)
    print(queue._maxsize)
    print(queue._getters)
    print(queue._putters)
    print(queue._unfinished_tasks)
    print(queue._finished)



# Generated at 2022-06-14 12:51:37.604293
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=3)
    print(q.put_nowait('test1'))
    print(q.put_nowait('test2'))
    print(q.put_nowait('test2'))
    print(q.put_nowait('test3'))
    print(q._queue)



# Generated at 2022-06-14 12:51:48.671630
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            print('Put %s' % item)
            await q.put(item)
        
    async def main():
        # Start consumer without waiting (since it never finishes).
        consumer()
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    ioloop.IOLoop.current().run_sync(main)

# Generated at 2022-06-14 12:51:54.665648
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put(1)
    q.put(2)
    # Test if q contains 1
    Test.assertTrue(1 in q._queue, 'Expected 1 to be in the queue')
    # Test if q contains 2
    Test.assertTrue(2 in q._queue, 'Expected 2 to be in the queue')
test_Queue_put()

# Generated at 2022-06-14 12:52:11.970463
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    assert q is not None
    assert q.qsize() == 0
    assert q.empty() == True
    assert q.full() == False
    future = q.put(item=1, timeout=None)
    assert q.qsize() == 1
    assert q.empty() == False
    assert q.full() == False
    assert isinstance(future, Future) == True
    future = q.put(item=2, timeout=None)
    assert q.qsize() == 2
    assert q.empty() == False
    assert q.full() == True
    assert isinstance(future, Future) == True


# Generated at 2022-06-14 12:52:21.186634
# Unit test for method put of class Queue
def test_Queue_put():
    # Test case 1
    q = Queue(maxsize=2)

    @gen.coroutine
    def consumer():
        while True:
            # use q.get()
            item = yield q.get()
            try:
                print('Doing work on %s' % item)
                yield gen.sleep(0.01)
            finally:
                q.task_done()

    @gen.coroutine
    def producer():
        for item in range(5):
            # use q.put()
            yield q.put(item)
            print('Put %s' % item)

    @gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        yield producer()  # Wait for producer to put all tasks.

# Generated at 2022-06-14 12:52:26.325204
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    assert q._queue == collections.deque([1])

    q.put_nowait(2)
    assert q._queue == collections.deque([1, 2])

    try:
        q.put_nowait(3)
        assert False, "not full"
    except:
        assert True

    assert q._queue == collections.deque([1, 2])


# Generated at 2022-06-14 12:52:28.915071
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    assert q.empty()
    assert not q.full()
    assert q.get_nowait() == QueueEmpty

# Generated at 2022-06-14 12:52:30.996043
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queue = Queue()
    queue.put_nowait('a')

# Generated at 2022-06-14 12:52:39.026866
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    # The queue is empty, so
    # should not raise QueueFull
    q.put_nowait(1)
    q.put_nowait(2)
    # The queue has reached
    # its maxsize, so should
    # raise QueueFull
    raised = False
    try:
        q.put_nowait(3)
    except QueueFull:
        raised = True
    finally:
        assert raised == True
        print("Test passed!")

if __name__ == "__main__":
    test_Queue_put_nowait()


# Generated at 2022-06-14 12:52:48.303917
# Unit test for method put of class Queue
def test_Queue_put():
    print('===========Testing method put in class Queue===========')
    q = Queue(maxsize=2)
    print('Test success!')
    try:
        q.put(11)
        q.put(12)
        q.put(13)
    except QueueFull:
        print('Test success!')
    else:
        print('Test fail!')
    try:
        q.put(11, timeout=10)
        q.put(12, timeout=10)
        q.put(13, timeout=10)
    except QueueFull:
        print('Test success!')
    else:
        print('Test fail!')


# Generated at 2022-06-14 12:52:57.017188
# Unit test for method put of class Queue
def test_Queue_put():
    # Missing parameter 1.
    try:
        Q1 = Queue()
        Q1.put()
    except:
        pass
    else:
        assert False

    # Wrong parameter type.
    try:
        Q2 = Queue()
        Q2.put("a")
    except:
        pass
    else:
        assert False

    # Wrong parameter type.
    try:
        Q3 = Queue()
        Q3.put(1.4)
    except:
        pass
    else:
        assert False

    # Wrong parameter type.
    try:
        Q4 = Queue()
        Q4.put(True)
    except:
        pass
    else:
        assert False

    # Wrong parameter type.

# Generated at 2022-06-14 12:53:04.230757
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    fetcher = None
    try:
        fetcher = asyncio.get_event_loop().create_task(q.get())
        q.put_nowait(1)
        if (1 == (await fetcher)):
            print("test_Queue_get: success")
    except:
        print("test_Queue_get: error")

test_Queue_get()


# Generated at 2022-06-14 12:53:08.494802
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.ioloop import IOLoop
    q = Queue()
    q.put_nowait(1)
    assert q.get().result()==1


# Generated at 2022-06-14 12:53:24.520790
# Unit test for method get of class Queue
def test_Queue_get():
    import unittest
    from tornado import gen
    from tornado.ioloop import IOLoop

    from tornado.queues import Queue
    import asyncio
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    q = Queue(maxsize=2)

    def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                yield gen.sleep(0.01)
            finally:
                q.task_done()

    def producer():
        for item in range(5):
            yield q.put(item)
            print('Put %s' % item)

    def main():
        # Start consumer without waiting (since it never finishes).
        loop.spawn_callback(consumer)

# Generated at 2022-06-14 12:53:34.857661
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=0)
    q.put_nowait("wow")
    assert q._queue == collections.deque(["wow"])
    assert q.qsize() == 1
    q.put_nowait("hell")
    assert q._queue == collections.deque(["wow", "hell"])
    assert q.qsize() == 2
    try:
        q.put_nowait("")
    except QueueFull:
        print("Queue is full")
        assert q._queue == collections.deque(["wow", "hell"])
        assert q.qsize() == 2
    else:
        raise AssertionError("Expected QueueFull")


# Generated at 2022-06-14 12:53:45.480934
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    timeout=None
    #futures = future()
    from tornado import gen
    from tornado import ioloop
    from tornado import queues
    from tornado.concurrent import Future
    from tornado.locks import Event


    q = queues.Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()


    async def producer():
        for item in range(10):
            await q.put(item)
            print('Put %s' % item)



# Generated at 2022-06-14 12:53:49.597816
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait("1")
    q.put_nowait("2")
    q.put_nowait("3")
    assert q.get() == "1"
    assert q.get_nowait() == "2"
    assert q.get_nowait() == "3"


# Generated at 2022-06-14 12:53:58.245274
# Unit test for method put of class Queue
def test_Queue_put():
    # Simulate tornado
    from tornado.platform.asyncio import AsyncIOMainLoop
    AsyncIOMainLoop().install()
    import tornado.ioloop
    # Tests
    q = Queue(maxsize=2)
    def consumer():
        async for item in q:
            print(item)
    def producer(item: int) -> None:
        print(item)
        await q.put(item)
    # Coverage
    async def main():
        await q.put(1)
        await q.put(2)
        await q.put(3)
    # Run
    tornado.ioloop.IOLoop.current().run_sync(main)



# Generated at 2022-06-14 12:54:07.105036
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado.ioloop
    import tornado.gen

    io_loop = tornado.ioloop.IOLoop.current()
    q = tornado.queues.Queue(maxsize=2)
    future1 = q.get()
    future2 = q.get()
    q.put_nowait(1)
    q.put_nowait(2)
    future1r = io_loop.run_sync(lambda: future1)
    future2r = io_loop.run_sync(lambda: future2)
    assert future1r == 1
    assert future2r == 2
    # This assertion as simply wrong.
    #assert q.qsize() == 0

# Test for method put of class Queue

# Generated at 2022-06-14 12:54:15.157197
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():

    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    l = [0, 0, 0]
    q.put(0)
    q.put(1)
    q.put(2)
    async def consumer():
        async for item in q:
            try:
                l[item] = 1
                await gen.sleep(0.01)
            finally:
                q.task_done()

    io_loop = IOLoop.current()
    io_loop.run_sync(consumer)
    print(l)


# Generated at 2022-06-14 12:54:18.738716
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    fut = q.put(1)
    q.put(2)
    assert q.get_nowait() == 1
    # q.get_nowait() will raise exception if empty
    assert q.get_nowait() == 2


# Generated at 2022-06-14 12:54:25.899724
# Unit test for method put of class Queue
def test_Queue_put():
    # implements the test
    import unittest
    import asyncio
    from datetime import timedelta

    from tornado.testing import AsyncTestCase, gen_test

    class TestQueue(unittest.TestCase):
        def setUp(self) -> None:
            asyncio.set_event_loop(None)
            self.queue = Queue()

        def test_put_nowait_with_queue_empty_and_getters_not_wait(self):
            # arrange 
            # act
            self.queue.put_nowait(1)
            result = self.queue.qsize()
            # assert
            self.assertEqual(result, 1)


# Generated at 2022-06-14 12:54:36.586404
# Unit test for method get of class Queue

# Generated at 2022-06-14 12:55:02.627059
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    assert q.qsize() == 0
    assert q.empty() == True
    assert q.full() == False
    assert q.join() == None
    assert q.put(1) == None
    assert q.put(2) == None
    assert q.put(3) == None
    assert q.qsize() == 2
    assert q.empty() == False
    assert q.full() == True
    assert q.task_done() == None
    assert q.join() == None

# Generated at 2022-06-14 12:55:08.249778
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q._queue = [1, 2, 3]
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    assert q._queue == []
    with pytest.raises(QueueEmpty):
        q.get_nowait()


# Generated at 2022-06-14 12:55:19.966425
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop
    from tornado import gen
    from tornado.concurrent import Future
    q = Queue()
    def put_coro():
        await q.put(1)
    IOLoop.current().run_sync(put_coro)
    f = q.put(2)
    IOLoop.current().run_sync(f)
    f = Future()
    f.add_done_callback(lambda _: IOLoop.current().stop())
    IOLoop.current().spawn_callback(lambda : q.put(3, timeout = 1))
    IOLoop.current().start()




# Generated at 2022-06-14 12:55:25.125658
# Unit test for method put of class Queue
def test_Queue_put():
    io_loop = ioloop.IOLoop.current()
    q = Queue(2)
    # Testing the first case where, when there are no getters and the queue is not full
    future = q.put(1)
    io_loop.run_sync(future)
    assert future.exception() is None, 'Test1 Failed'

    # Testing the second case where, when there are no getters but the queue is full and thus the put_request is added to _putters
    future = q.put(2)
    io_loop.run_sync(future)
    assert future.exception() is None, 'Test2 Failed'

    future = q.put(3)
    io_loop.run_sync(future)

# Generated at 2022-06-14 12:55:27.344912
# Unit test for method get of class Queue
def test_Queue_get():
    assert hasattr(Queue, 'get')
    q = Queue(maxsize=2)
    q.put(1)
    q.put(2)
    assert q.qsize() == 2
    assert q.get() == 1

# Generated at 2022-06-14 12:55:33.112068
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    q.put_nowait(4)
    q.put_nowait(5)
    q.put_nowait(6)

    print(q.qsize())
    print(q)


# Generated at 2022-06-14 12:55:42.929365
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # test_Queue_get_nowait begin

    q = Queue(maxsize=0)

    @gen.coroutine
    def consumer():
        item = None
        while True:
            try:
                item = yield q.get_nowait()
                print('Doing work on %s' % item)
                yield gen.sleep(0.01)
            except QueueEmpty:
                print('Queue is empty')
            finally:
                if item:
                    q.task_done()
                yield gen.sleep(0.01)

    @gen.coroutine
    def producer():
        for item in range(5):
            print('Put %s' % item)
            yield q.put(item)

    @gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        io_

# Generated at 2022-06-14 12:55:49.940651
# Unit test for method put of class Queue
def test_Queue_put():
    def run_async(cor):
        return next(cor, None)
    q = Queue(maxsize=500)
    my_future = q.put(item = "test_item", timeout = 5)
    assert my_future.result() == None
    assert run_async(q.get()) == "test_item"
test_Queue_put()
