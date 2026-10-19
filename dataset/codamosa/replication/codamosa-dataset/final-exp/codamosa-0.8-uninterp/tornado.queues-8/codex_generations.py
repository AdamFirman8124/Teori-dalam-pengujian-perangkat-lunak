

# Generated at 2022-06-14 12:46:44.832932
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
	# initialise a Queue
	queue = Queue(maxsize=5)
	# check the queue is not full
	if queue.full():
		raise Exception("Queue is full")
	# insert 3 elements in the empty queue
	for i in range(3) :
		queue.put_nowait(i)
	# insert another 2 elements to reach maxsize
	for i in range(2) :
		queue.put_nowait(i)
	# insert another element in the full queue, must raise the exception
	try :
		queue.put_nowait(1)
		raise Exception("QueueFull was not raised")
	except QueueFull :
		return True

# Generated at 2022-06-14 12:46:46.857749
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    q.get()


# Generated at 2022-06-14 12:46:56.450390
# Unit test for method get of class Queue
def test_Queue_get():
    """Test for method get of class Queue"""
    import unittest
    from tornado.queues import Queue
    from tornado.concurrent import Future

    print("Test Queue.get")
   
    # Test case:
    # a queue with no items. 
    
    q = Queue(maxsize=2)
    future = q.get()
    if future is None:
        raise TypeError("future is None")
    if not isinstance(future, Future):
        raise TypeError("future is not a Future")
    if future.done():
        raise ValueError("future is done")
    if not q._getters:
        raise ValueError("queue should have waiting getters")
    if len(q._getters) != 1:
        raise ValueError("wrong number of waiting getters")

# Generated at 2022-06-14 12:47:08.737567
# Unit test for method put of class Queue
def test_Queue_put():
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


# Generated at 2022-06-14 12:47:21.301864
# Unit test for method put of class Queue
def test_Queue_put():
    import random
    import time

    async def producer(queue, n):
        for x in range(n):
            # produce an item
            print('producing {}/{}'.format(x, n))
            # simulate i/o operation using sleep
            await gen.sleep(random.random())
            item = str(x)
            # put the item in the queue
            await queue.put(item)

    async def consumer(queue, n):
        while True:
            # wait for an item from the producer
            item = await queue.get()

            # process the item
            print('consuming {}...'.format(item))
            # simulate i/o operation using sleep
            await gen.sleep(random.random())

            # Notify the queue that the item has been processed
            queue.task_done()


# Generated at 2022-06-14 12:47:31.234282
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(3)
    assert  q.get_nowait() == None
    try:
        q.get()
    except QueueEmpty:
        assert True
    else:
        assert False
    q.put(2)
    assert q.get_nowait() == 2
    try:
        q.get_nowait()
    except QueueEmpty:
        assert True
    else:
        assert False
    try:
        q.get()
    except QueueEmpty:
        assert True
    else:
        assert False
    assert q.empty()
    assert not q.full()
    q.put(1)
    q.put(2)
    assert q.full()
    try:
        q.put(3)
    except QueueFull:
        assert True

# Generated at 2022-06-14 12:47:40.759368
# Unit test for method get of class Queue
def test_Queue_get():
    # test class Queue, method get
    from tornado.queues import Queue
    import time

    def test_get():
        q = Queue(maxsize=2)
        fut = q.put(1)
        assert fut.done()
        assert not fut.exception()
        fut = q.put(2)
        assert fut.done()
        assert not fut.exception()
        try:
            fut = q.put(3)
            assert False, "did not throw QueueFull"
        except QueueFull: pass
        assert not fut.done()
        assert not fut.exception()
        fut = q.get()
        assert fut.done()
        assert not fut.exception()
        assert fut.result() == 1
        fut = q.get()
        assert fut.done()
        assert not fut

# Generated at 2022-06-14 12:47:44.601014
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    
    q.put(1)
    #print(f'the queue is {q}')
    assert q.empty() == False



# Generated at 2022-06-14 12:47:49.420905
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(1)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 1



# Generated at 2022-06-14 12:47:59.652474
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado import queues
    from tornado.ioloop import IOLoop
    from tornado.gen import sleep
    from time import time
    from datetime import datetime
    def _put_nowait(item):
        try:
            q.put(item, timeout = 2)
        except QueueFull:
            pass

# Generated at 2022-06-14 12:48:25.967582
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
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
        IOLoop.current().spawn_callback(consumer)
        yield producer()     # Wait for producer to put all tasks.

# Generated at 2022-06-14 12:48:32.464978
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
	q = Queue(maxsize=2)
	q.put_nowait(1)
	q.put_nowait(2)
	if q.full():
		print("CRITICAL: Queue.put_nowait test failed.")
	else:
		print("Queue.put_nowait test succeded.")

# Generated at 2022-06-14 12:48:33.375607
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    pass



# Generated at 2022-06-14 12:48:38.236844
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q1 = Queue()
    q1.put_nowait(1)
    q1.put_nowait(2)
    assert q1.qsize() == 2
    assert q1.empty() == False
    assert q1.full() == False


# Generated at 2022-06-14 12:48:40.342589
# Unit test for method get of class Queue
def test_Queue_get():
    a = Queue(10)
    a.put(1)
    assert a.qsize() == 1
    assert a.get().result() == 1

# Generated at 2022-06-14 12:48:47.105590
# Unit test for method get of class Queue
def test_Queue_get():
    # Create a queue of integers.
    q = Queue(maxsize=2)
    q.__init__(maxsize=2)
    q.maxsize
    q.qsize()
    q.empty()
    q.full()
    q.put(1)
    q.put(2)
    q.put_nowait(3)
    q.get()
    q.get(timeout=1)
    q.get_nowait()
    q.task_done()
    q.join()
    q.join(timeout=1)
    q.__aiter__()
    q.__repr__()
    q.__str__()


# Generated at 2022-06-14 12:48:48.823513
# Unit test for method get of class Queue
def test_Queue_get():
    fut = Queue.get(1)
    assert fut is not None
    assert isinstance(fut, Future)


# Generated at 2022-06-14 12:48:50.693165
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    _queue = Queue()
    _queue.put_nowait(1)
    assert _queue.qsize() == 1


# Generated at 2022-06-14 12:48:52.277651
# Unit test for method get of class Queue
def test_Queue_get():
	_QueueIterator = Queue()
	return _QueueIterator.get()


# Generated at 2022-06-14 12:49:05.030696
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

# Generated at 2022-06-14 12:49:38.184574
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


# Generated at 2022-06-14 12:49:49.546894
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait(1)
    x=q.get_nowait()
    assert x==1
    #A queue is full when a key is copied and is not able to copy more values
    q=Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    with pytest.raises(QueueFull):
        q.put_nowait(3)
    #A queue is full when a key is copied and is not able to copy more values
    q=Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    with pytest.raises(QueueFull):
        q.put_nowait(3)


# Generated at 2022-06-14 12:49:55.863607
# Unit test for method put of class Queue
def test_Queue_put():
    # Should be able to put many items into an unbounded queue
    q = Queue()
    for i in range(1000):
        q.put(i)
        assert q.qsize() == i + 1, "Put %s items, queue size should be %s" % (i + 1, i + 1)
    # Should be able to get all the items from the queue in FIFO order
    for i in range(1000):
        j = q.get(timeout=10)
        assert i == j, "Got %s, expected %s" % (j, i)



# Generated at 2022-06-14 12:50:07.292573
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado
    import concurrent.futures
    import logging
    _future = Future()
    _future_result = None
    _future_exc = None
    _future_timeout = None
    _future_exception_self = None
    _future_exception_args = None
    _future_exception_kwargs = None
    _future_exception_result = None
    _future_exception_exc = None
    _future_exception_timeout = None
    _future_exception_self = tornado.ioloop.IOLoop.current()
    _future_exception_args = ()
    _future_exception_kwargs = {}
    _future_exception_result = None
    _future_exception_exc = None
    _future_exception_timeout = None
    _future_exception_self

# Generated at 2022-06-14 12:50:16.103459
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    def Queue_get_nowait(q, qsize):
        q._queue = qsize
        for i in range(0, len(qsize)):
            assert q.get_nowait() == qsize.pop(0)
        assert q.empty()
        assert q.qsize() == 0
        assert q._getters == []
        assert q._putters == []
        assert q._unfinished_tasks == 0
    q = Queue(maxsize=0)
    qsize = []
    q._queue = qsize
    assert q.empty()
    assert q.qsize() == 0
    assert q._getters == []
    assert q._putters == []
    assert q._unfinished_tasks == 0
    qsize = ['a']
    Queue_get_nowait(q, qsize)

# Generated at 2022-06-14 12:50:23.326847
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    res = q.get_nowait()
    assert (res==1)
    res = q.get_nowait()
    assert (res==2)
    try:
        q.get_nowait()
        assert False
    except QueueEmpty:
        pass



# Generated at 2022-06-14 12:50:25.879932
# Unit test for method get of class Queue
def test_Queue_get():
    assert type(Queue(maxsize=int).get(timeout=None)) != type(Exception)
    assert issubclass(type(Queue(maxsize=int).get(timeout=None)), Awaitable)

# Generated at 2022-06-14 12:50:30.162515
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.qsize() == 2


# Generated at 2022-06-14 12:50:42.118736
# Unit test for method put of class Queue
def test_Queue_put():
    import tornado
    import tornado.ioloop
    from tornado.queues import Queue
    from tornado import gen
    import time
    import threading
    
    
    q = Queue(2)
    cv = threading.Condition()

    def consumer_handler():
        #consumer()
        async def consumer():
            async for item in q:
                try:
                    print('Doing work on %s' % item)
                    await gen.sleep(0.01)
                finally:
                    q.task_done()
                    
        tornado.ioloop.IOLoop.current().run_sync(consumer)
        
    def main_handler():
        #main()
        async def producer():
            for i in range(5):
                await q.put(i)
                print('Put %s' % i)
                
       

# Generated at 2022-06-14 12:50:47.541488
# Unit test for method put of class Queue
def test_Queue_put():
    timeout: Optional[Union[float, datetime.timedelta]] = None
    item: _T = 1
    future = Future()  # type: Future[None]
    queue = Queue(maxsize=1)
    queue.put(item)
    assert queue.qsize() == 1
    queue.task_done()
    assert queue._unfinished_tasks == 0

# Generated at 2022-06-14 12:51:37.708683
# Unit test for method put of class Queue
def test_Queue_put():
    # Initialize the Queue
    q = Queue(maxsize=5)
    # Put an item into the Queue
    future = q.put(4, timeout=None)
    # Check if the put is successful
    assert q.qsize() == 1
    # Check the future object associated with the put method
    assert future.result() is None
    # Check if the put method fails when the Queue is full
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    assert q.put(5)
    assert q.full()
    # Check if the put method fails when the Queue is full
    # Check the future object associated with the put method
    # when the Queue is full

# Generated at 2022-06-14 12:51:49.149032
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty() == True
    assert q.full() == False
    q.put(1)
    q.put(1)
    q.put(3)
    assert q.qsize() == 3
    assert q.empty() == False
    assert q.full() == True
    assert q.get_nowait() == 1
    q.task_done()
    #test timeout
    assert q.get(timeout = 0.1) == 1
    q.task_done()
    q.get_nowait()
    q.task_done()
    assert q.get_nowait() == 3
    
    



# Generated at 2022-06-14 12:51:57.801373
# Unit test for method get of class Queue
def test_Queue_get():
    import unittest
    import random
    class QueueTestCase(unittest.TestCase):
        def test_Queue_get(self):
            q = Queue(maxsize=1)
            q.put(621)
            self.assertEqual(q.get(), 621)
    
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(QueueTestCase('test_Queue_get'))
        return suite
    
    results = unittest.TextTestRunner(verbosity=2).run(suite())
    if results.wasSuccessful():
        return 0
    else:
        return 1

# Generated at 2022-06-14 12:52:01.651568
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    future = q.put(1, timeout=None)
    assert future.result() is None
    assert isinstance(future, Future)
    assert future.done()


# Generated at 2022-06-14 12:52:10.249085
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado.testing
    import tornado.ioloop

    def test_Queue_get_0():
        q = Queue()

        def get():
            return q.get()

        tornado.testing.gen_test(get)()

        def put():
            return q.put(None)

        tornado.testing.gen_test(put)()
        tornado.ioloop.IOLoop.current().run_sync(put)

    def test_Queue_get_1():
        q = Queue()

        def get():
            return q.get()

        tornado.testing.gen_test(get)()

        def put():
            return q.put(None)

        tornado.testing.gen_test(put)()
        tornado.ioloop.IOLoop.current().run_sync(put)


# Generated at 2022-06-14 12:52:15.324969
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(3)
    q.put_nowait(4)
    if q.get_nowait() == 3:
        print("test_Queue_get_nowait_1 SUCCESS")
    else:
        print("test_Queue_get_nowait_1 FAIL")
    return


# Generated at 2022-06-14 12:52:25.305707
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)

    print('Test put with 0 items:')
    async def consumer():
        try:
            async for item in q:
                try:
                    print('Doing work on %s' % item)
                    await gen.sleep(0.01)
                finally:
                    q.task_done()
        except:
            print('Unexpected Error')

    async def producer():
        for item in range(0):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
       

# Generated at 2022-06-14 12:52:36.283005
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    # q = Queue(maxsize=2)
    #
    # async def consumer():
    #     async for item in q:
    #         try:
    #             print('Doing work on %s' % item)
    #             await gen.sleep(0.01)
    #         finally:
    #             q.task_done()
    #
    # async def producer():
    #     for item in range(5):
    #         await q.put(item)
    #         print('Put %s' % item)
    #
    # async def main():
    #     # Start consumer without waiting (since it never finishes).
    #     IOLoop.current().spawn_callback(consumer)
    #

# Generated at 2022-06-14 12:52:42.861153
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    
    q = Queue(maxsize=2)
    ret = []
    
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    
    async def producer(num):
        for item in range(num):
            await q.put(item)
            ret.append(item)
            print('Put %s' % item)
    
    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer(5)     # Wait for producer to put all

# Generated at 2022-06-14 12:52:52.602576
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    @gen.coroutine
    def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    @gen.coroutine
    def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
    @gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        yield producer()     # Wait for producer to put all tasks.
        yield q.join()       # Wait for consumer to finish all tasks.
        print('Done')
    ioloop

# Generated at 2022-06-14 12:53:36.819567
# Unit test for method get of class Queue
def test_Queue_get():
    a = Queue()
    if a.qsize == 0:
        return True
    else:
        return False
    
    
    
    # Unit test for method get_nowait of class Queue

# Generated at 2022-06-14 12:53:47.108505
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    # it is a bug that future.done should be False
    future = q.put(1, timeout=None)
    if future.done:
        raise Exception("future.done should be False")
    future = q.put(2, timeout=None)
    if future.done:
        raise Exception("future.done should be False")
    future = q.put(3, timeout=None)
    if not future.done:
        raise Exception("future.done should be True")
    if not future.exception():
        raise Exception("future.exception() should be True")
    future = q.put(4, timeout=None)
    if not future.done:
        raise Exception("future.done should be True")

# Generated at 2022-06-14 12:53:52.487632
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=0)
    q.put(1)
    q.put(2)
    assert q.get_nowait()==1
    assert q.get_nowait()==2
    # print(q.__doc__)
test_Queue_get_nowait()


# Generated at 2022-06-14 12:54:01.943278
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

# Generated at 2022-06-14 12:54:06.923193
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    test_str = "test"
    test_q = Queue(maxsize=1)
    test_q.put_nowait(test_str)
    result = test_q.get_nowait()
    if result != test_str:
        raise Exception("test_Queue_get_nowait failed")


# Generated at 2022-06-14 12:54:11.336606
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=5)
    assert q.qsize() == 0
    for i in range(5):
        q.put(i)
    assert q.qsize() == 5
    assert q.putters == []
    assert q.getters == []


# Generated at 2022-06-14 12:54:16.056370
# Unit test for method get of class Queue
def test_Queue_get():

    number_of_get_calls = 0

    class QueueSubclass(Queue):
        def get(self):
            nonlocal number_of_get_calls
            number_of_get_calls += 1
            return super().get()

    queue = QueueSubclass()
    queue.put('x')
    queue.get()
    queue.get()

    return number_of_get_calls


# Generated at 2022-06-14 12:54:24.090108
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
   import tornado.ioloop
   import tornado.gen
   import tornado.queues
   def f():
      tornado.ioloop.IOLoop.current().stop()
   q = tornado.queues.Queue(maxsize=2)
   # put_nowait has no return value.
   tornado.gen.Task(q.put_nowait)(1)
   # get_nowait has no return value.
   tornado.gen.Task(q.get_nowait)()
   # put_nowait has a return value.
   future = tornado.gen.Future()
   tornado.gen.Task(q.put_nowait)(2)
   # get_nowait has a return value.
   future = tornado.gen.Task(q.get_nowait)()

# Generated at 2022-06-14 12:54:25.313462
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)


# Generated at 2022-06-14 12:54:36.147598
# Unit test for method get of class Queue
def test_Queue_get():

    # Queue(int)
    assert isinstance(Queue(maxsize=0), Queue)
    assert isinstance(Queue(maxsize=1), Queue)
    assert isinstance(Queue(maxsize=2), Queue)

    # Queue().get(timeout: Optional[Union[float, datetime.timedelta]] = None) -> Awaitable[_T]
    # Queue().get(timeout: Union[float, datetime.timedelta]) -> Awaitable[_T]
    assert callable(Queue().get())
    assert callable(Queue().get(datetime.timedelta(seconds=0)))
    assert callable(Queue().get(0.0))
    assert callable(Queue().get(timeout=datetime.timedelta(seconds=0)))