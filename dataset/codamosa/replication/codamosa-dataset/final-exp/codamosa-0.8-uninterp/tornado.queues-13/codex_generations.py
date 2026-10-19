

# Generated at 2022-06-14 12:46:35.442650
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    q.put_nowait("put")
    assert q.qsize() == 1

    try:
        q.put_nowait("put")
    except QueueFull:
        print("test_Queue_put_nowait passed")




# Generated at 2022-06-14 12:46:39.235606
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(4)
    
    for i in range(4):
        q.put_nowait(i)

    for i in range(4):
        assert q.get_nowait() == i
    assert None


# Generated at 2022-06-14 12:46:51.916851
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    class Queue(Generic[_T]):
        # Exact type depends on subclass. Could be another generic
        # parameter and use protocols to be more precise here.
        _queue = None  # type: Any

        def __init__(self, maxsize: int = 0) -> None:
            if maxsize is None:
                raise TypeError("maxsize can't be None")

            if maxsize < 0:
                raise ValueError("maxsize can't be negative")

            self._maxsize = maxsize
            self._init()
            self._getters = collections.deque([])  # type: Deque[Future[_T]]
            self._putters = collections.deque([])  # type: Deque[Tuple[_T, Future[None]]]
            self._unfinished_tasks = 0
            self._finished = Event()
           

# Generated at 2022-06-14 12:47:03.874362
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

# Generated at 2022-06-14 12:47:07.899081
# Unit test for method get of class Queue
def test_Queue_get():
    import asyncio
    from tornado.queues import Queue
    q = Queue()
    def func():
        q.put(1)
    async def test():
        task = asyncio.create_task(q.get())
        func()
        await task
        
    test()

# Generated at 2022-06-14 12:47:09.936102
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    for item in range(3):
        q.put_nowait(item)


# Generated at 2022-06-14 12:47:22.895826
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

# Generated at 2022-06-14 12:47:25.706406
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    aQueue = Queue()
    aQueue.put_nowait(1)
    if aQueue.qsize() != 1:
        raise Exception("Failed")



# Generated at 2022-06-14 12:47:33.765396
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    
    test_queue = Queue()

    assert test_queue.qsize() == 0

    test_queue.__put_internal(1)
    assert test_queue.qsize() == 1
    assert test_queue.get_nowait() == 1
    assert test_queue.qsize() == 0
    assert len(test_queue._queue) == 0

    test_queue.__put_internal(2)
    test_queue.__put_internal(3)
    test_queue.__put_internal(4)
    test_queue.__put_internal(5)
    test_queue.__put_internal(6)
    assert test_queue.qsize() == 5
    assert test_queue.get_nowait() == 2
    assert test_queue.qsize() == 4
    assert test_queue.get_now

# Generated at 2022-06-14 12:47:42.313761
# Unit test for method put of class Queue
def test_Queue_put():
    import asyncio
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

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
        IOLoop.current().spawn_callback(consumer)
        yield producer()     # Wait for producer to put all tasks.

# Generated at 2022-06-14 12:48:00.022547
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import unittest
    from tornado.queues import Queue
    from tornado.testing import AsyncTestCase, gen_test
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String, create_engine
    from sqlalchemy.orm import sessionmaker

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)
        password = Column(String)

        def __repr__(self):
            return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


# Generated at 2022-06-14 12:48:06.584913
# Unit test for method put of class Queue
def test_Queue_put():
    def test_put1():
        q = Queue(maxsize=2)
        q.put_nowait(0)
        q.put_nowait(1)
        assert q.maxsize == 2
        assert q.qsize() == 2
        assert q.empty() == False
        assert q.full() == True

    def test_put2():
        q = Queue(maxsize=2)
        q.put_nowait(0)
        assert q.qsize() == 1
        assert q.empty() == False
        assert q.full() == False
        q.put_nowait(1)
        assert q.qsize() == 2
        assert q.empty() == False
        assert q.full() == True

    def test_put3():
        q = Queue(maxsize=2)
        q

# Generated at 2022-06-14 12:48:16.820757
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

# Generated at 2022-06-14 12:48:25.130312
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

# Generated at 2022-06-14 12:48:33.038492
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=10)
    for i in range(10):
        q.put_nowait(i)
    assert str(q) == "<Queue maxsize=10 queue=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]>"
    try:
        q.put_nowait(10)
        assert False
    except:
        pass


# Generated at 2022-06-14 12:48:39.988578
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()

    f1 = q.get_nowait()
    assert type(f1) == Future

    f2 = q.get()
    assert type(f2) == Future

    f3 = q.get(timeout = 1)
    assert type(f3) == Future

    f4 = q.get(timeout = datetime.timedelta(seconds = 1))
    assert type(f4) == Future


# Generated at 2022-06-14 12:48:41.524346
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    q.get(0)



# Generated at 2022-06-14 12:48:49.780562
# Unit test for method get of class Queue
def test_Queue_get():
    import unittest
    class TestQueue(unittest.TestCase):
        def setUp(self):
            class A:
                def __init__(self,x):
                    self.x=x
                def __eq__(self,other):
                    return self.x==other.x
            self.q = Queue()
            self.q._queue.append(A(1))
            self.q._queue.append(A(2))
            self.q._queue.append(A(3))
        def test_get_1(self):
            self.assertEqual(self.q.get(),1)
        def test_get_2(self):
            self.assertEqual(self.q.get(),1)
            self.assertEqual(self.q.get(),2)

# Generated at 2022-06-14 12:49:01.984093
# Unit test for method put of class Queue
def test_Queue_put():
	from tornado.ioloop import IOLoop
	from tornado.queues import Queue
	import time
	q = Queue()

	@gen.coroutine
	def producer():
		yield q.put("a")
		print("Put: a")
		print("q.qsize 1: ", q.qsize())
		yield q.put("b")
		print("Put: b")
		print("q.qsize 2: ", q.qsize())
	print("q: ", q)

	#@gen.coroutine
	def consumer():
		print("consumer start")
		while True:
			print("consumer run")
			print("q.qsize 3: ", q.qsize())
			item = yield q.get()

# Generated at 2022-06-14 12:49:12.266150
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    see_unfinished = q._unfinished_tasks
    see_getters = q._getters
    see_putters = q._putters
    see_queue = q._queue
    see_full = q.full()
    try:
        q.put_nowait(1)
    except QueueFull:
        pass
    see_unfinished = q._unfinished_tasks
    see_getters = q._getters
    see_putters = q._putters
    see_queue = q._queue
    see_full = q.full()
    try:
        q.put_nowait(1)
    except QueueFull:
        pass
    see_unfinished = q._unfinished_tasks
    see_getters = q._getters
    see

# Generated at 2022-06-14 12:49:24.897562
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    qsize = 10
    q = Queue(qsize)
    for i in range(qsize):
        q.put(i)
    for i in range(qsize):
        assert i == q.get_nowait()
    try:
        q.get_nowait()
    except QueueEmpty:
        return
    assert False
test_Queue_get_nowait()



# Generated at 2022-06-14 12:49:37.238465
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.gen import coroutine, sleep
    
    
    q = Queue(maxsize=5)

    @coroutine
    def consumer():
        lst = []
        res = 5
        while True:
            item = yield q.get()
            lst.append(item)
            try:
                print('Doing work on %s' % item)
                yield sleep(0.01)
            finally:
                q.task_done()

    @coroutine
    def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    @coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current

# Generated at 2022-06-14 12:49:48.522619
# Unit test for method get of class Queue
def test_Queue_get():
    import sys
    import os
    import inspect
    import pytest
    curr_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parent_dir = os.path.dirname(curr_dir)
    sys.path.insert(0, parent_dir)
    from pyq import Queue

    def method_main_program(q: Queue):
        q.put_nowait(5)
        assert q.get_nowait() == 5
        # Test put_nowait of class Queue
        with pytest.raises(QueueFull):
            q.put_nowait(5)
        assert q.get() == 5
        # Test get of class Queue


    # Test get of class Queue

# Generated at 2022-06-14 12:49:51.991962
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=1)
    q.put_nowait('a')
    assert q.get_nowait() == 'a'
    try:
        q.put_nowait('a')
        assert False
    except QueueFull:
        pass


# Generated at 2022-06-14 12:50:00.930953
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Initialize some vars that Queue.__init__ uses
    qs = collections.deque()
    empty_getters = collections.deque()
    empty_putters = collections.deque()

    # Initialize q as a new Queue
    q = Queue()

    # Test for expected ValueError (if maxsize is None)
    q.maxsize = None
    try:
        q.get_nowait()
    except ValueError as e:
        pass
    else:
        raise Exception("did not raise ValueError")

    # Test for expected ValueError (if maxsize is < 0)
    q.maxsize = -1
    try:
        q.get_nowait()
    except ValueError as e:
        pass
    else:
        raise Exception("did not raise ValueError")

    # Initialize q

# Generated at 2022-06-14 12:50:11.238223
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    MAXSIZE = 5
    ioloop.install()
    q = Queue(MAXSIZE)
    
    # check the queue is empty after initialization.
    if q.empty():
        print('The queue is empty after initialization.')
    else:
        print('The queue is not empty after initializtion.')
        return False

    # try to get an item from the queue when it is empty
    try:
        print('Trying to get an item from the queue when it is empty.')
        print('The item retrived from the queue is {}'.format(q.get_nowait()))
    except QueueEmpty:
        print('Trying to get an item from the queue when it is empty.')
        print('The Queue is empty, so throw exception QueueEmpty.')

    # check the queue is still empty

# Generated at 2022-06-14 12:50:17.406660
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


# Generated at 2022-06-14 12:50:24.772416
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue()
    # add four items to queue
    queue.put([1])
    queue.put([2])
    queue.put([3])
    queue.put([4])

    # remove four items from queue
    queue.get_nowait()
    queue.get_nowait()
    queue.get_nowait()
    queue.get_nowait()

    # assert queue is empty
    assert len(queue) == 0


# Generated at 2022-06-14 12:50:29.278396
# Unit test for method put of class Queue
def test_Queue_put():
    async def put(q,item):
        await q.put(item)

    q = Queue()
    put(q,1)
    put(q,2)
    put(q,3)
    put(q,4)
    put(q,5)
    put(q,6)
    

# Generated at 2022-06-14 12:50:37.684339
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    future = q.put(1)
    # print(future)
    # print(type(future))
    q.put(2)
    print(q.maxsize)
    print(q.qsize())
    print(q.empty())
    print(q.full())
    # q.put_nowait(3)
    future = q.put(3,timeout=2)
    print(q.qsize())
    print(q.putters)

    

# Generated at 2022-06-14 12:50:50.069386
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(10)
    q.put_nowait(20)
    try:
        q.put_nowait(30)
    except QueueFull:
        return
    assert False, "Couldn't raise QueueFull"

test_Queue_put_nowait()

# Generated at 2022-06-14 12:51:00.102317
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    io_loop = ioloop.IOLoop.current()
    q = Queue(maxsize=3)
    io_loop.run_sync(lambda: q.put(1))
    assert q.qsize() == 1
    assert q._unfinished_tasks == 1
    assert q.empty() == False
    assert q.full() == False
    io_loop.run_sync(lambda: q.put(2))
    assert q.qsize() == 2
    assert q._unfinished_tasks == 2
    assert q.empty() == False
    assert q.full() == False
    io_loop.run_sync(lambda: q.put(3))
    assert q.qsize() == 3
    assert q._unfinished_tasks == 3
    assert q.empty() == False
    assert q.full()

# Generated at 2022-06-14 12:51:05.540541
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(2)
    print('queue', q)
    print('empty', q.empty())
    q._init()
    print('queue', q)
    print('empty', q.empty())
    q._queue = collections.deque([1])
    print('queue', q)
    print('empty', q.empty())
    x = q._get()
    print('x', x)
    print('queue', q)
    print('empty', q.empty())


# Generated at 2022-06-14 12:51:08.091112
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        q.put_nowait(3)
        assert False
    except QueueFull:
        assert True
    except:
        assert False


# Generated at 2022-06-14 12:51:09.698250
# Unit test for method get of class Queue
def test_Queue_get():
    t = Queue(maxsize=10)
    x = t.get()
    assert x



# Generated at 2022-06-14 12:51:12.947111
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(1)
    q.put_nowait(0)
    q.get_nowait()

# Generated at 2022-06-14 12:51:19.719140
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    print("Testing Queue.get_nowait()...", end = '')

    q = Queue(maxsize=2)
    q.put(42)
    q.put(100)
    assert q.get_nowait() == 42
    assert q.get_nowait() == 100

    try:
        q.get_nowait()
        assert False
    except QueueEmpty:
        pass

    print("Passed!")


# Generated at 2022-06-14 12:51:26.494063
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    result = q.put(1)
    assert result.done()
    assert result.result() == None
    assert q._queue == deque([1])
    q.put_nowait(2)
    assert q._queue == deque([1, 2])
    q.put_nowait(3)
    assert q._queue == deque([1, 2, 3])

# Generated at 2022-06-14 12:51:28.805169
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    assert q.qsize() == 0
    assert not q.full()
    assert q.empty()

# Generated at 2022-06-14 12:51:41.156503
# Unit test for method put of class Queue
def test_Queue_put():
    import time
    import numpy
    from random import shuffle
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado import gen
    from tornado.concurrent import Future
    from tornado.locks import Event
    q = Queue(maxsize=5)
    async def putter():
        for i in range(5):
            for j in range(5):
                await q.put(i)
                print('Put %s' % i)
    async def getter():
        while True:
            item = await q.get()
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    async def main():
        consumer = getter()
        producer = putter()
       

# Generated at 2022-06-14 12:51:58.398162
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

# Generated at 2022-06-14 12:52:05.992126
# Unit test for method get of class Queue
def test_Queue_get():
    def run_test(name, return_value):
        print('\ntesting queue: %s' %name)
        q = Queue(maxsize=2)
        print('calling q.get(timeout=1): %s' %name)
        res = q.get(timeout= 1)
        print('q.get() - returned: %s' %res)
        res = res.result()
        print('res.result() - returned: %s' %res)

test_Queue_get()


# Generated at 2022-06-14 12:52:08.376365
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    queue = Queue(maxsize=1)
    queue.put_nowait(5)
    assert queue.get_nowait() == 5
    assert queue.empty()


# Generated at 2022-06-14 12:52:14.618108
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    """
    Test put_nowait
    Test whether put_nowait is working correctly
    Calling put_nowait to insert data into the queue
    """
    a = Queue()
    a.put_nowait(1)
    a.put_nowait(2)
    a.put_nowait(3)
    assert a.qsize() == 3, "qsize() should return 3"


# Generated at 2022-06-14 12:52:22.774758
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():

    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                print("Doing work on", item)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print("Put", item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()  # Wait for producer to put all tasks.
        await q.join()  # Wait for consumer to finish all tasks.
        print("Done")

    ioloop.IOLoop.current().run_sync(main)



# Generated at 2022-06-14 12:52:26.501446
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # type: () -> None
    q = Queue()
    q.put_nowait(1)
    assert q.get_nowait() == 1
    assert q.empty()
    try:
        q.get_nowait()
        assert False, "expected exception"
    except QueueEmpty:
        pass



# Generated at 2022-06-14 12:52:27.940180
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    print(Queue._get.__doc__)



# Generated at 2022-06-14 12:52:35.732417
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    print('q=', q)

    try:
        q.put_nowait(1)
    except QueueFull:
        print('QueueFull exception raised')

    try:
        q.put_nowait(2)
    except QueueFull:
        print('QueueFull exception raised')

    try:
        q.put_nowait(3)
    except QueueFull:
        print('QueueFull exception raised')

    print('q=', q)



# Generated at 2022-06-14 12:52:46.525555
# Unit test for method get of class Queue
def test_Queue_get():
    if __name__ == '__main__':
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
            await q.join()       # Wait for

# Generated at 2022-06-14 12:52:51.862866
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    try:
        q.put_nowait(1)
    except:
        pass
    try:
        q.put_nowait(2)
    except:
        pass
    exception_has_been_raised = False
    try:
        q.put_nowait(3)
    except:
        exception_has_been_raised = True
    return exception_has_been_raised

# Generated at 2022-06-14 12:53:03.529229
# Unit test for method put of class Queue
def test_Queue_put():
    def method(maxsize = 0):
        '''A method of class Queue which can be tested.'''
        q = Queue(maxsize = maxsize)
        return q.put(0.0)
    # Add your test cases here


# Generated at 2022-06-14 12:53:10.886055
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put_nowait(1)
    assert q.get_nowait() == 1
    q.put_nowait(2)
    q.put_nowait(3)
    q.put_nowait(4)
    assert q.get_nowait() == 2
    q.task_done()
    assert q.get_nowait() == 3
    q.task_done()
    assert q.get_nowait() == 4
    q.task_done()
    q.join()
    q.put_nowait(5)
    try:
        assert q.get_nowait() == 5
    except QueueEmpty:
        pass



# Generated at 2022-06-14 12:53:14.831870
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    q.put(1)
    q.put(2)
    item = q.get()
    print(item)
    item = q.get()
    print(item)
    q.task_done()
    q.task_done()


# Generated at 2022-06-14 12:53:24.693817
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    def test_body(self):
        async def consumer():
            async for item in q:
                try:
                    assert item == 1, "Can't get item"
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
        a_test = gen.coroutine(main)
        io = IOLoop

# Generated at 2022-06-14 12:53:36.288447
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # Verify that type of get_nowait function return value is None
    queue = Queue(3)
    assert(isinstance(queue.get_nowait(), None.__class__)), "ERROR: in Queue::get_nowait(), return value type is not None."

    queue = Queue(3)
    queue.put_nowait(1)
    assert(queue.qsize() == 1), "ERROR: in Queue::get_nowait(), unable to put_nowait()"
    queue.put_nowait(2)
    assert(queue.qsize() == 2), "ERROR: in Queue::get_nowait(), unable to put_nowait() back to back"
    queue.put_nowait(3)

# Generated at 2022-06-14 12:53:46.794145
# Unit test for method put of class Queue
def test_Queue_put():
    import asyncio
    import time
    from tornado.platform.asyncio import BaseAsyncIOLoop
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.ioloop import IOLoop
    async def test_put(q):
        for i in range(20):
            await q.put(1)
            print("put {}".format(i))
            await asyncio.sleep(0.1)
    async def test_get(q):
        while True:
            i = await q.get()
            print("get {}".format(i))
            q.task_done()
    q = Queue(maxsize=10)
    AsyncIOMainLoop().install()
    io_loop = IOLoop.instance()
    io_loop.create_task(test_put(q))
   

# Generated at 2022-06-14 12:53:52.213006
# Unit test for method get of class Queue
def test_Queue_get():
    
    async def test_get():
        queue = Queue()
        await queue.put("First")
        await queue.put("Second")
        item = await queue.get()
        assert item == "First"
        
    ioloop.IOLoop.current().run_sync(test_get)


# Generated at 2022-06-14 12:54:01.267380
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



# Generated at 2022-06-14 12:54:10.331258
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

# Generated at 2022-06-14 12:54:14.390972
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    try:
         q.put_nowait(3)
    except Exception as e:
         print(type(e),e.args)
    q.empty()
    q.full()


# Generated at 2022-06-14 12:54:43.197383
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait(): 
	import time
	import random
	from queue import Queue
	import multiprocessing 
	q = Queue(maxsize=0)
	@gen.coroutine
	def consumer(q):
		while True:
			try:
				item = yield q.get()
				print(item)
			finally:
				q.task_done() 

	@gen.coroutine
	def producer(q):
		for i in range(10):
			item = random.random()
			q.put(item)
			time.sleep(0.2)
			print("Put %s" % item)


# Generated at 2022-06-14 12:54:50.187164
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)
    q.put_nowait(1)
    assert q.get_nowait() == 1
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3
    q.put_nowait(4)
    q.put_nowait(5)
    assert q.get_nowait() == 4
    assert q.get_nowait() == 5
    assert q.empty()
    q.put_nowait(6)
    q.put_nowait(7)
    assert q.get_nowait() == 6

# Generated at 2022-06-14 12:55:00.838090
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    print("method put of Queue")
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

    ioloop.IOLoop.current().run

# Generated at 2022-06-14 12:55:04.751950
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    a = gen.Task(q.get())
    assert a._futures.done() == False
    q.put_nowait(12345)
    #assert a._futures.done() == True

# Generated at 2022-06-14 12:55:07.354245
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    async def consumer():
        async for item in q:
            print('Doing work on %s' % item)
    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
    async def main():
        consumer()
        await producer()
    main()

# Generated at 2022-06-14 12:55:08.676024
# Unit test for method put of class Queue
def test_Queue_put():
    # Class Queue has no method put
    pass

# Generated at 2022-06-14 12:55:21.782314
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    from tornado.concurrent import Future
    from tornado.locks import Event
    from threading import Thread
    import time
    import pytest
    import sys
    def start_loop(loop):
        async def consumer():
            async for item in q:
                try:
                    print('Doing work on %s' % item)
                    time.sleep(0.01)
                finally:
                    q.task_done()

        async def producer():
            for item in range(5):
                await q.put(item)
                print('Put %s' % item)
        async def main():
            # Start consumer without waiting (since it never finishes).
            IOLoop.current().spawn_callback(consumer)
            await producer()

# Generated at 2022-06-14 12:55:23.556566
# Unit test for method get of class Queue
def test_Queue_get():
    #this code is used to test the Queue.get method of the Queue class
    itemQueue = Queue()
    consumer(itemQueue)
    producer(itemQueue)


# Generated at 2022-06-14 12:55:29.764600
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(1)
    print("Put a Task in the Queue")
    q.put("Task_0")
    print("Put a Task in the Queue")
    q.put("Task_1")
    assert q.qsize()==1
    print("Try Put a Task in the Queue")
    try:
        print("Put a Task in the Queue")
        q.put("Task_2")
    except QueueFull:
        print("The Queue is Full, Throw QueueFull Exception")
    print("The Task are ",q.qsize())
    print("Put a Task in the Queue")
    q.put("Task_2", time.time()+2)
    print("The Task are ",q.qsize())
    time.sleep(2)
    print("Put a Task in the Queue")

# Generated at 2022-06-14 12:55:32.092166
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.get_nowait()
