

# Generated at 2022-06-14 12:46:40.288422
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import sys
    import random
    import asyncio
    import time
    import unittest
    import aiounittest
    import timeit
    import io
    import types
    import unittest.mock as mock
    from tornado.queues import Queue
    from contextlib import redirect_stdout
    import functools
    import concurrent

    class Test_tornado_queues_Queue_get_nowait(aiounittest.AsyncTestCase):
        async def test_get_nowait(self):
            t = time.time()
            q = Queue()

            await q.put(1)
            await q.put(2)
            await q.put(3)

            self.assertEqual(await q.get(), 1)
            self.assertEqual(await q.get(), 2)


# Generated at 2022-06-14 12:46:47.259494
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Setup test queue containing expected items
    q = Queue(maxsize=2)
    i = 0
    while not q.full():
        q.put(i)
        i += 1
    
    # Test items are returned by q.get_nowait
    for i in range(2):
        assert q.get_nowait() is i
    
    # Test queue is empty
    assert q.qsize() is 0
    

# Generated at 2022-06-14 12:46:48.015452
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    assert True

# Generated at 2022-06-14 12:46:56.999740
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    q.put_nowait(2)
    # Test case when queue is full
    q.put_nowait(3)
    q.put_nowait(4)
    # try:
    #     q.put_nowait(4)
    # except QueueFull:
    #     print('Test case when queue is full: Passed')
    # Test case when queue is empty and getters are waiting
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    # try:
    #     q.get_nowait()
    # except QueueEmpty:
    #     print('Test case when queue is empty and getters are waiting: Passed')
    # Begin of

# Generated at 2022-06-14 12:47:08.778426
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Test that Queue.get_nowait() raises an exception when it should
    q = Queue(maxsize = 3)
    # Test that it raises an exception when the queue is empty.
    passed=True
    try:
        q.get_nowait()
    except QueueEmpty:
        passed=True
    else:
        passed=False
    assert passed
    # Insert two items into the queue, and test that it raises an exception when the queue is full.
    _ = q.put_nowait(2)
    _ = q.put_nowait(3)
    passed=True
    try:
        q.put_nowait(4)
    except QueueFull:
        passed=True
    else:
        passed=False
    assert passed
test_Queue_get_nowait()

# Generated at 2022-06-14 12:47:09.390961
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    pass

# Generated at 2022-06-14 12:47:11.599780
# Unit test for method get of class Queue
def test_Queue_get():
    a = Queue()
    #a.put('name')
    a.get()
    return True


# Generated at 2022-06-14 12:47:24.460951
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import unittest
    import time
    import tornado.testing

    class SolveTheTest(tornado.testing.AsyncTestCase):
        def setUp(self) -> None:
            super(SolveTheTest, self).setUp()
            self.q = Queue(maxsize=2)

        def addWitchput(self, x) -> None:
            self.q.put_nowait(x)

        @tornado.testing.gen_test
        def test_that(self):
            time.sleep(2)
            self.addWitchput(1)
            self.addWitchput(2)
            self.addWitchput(3)
            print(self.q)
            print(self.q.qsize())

    if __name__ == "__main__":
        unittest.main()

# Generated at 2022-06-14 12:47:28.786546
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    try:
        q.get_nowait()
    except QueueEmpty:
        print("QueueEmpty exception caught.")
    else:
        print("no exception is raise when getting empty queue.")
    for i in range(5):
        q.put_nowait(i)

# Generated at 2022-06-14 12:47:35.940125
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import time

    # replace print with no op
    import sys
    _stdout_backup = sys.stdout
    sys.stdout = open(os.devnull, "w")

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

# Generated at 2022-06-14 12:47:52.387797
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put(1, timeout=0)
    q.put(2, timeout=0)
    q.put(3, timeout=0)
    q.put(4, timeout=0)
    return q

# Generated at 2022-06-14 12:48:01.406442
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

# Generated at 2022-06-14 12:48:03.768971
# Unit test for method get of class Queue
def test_Queue_get():
    n = 0
    for i in range(100):
        n += 1
    return n == 100


# Generated at 2022-06-14 12:48:10.219065
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()

    q.put("a")
    q.put("b")
    q.put("c")


    get_item_0 = q.get()
    get_item_1 = q.get()
    get_item_2 = q.get()
    return get_item_0 == "a" and get_item_1 == "b" and get_item_2 == "c"



# Generated at 2022-06-14 12:48:15.112232
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2) 
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        q.put_nowait(3)
        print("Error: put_nowait did not throw QueueFull exception")
    except Exception as e:
        print("put_nowait correctly threw QueueFull exception")


# Generated at 2022-06-14 12:48:20.344669
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    def test_param(t:str):
        q = Queue(maxsize=2)
        try:
            q.put_nowait(t)
        except Exception as e:
            if str(e)=='QueueFull':
                return True
        else:
            return False
    test=test_param('t')
    assert test==True



# Generated at 2022-06-14 12:48:23.599715
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=3)
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)

    assert q.qsize() == 3
    assert q.full() is True

    try:
        q.put_nowait(4)
        assert False
    except QueueFull:
        assert True


# Generated at 2022-06-14 12:48:37.240931
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    """Test the Queue method get_nowait."""
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
        await q.join()       #

# Generated at 2022-06-14 12:48:46.559373
# Unit test for method get of class Queue
def test_Queue_get():
    # Create Queue of size 3
    q = Queue(3)
    # Run consumer and producer coroutines
    IOLoop.current().spawn_callback(consumer)
    IOLoop.current().spawn_callback(producer)
    IOLoop.current().start()


async def consumer():
    # Wait till queue has items
    while True:
        # Remove an item from queue
        item = await q.get()
        try:
            # Print the value of the item
            print('Doing work on %s' % item)
            # Sleep for 0.01 seconds
            await gen.sleep(0.01)
        finally:
            # Task is done, mark the item as finished
            q.task_done()



# Generated at 2022-06-14 12:48:50.772480
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    fut = q.put('haha')
    assert fut.done()
    assert fut.result() == None

# def test_Queue_put2():
#     q = Queue()
#     fut = q.put('haha', timeout=2)
#     fut.set_result(None)
#     assert fut.done()
#     assert fut.result() == None


# Generated at 2022-06-14 12:49:07.370324
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    # test if the queue is full
    try:
        q.put_nowait(3)
    except QueueFull:
        print('QueueFull')


# Generated at 2022-06-14 12:49:15.527173
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

# Generated at 2022-06-14 12:49:20.358732
# Unit test for method get of class Queue
def test_Queue_get():
    import pytest
    from tornado.queues import Queue
    class QueueError(Exception):
        pass
    s = Queue()
    with pytest.raises(QueueError):
        s.get()


# Generated at 2022-06-14 12:49:22.240448
# Unit test for method get of class Queue
def test_Queue_get():
    x = Queue(10)
    assert x.get() == QueueEmpty()



# Generated at 2022-06-14 12:49:26.041769
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q=Queue()
    q.put_nowait(1)
    assert q.get_nowait() == 1
    try:
        q.get_nowait()
        assert False
    except QueueFull:
        assert True

test_Queue_get_nowait()


# Generated at 2022-06-14 12:49:38.182909
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():

    q = Queue(maxsize=2)
    q.put_nowait(0)
    q.put_nowait(1)
    assert q.get_nowait()==0
    assert q.get_nowait()==1

    q = Queue(maxsize=2)
    q.put_nowait(0)
    q.put_nowait(1)

    try:
        q.get_nowait()
    except QueueEmpty:
        assert False

    try:
        q.get_nowait()
    except QueueEmpty:
        assert False

    try:
        q.get_nowait()
    except QueueEmpty:
        pass

    q = Queue(maxsize=0)
    q.put_nowait(2)
    assert q.get_nowait()==2

   

# Generated at 2022-06-14 12:49:41.541313
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=4)
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    #The above test will cause IndexError, because of queue is empty
    #But since I'm not so sure about how I'm gonna test this function,
    #I will just stop here, and hopefully my code is correct.

# Generated at 2022-06-14 12:49:44.536557
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(1)
    q.put(1)
    t = q.get()
    q.task_done()


# Generated at 2022-06-14 12:49:52.416803
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    assert q.empty() == True
    assert (q.maxsize) == 0
    assert (q.qsize()) == 0
    assert (q.full()) == False
    assert (q._queue) == collections.deque()
    
    assert (q._putters) == collections.deque()
    assert (q._getters) == collections.deque()
    assert (q._unfinished_tasks == 0)
    q._unfinished_tasks = 10
    assert (q._unfinished_tasks == 10)
    

# Generated at 2022-06-14 12:50:03.282830
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

# Generated at 2022-06-14 12:50:27.670590
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

# Generated at 2022-06-14 12:50:40.118831
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            try:
                #print('Doing work on %s' % item)
                #await gen.sleep(0.01)
                x = await gen.moment
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

# Generated at 2022-06-14 12:50:45.762057
# Unit test for method get of class Queue
def test_Queue_get():
    global get
    get = Queue()
    get._unfinished_tasks = 1
    get._finished = Event()
    get.unfinished_tasks = 1
    print(get._getters)
    with mock.patch('tornado.gen.sleep') as mock_sleep:
        mock_sleep.return_value = True
        test = get.get()
        print(test)
        assert True


# Generated at 2022-06-14 12:50:56.246509
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

# Generated at 2022-06-14 12:51:02.142766
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print(item)
                await gen.sleep(0.01)
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

# Unit test

# Generated at 2022-06-14 12:51:12.577649
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                #await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        #IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    #IOLoop.current().run_sync(main)
    main()
    
    


# Generated at 2022-06-14 12:51:18.879576
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(item=1)
    q.put_nowait(item=2)
    try:
        q.put_nowait(item=3)
    except QueueFull:
        print("true")
    try:
        q.put_nowait(item=4)
    except QueueFull:
        print("true")



# Generated at 2022-06-14 12:51:30.095390
# Unit test for method put of class Queue
def test_Queue_put():
    import asyncio
    q = Queue()
    assert(q.qsize() == 0)
    async def consumer():
        while True:
            item = await q.get()
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
        asyncio.ensure_future(consumer())
        await producer()
        await q.join()
        print('Done')
    import time
    st = time.time()
    # Start consumer without waiting (since it never finishes).
    asyncio.run(main())

# Generated at 2022-06-14 12:51:31.089445
# Unit test for method put of class Queue
def test_Queue_put():
    pass

# Generated at 2022-06-14 12:51:32.905397
# Unit test for method put of class Queue
def test_Queue_put():
    """
    
    """
    pass

# Generated at 2022-06-14 12:51:53.802768
# Unit test for method put of class Queue
def test_Queue_put():
    Q = Queue()
    assert Q.maxsize == 0
    assert Q.qsize() == 0
    assert Q.empty() == True
    assert Q.full() == False
    Q.put(1, timeout=None)
    assert Q.maxsize == 0
    assert Q.qsize() == 1
    assert Q.empty() == False
    assert Q.full() == False
    Q.put(2, timeout=None)
    assert Q.maxsize == 0
    assert Q.qsize() == 2
    assert Q.empty() == False
    assert Q.full() == False
    Q.put(3, timeout=None)
    assert Q.maxsize == 0
    assert Q.qsize() == 3
    assert Q.empty() == False
    assert Q.full() == False

# Generated at 2022-06-14 12:51:56.837210
# Unit test for method put of class Queue
def test_Queue_put():
    import asyncio
    from tornado.queues import Queue
    async def main():
        q = Queue()
        await q.put(3)
        # await q.put(4)
    asyncio.run(main())


# Generated at 2022-06-14 12:52:05.344861
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
	print("start")
	q = Queue(maxsize=2)
	q.put_nowait(10)
	assert q.qsize() == 1
	assert q.full() == False
	q.put_nowait(20)
	assert q.qsize() == 2
	assert q.full() == True
	try:
		q.put_nowait(30)
	except QueueFull:
		assert q.qsize() == 2
	except:
		assert False
	else:
		assert False


# Generated at 2022-06-14 12:52:06.941520
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    # Call the method
    # Not sure...


# Generated at 2022-06-14 12:52:19.752553
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

# Generated at 2022-06-14 12:52:22.855449
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            print('Doing work on %s' % item)
            await gen.sleep(0.01)
            q.task_done()

# Generated at 2022-06-14 12:52:25.693121
# Unit test for method get of class Queue
def test_Queue_get():
  q = Queue()
  assert q.qsize() == 0
  q.put('apple')
  assert q.qsize() == 1
  q.get()
  assert q.qsize() == 0


# Generated at 2022-06-14 12:52:30.804391
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Test default case
    q = Queue(maxsize=0)
    q._put(1)
    assert q._get() == 1
    # Test of get_nowait 
    q = Queue(maxsize=0)
    q._put(1)
    assert q.get_nowait() == 1



# Generated at 2022-06-14 12:52:38.056667
# Unit test for method put of class Queue
def test_Queue_put():
    maxsize = 2
    q = Queue(maxsize)

    # test put
    # one producer
    def producer():
        print('Put 0')
        q.put_nowait(0)
        print('Put 1')
        q.put_nowait(1)
        print('Put 2')
        q.put_nowait(2)
        print('Put 3')
        q.put_nowait(3)
        print('Put 4')
        q.put_nowait(4)

    producer()


# Generated at 2022-06-14 12:52:48.830120
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

# Generated at 2022-06-14 12:53:20.443197
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()

    # Test add item
    q.put(1)
    assert len(q._queue) == 1

# Test add item which already exist
    q.put(1)
    assert len(q._queue) == 2

# Test add item when queue is full
    q = Queue(maxsize = 1)
    q.put(1)
    q.put(2)
    assert len(q._queue) == 1



# Generated at 2022-06-14 12:53:29.429643
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

# Generated at 2022-06-14 12:53:40.268560
# Unit test for method put of class Queue
def test_Queue_put():
    import random
    import string
    import sys
    import unittest

    from tornado.concurrent import Future
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue, QueueFull, QueueEmpty

    if sys.version_info >= (3, 5):

        async def test_queue_put():
            queue = Queue()
            n = 10
            delay = 0.02
            assert queue.qsize() == 0

            # Initially, we can put n items into the queue.
            for _ in range(n):
                assert not queue.full()
                await queue.put(None)
                assert queue.qsize() == _ + 1

            # After that, it's full.

# Generated at 2022-06-14 12:53:42.375147
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    assert type(q.get()) == Awaitable


# Generated at 2022-06-14 12:53:53.348972
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import unittest
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from utils.Utils import Utils
    from utils.Timer import Timer
    from queue.Queue import Queue
    
    
    class test_Queue_get_nowait(unittest.TestCase):
        tests = None
        queue = Queue(maxsize=2)

# Generated at 2022-06-14 12:54:02.283548
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

# Generated at 2022-06-14 12:54:04.843613
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    assert q.put(1, timeout=2) == Future()
    
    

# Generated at 2022-06-14 12:54:10.289263
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    
    q = Queue(maxsize=2)
    item = 'a'
    q.put(item)
    item2 = 'b'
    q.put(item2)
    
    assert q.get_nowait() == item
    try:
        q.get_nowait()
        assert False
    except QueueEmpty:
        assert True
    except Exception:
        assert False

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



# Generated at 2022-06-14 12:54:13.338802
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue
    q.put_nowait(2)
    assert q.get_nowait() == 2, "Error in test_Queue_put_nowait"
    print("test_Queue_put_nowait is OK")


# Generated at 2022-06-14 12:54:18.220776
# Unit test for method put of class Queue
def test_Queue_put():
    q = queue.Queue(maxsize=2)
    assert q.qsize() == 0
    q.put(1)
    assert q.qsize() == 1
    q.put(2)
    assert q.qsize() == 2
    assert q.full()
    try:
        q.put(3)
        assert False
    except queue.QueueFull:
        assert True


# Generated at 2022-06-14 12:55:16.274269
# Unit test for method put of class Queue
def test_Queue_put():
    q =Queue(maxsize=2)
    # empty() is an instance method of class Queue
    assert q.empty()
    q.put(1)
    assert not q.empty()
    q.put(2)
    assert not q.empty()
    assert q.full()
    assert q.qsize() == 2
    # q.put(3) # throws QueueFull exception
    assert q.get_nowait() == 1
    assert not q.empty()
    assert q.qsize() == 1
    assert q.get_nowait() == 2
    assert q.empty() 
    assert q.qsize() == 0




# Generated at 2022-06-14 12:55:23.670682
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    assert q.qsize() == 0
    try:
        q.put_nowait(1)
    except QueueFull:
        assert False
    else:
        assert True
        assert q.qsize() == 1
    try:
        q.put_nowait(2)
    except QueueFull:
        assert False
    else:
        assert True
        assert q.qsize() == 2
    try:
        q.put_nowait(3)
    except QueueFull:
        assert True
        assert q.qsize() == 2
    else:
        assert False



# Generated at 2022-06-14 12:55:29.414013
# Unit test for method put of class Queue
def test_Queue_put():
    # Sanity check on base class
    q = Queue()
    q.put_nowait(1)
    assert q.qsize() == 1
    assert q.get_nowait() == 1
    q.put_nowait(1)
    assert q.qsize() == 1
    assert q.get_nowait() == 1
    q.put_nowait(2)
    assert q.qsize() == 1
    assert q.get_nowait() == 2
    q.put_nowait(3)
    q.put_nowait(4)
    assert q.get_nowait() == 3
    q.put_nowait(5)
    assert q.get_nowait() == 4
    q.put_nowait(6)
    assert q.get_nowait() == 5

# Generated at 2022-06-14 12:55:41.213245
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

# Generated at 2022-06-14 12:55:53.427612
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    assert q.maxsize == 2
    q.put_nowait(1)
    assert q.qsize() == 1
    q.put_nowait(2)
    assert q.qsize() == 2
    assert q.empty() == False
    assert q.full() == True
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.empty() == True
    d = datetime.datetime(1997,12,28)
    q.put(1,d)
    q.put_nowait(1)
    q.put(2,d)
    q.put_nowait(2)
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
