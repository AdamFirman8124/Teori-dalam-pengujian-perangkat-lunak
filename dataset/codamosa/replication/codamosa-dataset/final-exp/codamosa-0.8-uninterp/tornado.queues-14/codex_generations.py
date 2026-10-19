

# Generated at 2022-06-14 12:46:37.045251
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=3)
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        q.get_nowait()
        assert "Queue should be empty"
    except QueueEmpty:
        pass
    try:
        q.get_nowait()
        assert "Queue should be empty"
    except QueueEmpty:
        pass
    try:
        q.get_nowait()
        assert "Queue should be empty"
    except QueueEmpty:
        pass


# Generated at 2022-06-14 12:46:45.922854
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q1 = Queue(maxsize=2)
    assert q1.qsize() == 0
    q1.put_nowait(1)
    assert q1.qsize() == 1
    q1.put_nowait(2)
    assert q1.qsize() == 2
    try:
        q1.put_nowait(3)
        assert False
    except QueueFull:
        assert True
    assert q1.qsize() == 2
    assert q1.full() == True


# Generated at 2022-06-14 12:46:52.036205
# Unit test for method put of class Queue
def test_Queue_put():
    # Initialize a new Queue with maxsize=2.
    queue = Queue(maxsize=2)
    assert queue.maxsize == 2, "Wrong maxsize of the queue"
    assert queue.empty(), "When a new Queue is created, it should be empty"
    assert not queue.full(), "Queue shouldn't be full"

    # Put the first item, it shouldn't be blocking.
    queue.put_nowait(1)
    assert not queue.empty(), "Queue shouldn't be empty"
    assert not queue.full(), "Queue shouldn't be full"

    # Put a second item.
    queue.put_nowait(2)
    assert not queue.empty(), "Queue shouldn't be empty"
    assert queue.full(), "Queue should be full"

    # Putting the third item should block because the Queue is full.

# Generated at 2022-06-14 12:46:54.986660
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=5)
    for i in range(5):
        q.put_nowait(i)
    print(q.qsize())
#test_Queue_put_nowait()


# Generated at 2022-06-14 12:47:02.215298
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    #assert q.get_nowait() == 1
    #assert q.get_nowait() == 2
    q.put_nowait(3)
    q.put_nowait(4)
    #print(q)



# Generated at 2022-06-14 12:47:11.362560
# Unit test for method put of class Queue
def test_Queue_put():

    q = Queue(maxsize=2)

    future = q.put(0)
    future = q.put(0)
    assert not future.done()

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


# Generated at 2022-06-14 12:47:24.252322
# Unit test for method put of class Queue
def test_Queue_put():
    async def main():

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

        q = Queue(maxsize=2)

        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    ioloop.IOLoop.current().run_sync(main)

# Generated at 2022-06-14 12:47:28.211201
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        q.put_nowait(3)
        assert False
    except QueueFull:
        pass
    assert len(q._queue) == 2


# Generated at 2022-06-14 12:47:38.022234
# Unit test for method get_nowait of class Queue

# Generated at 2022-06-14 12:47:43.012592
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    fut1 = Future()
    fut2 = Future() # some future object
    queue = Queue(maxsize=2)
    # put_nowait will call the function __put_internal
    queue.put_nowait(fut1) # put the future object into queue
    assert len(queue._queue) == 1
    assert queue._queue.popleft() == fut1 # remember, a queue is deque
    queue.put_nowait(fut2)
    assert len(queue._queue) == 1
    assert queue._queue.popleft() == fut2


# Generated at 2022-06-14 12:47:53.773762
# Unit test for method put of class Queue
def test_Queue_put():
    pass

# Generated at 2022-06-14 12:47:57.657935
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import pytest
    q = Queue(maxsize=2)

    q.put_nowait(1)
    q.put_nowait(2)
    with pytest.raises(QueueFull):
        q.put_nowait(3)


# Generated at 2022-06-14 12:48:01.462327
# Unit test for method get of class Queue
def test_Queue_get():
    maxsize = 0
    q = Queue(maxsize=maxsize)
    timeout = None
    res = q.get(timeout=timeout)
    assert res is not None
    pass


# Generated at 2022-06-14 12:48:04.779016
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    """Unit test for method get_nowait of class Queue"""
    q = Queue(maxsize=5)
    assert q.get_nowait() == 0



# Generated at 2022-06-14 12:48:09.453639
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    # test put task
    q.put(1)
    q.put(2)
    q.put(3)
    assert q.qsize() == 3
    # test put multiple items
    q.put_nowait([4,5,6])
    q.put_nowait((7,8,9))
    assert q.qsize() == 6
    # test put too many items
    q.put_nowait(10)
    assert q.qsize() == 7

# Generated at 2022-06-14 12:48:14.693087
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.testing import AsyncTestCase, gen_test

    a = Queue()
    a.put_nowait('a')
    async def test_get():
        a = Queue()
        a.put_nowait('a')
        res = await a.get()
        assert res == 'a'
        res = await a.get()
        assert res == 'a'


# Generated at 2022-06-14 12:48:24.421364
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    q.put(1)
    q.put(2)
    assert q.get_nowait() == 1
    assert q.qsize() == 1
    q.put(3)
    q.put_nowait(4)
    assert q.get_nowait() == 2
    assert q.qsize() == 2
    q.put_nowait(5)
    q.put(6)
    assert q.get_nowait() == 3
    assert q.get_nowait() == 4
    assert q.get_nowait() == 5
    assert q.qsize() == 1
    q.put_nowait(7)
    assert q.qsize() == 2
    assert q.full() == True
    assert q.get_nowait() == 6
   

# Generated at 2022-06-14 12:48:26.379594
# Unit test for method get of class Queue
def test_Queue_get():
    q=Queue()
    q.get()

# Generated at 2022-06-14 12:48:36.962968
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    with pytest.raises(QueueFull):
        q.put_nowait(3)
    q.put_nowait(1)
    q.put_nowait(2)
    with pytest.raises(QueueFull):
        q.put_nowait(3)
    q.get_nowait()
    q.put_nowait(3)
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    with pytest.raises(QueueEmpty):
        q.get_nowait()

# Generated at 2022-06-14 12:48:41.894557
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    assert isinstance(q.get(), Future)

    with pytest.raises(QueueEmpty):
        q.get_nowait()
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty() is True
    assert q.full() is False



# Generated at 2022-06-14 12:48:55.694175
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put(1)
    q.put_nowait(2)
    q.get_nowait()
    q.get()
    q.task_done()
    return


# Generated at 2022-06-14 12:49:07.745441
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado.gen import Return, coroutine
    from tornado.ioloop import IOLoop
    import time
    import uuid
    from queue import Queue
    q = Queue(2)
    async def print_q():
        try:
            while True:
                x = await q.get()
                print(x)
        except gen.Return:
            print('done')
            raise Return("m_done")
    @coroutine
    def put_q():
        i = 0
        while i < 100:
            async def put_everyth():
                await q.put(uuid.uuid4())
            IOLoop.current().spawn_callback(put_everyth)
            i = i + 1
        IOLoop.current().spawn_callback(print_q)
    put_q()

# Generated at 2022-06-14 12:49:12.885795
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    a = Queue()
    assert a.empty() == True
    a.put("2")
    a.put("1")
    assert a.qsize() == 2 #qsize return the size of the queue
    assert a.get_nowait() == "2"
    assert a.empty() == False
    assert a.get_nowait() == "1"
    assert a.empty() == True

test_Queue_get_nowait()


# Generated at 2022-06-14 12:49:19.231332
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put(1)
    assert q.qsize() == 1
    assert q.empty() == False
    assert q.full() == False
    assert q._putters == []
    assert q._getters == []
    assert q._unfinished_tasks == 1
    assert q._finished._is_set == False



# Generated at 2022-06-14 12:49:28.243402
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

# Generated at 2022-06-14 12:49:36.841417
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import time
    import random
    import threading
    from tornado.queues import Queue
    x = Queue()
    def func():
        time.sleep(random.randint(1,5))
        print('pop', x.get_nowait())
        print('poped!')
    while True:
        i = input()
        if i == 'exit':
            print('exit')
            break
        x.put(i)
        threading.Thread(target=func).start()
        print('putted!')


# Generated at 2022-06-14 12:49:47.572909
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # If no free slot is immediately available, raise `QueueFull`
    q = Queue(maxsize=1)
    q.put_nowait(1)
    try:
        q.put_nowait(2)
    except QueueFull:
        pass
    # If there are waiting `Future`s of getters, add the item to the queue and set the result of `Future`
    q = Queue(maxsize=1)
    q.put_nowait(1)
    fut = Future()
    q._getters.append(fut)
    q.put_nowait(2)
    assert fut.result() == 1
    assert q.get_nowait() == 2
    # If the queue is full, raise `QueueFull`
    q = Queue(maxsize=1)
    q.put_nowait

# Generated at 2022-06-14 12:49:56.298860
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    pass
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue
    # object of class Queue -> object of class Queue


# Generated at 2022-06-14 12:50:07.685673
# Unit test for method put of class Queue
def test_Queue_put():
    import tornado.ioloop

    # TESTCASE 1
    from tornado.queues import Queue
    q = Queue()
    timeout = 0
    future = q.put(1, timeout=timeout)
    assert q.qsize() == 1
    assert q.get_nowait() == 1
    assert q.qsize() == 0

    # TESTCASE 2
    import datetime
    from tornado.queues import Queue
    q = Queue()
    timeout = datetime.timedelta(seconds=1)
    future = q.put(2, timeout=timeout)
    assert q.qsize() == 1
    assert q.get_nowait() == 2
    assert q.qsize() == 0

    # TESTCASE 3
    import datetime
    from tornado.queues import Queue
    q

# Generated at 2022-06-14 12:50:15.614201
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    assert q.empty() == True, "expect True to be True"
    assert q.full() == False, "expect False to be False"

    q.put_nowait(0)
    assert q.empty() == False, "expect False to be False"
    assert q.get_nowait() == 0, "expect 0 to be 0"
    assert q.full() == False, "expect False to be False"

    try:
        assert q.get_nowait() == None, "expect None to be None"
    except QueueEmpty as e:
        print("get_nowait QueueEmpty: {}".format(e))



# Generated at 2022-06-14 12:50:42.893678
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
	# Test 1: Unit test for method put_nowait() when queue is not full
	q=Queue()
	q.put_nowait(1)
	if 1==len(q._queue):
		return True
	else:
		return False
	  
	# Test 2: Unit test for method put_nowait() when queue is full
	# q=Queue(1)
	# q.put_nowait(1)
	# if QueueFull==q.put_nowait(1):
	# 	return True
	# else:
	# 	return False


# Generated at 2022-06-14 12:50:51.449766
# Unit test for method get of class Queue
def test_Queue_get():
   q = Queue(maxsize=2)
   a = Future()
   b = Future()
   c = Future()
   q._getters.append(a)
   q._getters.append(b)
   q._getters.append(c)
   assert q.get_nowait() is a
   assert q.get_nowait() is b
   q._queue = [1, 2, 3]
   assert q.get_nowait() is 3
   with pytest.raises(QueueEmpty):
       q.get_nowait()


# Generated at 2022-06-14 12:50:53.445866
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    f = open('test_Queue_get_nowait.txt', 'w')

# Generated at 2022-06-14 12:50:55.242854
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    r = q.get()
    assert r



# Generated at 2022-06-14 12:51:03.988900
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
test_

# Generated at 2022-06-14 12:51:11.533555
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Test Queue.put_nowait()
    # Case 1:  queue is empty.
    # Case 2:  queue is not empty.
    # Case 3:  queue is full.
    q = Queue(2)
    # Case 1
    assert q.qsize() == 0
    q.put_nowait(3)
    assert q.qsize() == 1
    # Case 2
    q.put_nowait("c")
    assert q.qsize() == 2
    # Case 3
    try:
        q.put_nowait("d")
        assert False
    except (QueueFull):
        pass
    assert q.qsize() == 2



# Generated at 2022-06-14 12:51:17.973819
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    @gen.coroutine
    def main():
        q = Queue(maxsize=2)
        q.put_nowait(1)
        q.put_nowait(2)

        try:
            q.put_nowait(3)
        except QueueFull:
            print('Queue is full')

        yield gen.sleep(1)

    ioloop.IOLoop.current().run_sync(main)

# Generated at 2022-06-14 12:51:29.474526
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.ioloop import IOLoop
    import time
    import datetime

    q = Queue(maxsize=2)
    # PUT 5 items into the queue
    for i in range(5):
        q.put(i)
    print("PUT:", q)
    # GET 2 items from the queue
    for i in range(2):
        q.get_nowait()
    print("GET 2 ITEMS:", q)
    q.put(9)
    print("PUT 9", q)
    q.get_nowait()
    print("GET 9", q)
    q.task_done()
    # PUT 100 items into the queue
    for i in range(100):
        # Put the item in the queue
        q.put(i)
        print('PUT', i)
        # Returns true if

# Generated at 2022-06-14 12:51:36.498694
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import ioloop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.empty()
    assert q.full()
    q.put_nowait(3)
    q.put_nowait(4)
    assert q.qsize() == 2
    assert not q.empty()
    assert q.full()

# Generated at 2022-06-14 12:51:45.162692
# Unit test for method get of class Queue
def test_Queue_get():
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
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    ioloop.IOLoop.current().run_sync(main)

# Unit

# Generated at 2022-06-14 12:52:34.236593
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

# Generated at 2022-06-14 12:52:45.063609
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

# Generated at 2022-06-14 12:52:49.959802
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    print("Testing put_nowait")
    q = Queue(maxsize=2)
    try:
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
    except QueueFull as e:
        print("QueueFull ->", e)


test_Queue_put_nowait()

# Generated at 2022-06-14 12:52:57.351662
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

# Generated at 2022-06-14 12:53:05.627365
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=1)

    # put_nowait is called with full queue
    q.put_nowait('A')
    try:
        q.put_nowait('B')
        assert False
    except QueueFull:
        pass

    # put_nowait is called with empty queue
    q.get_nowait()
    q.put_nowait('C')

    # put_nowait is called with non-empty queue
    q.get_nowait()
    q.put_nowait('D')



# Generated at 2022-06-14 12:53:16.639777
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # A test for Queue.get_nowait() method
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
        await producer()  # Wait for producer to put all tasks.
        await q.join() 

# Generated at 2022-06-14 12:53:25.344118
# Unit test for method put of class Queue
def test_Queue_put():
    import asyncio
    import random
    import sys
    import time
    import tornado.queues
    ''' Test for put method of class Queue
    '''
    maxsize = 7
    async def consumer(id, q):
        '''
            Set up a consumer coroutine 
        '''
        while True:
            val = await q.get()
            try:
                if val is None:
                    break
                print('consumer {}: <{}>'.format(id, val))
                await asyncio.sleep(random.random())
            finally:
                q.task_done()
    async def producer(id, q):
        '''
            Set up a producer coroutine 
        '''
        nums = range(5 * sys.getsizeof(id))
        num = 0

# Generated at 2022-06-14 12:53:34.471452
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    assert str(q) == "<Queue maxsize=0>"
    q.put_nowait(1)
    assert str(q) == "<Queue maxsize=0 queue=[1]>"
    q.put_nowait(2)
    assert str(q) == "<Queue maxsize=0 queue=[1, 2]>"
    assert q.get_nowait() == 1
    assert str(q) == "<Queue maxsize=0 queue=[2]>"
    assert q.get_nowait() == 2
    assert str(q) == "<Queue maxsize=0>"

# Generated at 2022-06-14 12:53:45.183925
# Unit test for method put of class Queue
def test_Queue_put():
    def create_queue():
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

    create_queue()

# Generated at 2022-06-14 12:53:47.605076
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Initialization
    q = Queue()

    # Function under test
    try:
        q.get_nowait()
    except QueueEmpty:
        pass



# Generated at 2022-06-14 12:55:15.293692
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    pass


# Generated at 2022-06-14 12:55:24.589671
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

# Generated at 2022-06-14 12:55:30.574160
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    import time
    from threading import Thread
    from tornado.ioloop import IOLoop

    class TestThread(Thread):
        def __init__(self, q):
            Thread.__init__(self)
            self.queue = q
            self.t0 = None
            self.t1 = None
        def run(self):
            self.t0 = time.time()
            timeout = 0.001
            @gen.coroutine
            def gen_get():
                res = yield self.queue.get(timeout)
                self.t1 = time.time()
                print("Get result: '%s'" % res)
            IOLoop().run_sync(gen_get)

# Generated at 2022-06-14 12:55:41.820700
# Unit test for method put of class Queue
def test_Queue_put():
    import sys
    import tornado.testing
    class MyTestCase(tornado.testing.AsyncTestCase):
        @tornado.testing.gen_test
        async def test_put(self):
            q = Queue(maxsize=2)

            async def consumer():
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

            # Start consumer without waiting (since it never finishes).
            self.io_loop.spawn_callback(consumer)
            await producer()     # Wait for producer to put all tasks.
            await q.join()       #

# Generated at 2022-06-14 12:55:42.647302
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    pass

# Generated at 2022-06-14 12:55:54.204368
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import sys
    import os
    import inspect
    import ast

    # Set test directory and test file path
    test_dir = os.path.dirname(__file__)
    path = os.path.join(test_dir, 'test_Queue_put_nowait_results.txt')
    path = os.path.normpath(path)
    # Read expected results from file
    with open(path, 'r') as file:
        content = file.readlines()

    # Set module and function to test
    module = sys.modules[__name__]
    function = module.Queue.put_nowait

    # Retrieve arguments to pass to function
    # No arguments to retrieve

    # Set expected results
    expected_results = content

    # Get results from function
    # No results to get

    # Test if results match expected results

# Generated at 2022-06-14 12:55:56.700609
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    future = q.put(1)
    assert future.result(timeout=0.01) == None


# Generated at 2022-06-14 12:56:06.576609
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado.gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    import datetime
    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await tornado.gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()  # Wait for producer to put all tasks.
        await q.join()  # Wait for consumer to finish all tasks