

# Generated at 2022-06-14 12:46:09.387718
# Unit test for method put of class Queue
def test_Queue_put():
    Queue()
    # assert False # TODO: implement your test here


# Generated at 2022-06-14 12:46:18.716072
# Unit test for method get of class Queue
def test_Queue_get():
    def _run_get_test(get_function_name, timeout_param_name):
        def check_exception_name(q, timeout):
            future = getattr(q, get_function_name)(**{timeout_param_name: timeout})

            #function that returns the instance of the exception that was raised,
            #if any, or false otherwise
            def get_exception():
                try:
                    ioloop.IOLoop.current().run_sync(future)
                    return False
                except gen.TimeoutError:
                    return gen.TimeoutError

            def check_false(q, timeout):
                return False

            return check_false if timeout is None else get_exception

        for timeout in [None, 10000, 1000.0, datetime.timedelta(seconds=0.01)]:
            q = Queue()


# Generated at 2022-06-14 12:46:30.549257
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    def consumer():
        c = 1
        while True:
            print('Doing work on %s' % c)
            c = c+1
            yield gen.sleep(0.01)
            q.task_done()
    def producer():
        for item in range(5):
            q.put_nowait(item)
            print('Put %s' % item)
    def main():
        IOLoop.current().spawn_callback(consumer)
        IOLoop.current().spawn_callback(producer)
    IOLoop.current().run_sync(main) 


# Generated at 2022-06-14 12:46:38.050823
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(0)
    q.put_nowait(1)
    q.qsize()
    #q.get_nowait()#ValueError
    try:
        q.get_nowait()
        q.get_nowait()
        q.get_nowait()
        #抛出异常QueueEmpty
    except QueueEmpty as e:
        print(e)
    finally:
        print('Done')

if __name__ == '__main__':
    test_Queue_get_nowait()

# Generated at 2022-06-14 12:46:51.266481
# Unit test for method get of class Queue
def test_Queue_get():
    import asyncio
    from tornado.queues import Queue
    from tornado.testing import gen_test

    @gen.coroutine
    def consumer():
        q = Queue()

        for x in range(5):
            # print('Put: %s' % x)
            yield q.put(x)
        yield q.join()
        # print('Queue is empty')

        for _ in range(5):
            # print('Get: %s' % q.get_nowait())
            q.get_nowait()
        assert q.qsize() == 0
        raise gen.Return(True)

    @gen_test
    async def test_coroutine():
        print(await consumer())

    @asyncio.coroutine
    def test():
        print(test_coroutine())

    test()


# Unit

# Generated at 2022-06-14 12:47:02.821374
# Unit test for method get of class Queue
def test_Queue_get():
    import asyncio
    async def consumer(queue):
        while True:
            item = await queue.get()
            if item is None:
                break
            print('Doing work on {}'.format(item))
            await asyncio.sleep(0.01)
            queue.task_done()

    async def producer(queue):
        for item in range(5):
            await queue.put(item)
            print('Put {}'.format(item))

    async def main():
        queue = Queue(maxsize=2)
        consumer_task = asyncio.create_task(consumer(queue))
        
        await producer(queue)
        await queue.join()
        await queue.get()
        consumer_task.cancel()

    asyncio.run(main())


# Generated at 2022-06-14 12:47:04.008735
# Unit test for method get of class Queue
def test_Queue_get():
    assert(True)


# Generated at 2022-06-14 12:47:09.629884
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    q.get()
    q.put_nowait(1)
    q.get_nowait()
    q.get_nowait()
    q.get()
    q.get()
    q.put(1)
    q.put_nowait(1)
    q.task_done()
    q.task_done()
    q.task_done()
    return q.join()

# Generated at 2022-06-14 12:47:20.945636
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # Initialize a queue with a size 2
    q = Queue(maxsize = 2)

    # As the queue is not full, the put_nowait command should proceed and the
    # the size of the queue should be one
    q.put_nowait(1)
    test_result = (len(q._queue) == 1)

    # As the queue is full, the put_nowait command should raise the QueueFull
    # exception
    try:
        q.put_nowait(2)
        q.put_nowait(3)
        test_result = False
    except QueueFull:
        test_result = test_result and True

    return test_result


# Generated at 2022-06-14 12:47:26.902973
# Unit test for method put of class Queue
def test_Queue_put():
    queue = Queue()
    print(queue.qsize())
    a = queue.put(1)
    b = queue.put(2)
    print(queue.qsize())
    print(a.done())
    print(b.done())
    queue.put_nowait(3)
    queue.put_nowait(4)
    print(queue.qsize())

# Generated at 2022-06-14 12:47:38.640147
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    # + 1
    q.put_nowait(0)
    # + 1
    q.put(0)
    # + 1
    q.put((0, 0))
    # + 1
    q.put((0,))
    # + 1
    q.put(0, None)



# Generated at 2022-06-14 12:47:45.684425
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    for i in range(10):
        q.put_nowait(i)
        assert i == q.get_nowait()
    with pytest.raises(QueueEmpty):
        q.get_nowait()
    q.put_nowait(1)
    q.put_nowait(2)
    with pytest.raises(QueueFull):
        q.put_nowait(3)

# Generated at 2022-06-14 12:47:57.657551
# Unit test for method put of class Queue
def test_Queue_put():
    import tornado
    import tornado.gen


    async def test(queue):
        await queue.put(1)
        await queue.put(2)
        await queue.put(3)
        await queue.put(4)
        await queue.put(5)
        await queue.put(6)
        await queue.put(7)
        await queue.put(8)
        await queue.put(9)


    queue = Queue(maxsize=9)
    test(queue)
    print(queue)
    print(queue.qsize())
    queue.get_nowait()
    print(queue.qsize())
    queue.get_nowait()
    print(queue.qsize())
    queue.get_nowait()
    print(queue.qsize())
    queue.get_nowait()
    print

# Generated at 2022-06-14 12:48:04.574116
# Unit test for method put of class Queue
def test_Queue_put():
    import logging
    from tornado.log import app_log
    from log import logger
    logger.setLevel(logging.DEBUG)
    app_log.setLevel(logging.DEBUG)
    q = Queue(maxsize=2)
    q.put(1)
    q.put(2)
    print(q)
    print(q.empty(), q.full(), q.qsize())



# Generated at 2022-06-14 12:48:10.874700
# Unit test for method get of class Queue
def test_Queue_get():
    class TestQueue(_QueueIterator):
        def _init(self):
            self._queue = collections.deque(['item_1', 'item_2'])

        def __put_internal(self, item):
            self._queue.append(item)

        def _format(self):
            return str(self._queue)

    tq = TestQueue(2)
    item = tq.get()
    assert item == 'item_1'
    item = tq.get_nowait()
    assert item == 'item_2'
    tq.get().add_done_callback(lambda f: f.result())
    tq.put_nowait('item_3')



# Generated at 2022-06-14 12:48:13.904673
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    future = q.put(1)
    print(future)
    future.done()

test_Queue_put()
print("-" * 100)


# Generated at 2022-06-14 12:48:20.209651
# Unit test for method put of class Queue
def test_Queue_put():
	q = Queue(maxsize=2)
	q.put(1)
	q.put(2)
	q.put_nowait(3)
	q.put(4,timeout=None)
	q.put(5,timeout=2)
	q.put(6,timeout=datetime.timedelta(seconds=5))
	
if __name__=='__main__':
	test_Queue_put()

# Generated at 2022-06-14 12:48:26.878278
# Unit test for method put of class Queue
def test_Queue_put():
    # Parameters
    q = Queue()
    timeout = None
    item = None

    # Call function being tested
    future = q.put(
        item, timeout
    )

    # Check results
    q.put_nowait(item)
    future.set_result(None)
    q.put_nowait(item)
    future.set_result(None)
    q.put_nowait(item)
    future.set_result(None)
    q.put_nowait(item)
    future.set_result(None)
    q.put_nowait(item)
    future.set_result(None)
    q.put_nowait(item)
    future.set_result(None)
    q.put_nowait(item)
    future.set_result(None)

# Generated at 2022-06-14 12:48:37.351445
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    """
    This testing case checks that the method get_nowait 
    of class Queue works correctly
    """
    maxsize = 3
    q = Queue(maxsize)
    q.put_nowait(0)
    q.put_nowait(1)
    q.put_nowait(2)
    t = q.get_nowait()
    if t == 0:
        t = q.get_nowait()
    if t == 1:
        t = q.get_nowait()
    if t == 2:
        print("OK")
    else:
        print("ERROR")

# Generated at 2022-06-14 12:48:39.376355
# Unit test for method get of class Queue
def test_Queue_get():
    queue = Queue()
    print(queue.empty())

# test_Queue_get()


# Generated at 2022-06-14 12:48:56.553889
# Unit test for method get of class Queue
def test_Queue_get():
    print("test_Queue_get()")
    ioloop.IOLoop.current().run_sync(put_get)


# Generated at 2022-06-14 12:49:01.797850
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.qsize()==2
    try:
        q.put_nowait(3)
        assert False
    except QueueFull:
        assert True


# Generated at 2022-06-14 12:49:07.007289
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import time
    dict = {'test_Queue_get_nowait': 0}
    def func():
        dict['test_Queue_get_nowait'] += 1
    q = Queue()
    q.get_nowait()
    time.sleep(2)
    assert dict['test_Queue_get_nowait'] == 0

# Generated at 2022-06-14 12:49:13.265755
# Unit test for method put of class Queue
def test_Queue_put():
    # Code here
    q = queue.Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    q.put(6)
    q.put(7)
    q.put(8)
    assert q.maxsize == 10
    assert q.qsize() == 8
    assert q.empty() == False
    assert q.full() == False
    assert q.get() == 1

# Generated at 2022-06-14 12:49:24.547800
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

# Generated at 2022-06-14 12:49:28.790209
# Unit test for method get of class Queue
def test_Queue_get():
    from .queue_test import test_Queue_get
    from .queue_test import test_Queue_get_2
    print ('Running Queue get unit tests')
    test_Queue_get()
    test_Queue_get_2()



# Generated at 2022-06-14 12:49:40.135732
# Unit test for method put of class Queue
def test_Queue_put():
    # Testing for method put
    # of class Queue
    q = Queue(maxsize=2)
    async def consumer():
        #async for item in q:
        #    print('Doing work on %s' % item)
        #    await gen.sleep(0.01)
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        future = q.put('item')
        while True:
            try:
                await future
            except gen.TimeoutError:
                print('timeout')
            else:
                print('put')
            if q.full():
                break
            future = q.put('item')



# Generated at 2022-06-14 12:49:44.962834
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Queue.get_nowait(self)
    q = Queue()
    q.empty() is True
    try:
        q.get_nowait()
        raise Exception("QueueEmpty is not raised")
    except QueueEmpty:
        pass
    q.put_nowait(1)
    q.empty() is False
    q.get_nowait() == 1
    q.get_nowait()


# Generated at 2022-06-14 12:49:54.929270
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import tornado
    import time
    import tornado.gen
    import tornado.ioloop
    import tornado.queues
    import tornado.concurrent
    import tornado.locks
    import threading

    q = tornado.queues.Queue(maxsize=0)
    try:
        print('First q.get_nowait()')
        print(q.get_nowait())
    except tornado.queues.QueueEmpty:
        print('First q.get_nowait() raised QueueEmpty')

    # Spawn a producer.
    def producer():
        for i in range(100):
            q.put_nowait(i)
            print('Put')
            time.sleep(0.01)
    threading.Thread(target=producer).start()

    # Spawn a consumer.
    async def consumer():
        consume = 0
       

# Generated at 2022-06-14 12:50:06.334528
# Unit test for method get of class Queue
def test_Queue_get():
    import sys
    import logging
    import unittest
    import asyncio

    from tornado.gen import Wait, Return
    from tornado.queues import Queue

    class TestQueue(unittest.TestCase):
        def setUp(self):
            self.q = Queue()

        def test_basic_get(self):
            @asyncio.coroutine
            def check_getter(self):
                yield self.q.put(42)
                i = yield self.q.get()
                self.assertEqual(i, 42)

            asyncio.get_event_loop().run_until_complete(check_getter(self))

        def test_get_nowait(self):
            self.assertRaises(QueueEmpty, self.q.get_nowait)

# Generated at 2022-06-14 12:50:39.089718
# Unit test for method get of class Queue
def test_Queue_get():
  q = Queue()
  test_Queue_get_res = q.get()
  print("-----result of test_Queue_get")
  print(test_Queue_get_res)
  print("-----result of test_Queue_get")
  return test_Queue_get_res


# Generated at 2022-06-14 12:50:49.192930
# Unit test for method put of class Queue
def test_Queue_put():
    queue = Queue(maxsize=2)
    assert queue.empty() is True
    assert queue.full() is False
    # 依次put
    future = queue.put(0)
    assert queue.empty() is False
    assert queue.full() is False
    future = queue.put(1)
    assert queue.empty() is False
    assert queue.full() is True
    # put一个元素，但是队列已满，会block
    future = queue.put(2, 0.5)
    assert future.result() is None
    assert queue.empty() is False
    assert queue.full() is True
    

# Generated at 2022-06-14 12:50:54.520521
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q._queue.append(1)
    q._queue.append(2)
    q._queue.append(3)
    q._getters.append(1)
    q.get_nowait()
    assert q._queue == collections.deque([2,3])


# Generated at 2022-06-14 12:51:03.349889
# Unit test for method get of class Queue
def test_Queue_get():
    # Set up
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

# Generated at 2022-06-14 12:51:05.094991
# Unit test for method get of class Queue
def test_Queue_get():
    #t = Queue()
    #assert isinstance(t.get(), Future)
    pass

# Generated at 2022-06-14 12:51:07.649270
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put(12)
    q.put(23)
    assert q.get_nowait() == 12
    assert q.get_nowait() == 23



# Generated at 2022-06-14 12:51:13.468032
# Unit test for method get of class Queue
def test_Queue_get():
    # Instance Non-empty queue
    #instance = Queue([1,2,3])
    #assert instance.get() == 1

    # Instance Empty queue
    instance = Queue()
    try:
        instance.get()
    except QueueEmpty:
        assert True
    else:
        assert False


# Generated at 2022-06-14 12:51:25.519575
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    try:
        q = Queue(maxsize=None)
        q.put_nowait(1)
        q.put_nowait(2)
        tmp = q.get_nowait()

        if tmp == 1:
            q.task_done()
        elif tmp == 2:
            q.task_done()
        else:
            print("Failed!")
            return

        tmp = q.get_nowait()
        if tmp == 1:
            q.task_done()
        elif tmp == 2:
            q.task_done()
        else:
            print("Failed!")
            return

        q.join()
        print("Succeeded!")
    except QueueEmpty:
        q.task_done()
        print("Failed!")

# Generated at 2022-06-14 12:51:33.125453
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # test for the function Queue.get_nowait
    q = Queue()
    # test for the empty queue
    try:
        v = q.get_nowait()
        assert False
    except QueueEmpty:
        pass
    # test for the non-empty queue
    global flag
    flag = True
    async def test():
        q.put(1)
        v = q.get_nowait()
        assert v == 1
        if flag:
            raise Exception("Awaitable")
    ioloop.IOLoop.current().run_sync(test)


# Generated at 2022-06-14 12:51:43.182951
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put(42)
    assert q.get_nowait() == 42
    assert q.empty()
    q.put_nowait(42)
    q.put_nowait(43)
    assert q.qsize() == 2
    # test iterator
    assert list(q) == [42, 43]
    q.get_nowait()
    assert q.qsize() == 1
    assert not q.full()
    q.get_nowait()
    assert q.empty()
    q.maxsize = 2
    q.put_nowait(42)
    assert q.full()
    assert q.task_done() is None
    q.put_nowait(42)
    assert q.task_done() is None
    assert not q.full()
    assert q.q

# Generated at 2022-06-14 12:52:43.300210
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import asyncio
    import tornado
    import tornado.queues
    import tornado.autoreload

    q = tornado.queues.Queue()
    q.put(1)
    value = q.get_nowait()
    assert value == 1, 'Object value is not 1'

# Generated at 2022-06-14 12:52:46.819515
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    q.put("a")
    q.put("b")
    try:
        q.put("c")
    except QueueFull:
        print("queue is full")
# test_Queue_put()


# Generated at 2022-06-14 12:52:48.578801
# Unit test for method put of class Queue
def test_Queue_put():
    # Put an item into the queue, perhaps waiting until there is room.
    raise NotImplementedError()


# Generated at 2022-06-14 12:52:57.110349
# Unit test for method get of class Queue
def test_Queue_get():

	from tornado import gen
	from tornado.ioloop import IOLoop
	from tornado.queues import Queue
	
	# Case 0: if getters is empty, then a new Future is created, and it is appended to getters
	
	# q = Queue(maxsize=2)
	# q._getters = []
	# q.get(timeout=None)
	# assert len(q._getters) == 1
	
	# Case 1: if getters is not empty, then the getters is popped and an item is got from the queue
	
	q = Queue(maxsize=2)
	q._unfinished_tasks = 0
	q._finished = Event()
	q._finished.set()
	q._getters = collections.deque([])
	q._putters = collections.deque([])

# Generated at 2022-06-14 12:53:08.146088
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

# Generated at 2022-06-14 12:53:15.623267
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    class MyQueue(Queue):
        def _get(self) -> _T:
            return self._queue.popleft()

        def _put(self, item: _T) -> None:
            self._queue.append(item)

    q = MyQueue()
    q.put_nowait("first")
    print("first put_nowait success")
    q.put_nowait("second")
    print("second put_nowait success")
    q.put_nowait("third")
    print("third put_nowait success")


# Generated at 2022-06-14 12:53:18.760987
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    f = Future()
    f.set_result(5)
    q._getters.append(f)
    q._queue.append(5)
    x = q._get()
    assert x == 5

# Generated at 2022-06-14 12:53:26.427297
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

# Generated at 2022-06-14 12:53:27.880779
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
  # Intentionally empty
  pass

# Generated at 2022-06-14 12:53:29.329406
# Unit test for method put of class Queue
def test_Queue_put():
    assert True

# Generated at 2022-06-14 12:55:39.600039
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    def test():
        q = Queue(maxsize=5)
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
        q.put_nowait(4)
        q.put_nowait(5)
        return q
    return test


# Generated at 2022-06-14 12:55:44.722904
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(2)
    q.put_nowait(3)
    q.put_nowait(4)
    print(q.put_nowait(5))
    res = q.get_nowait()
    print(res)

# Generated at 2022-06-14 12:55:48.927440
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put(item=10, timeout=30)
    q.put(item=20, timeout=None)
    q.put(item=30, timeout=40)

# Generated at 2022-06-14 12:55:53.603065
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    print(q.maxsize)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    print(q.qsize())
    print(q.put_nowait(5))
    print(q.qsize())
