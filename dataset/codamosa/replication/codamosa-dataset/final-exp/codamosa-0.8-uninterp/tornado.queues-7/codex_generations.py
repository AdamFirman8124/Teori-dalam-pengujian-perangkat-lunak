

# Generated at 2022-06-14 12:46:33.733821
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    task = Future()
    task.set_result(None)
    q._putters.append((3, task))
    future = Future()
    future.set_result(None)
    q._getters.append(future)
    try:
        q.put_nowait(3)
    except QueueFull:
        q.put(3)
    task.set_result({'t': 4})
    q._finished.set()
    q.task_done()
    q.get(100)
    assert q._finished.is_set()
    assert q._unfinished_tasks == 0
    assert q.empty()
    assert task.result() == {'t': 4}
    assert q._getters == deque([])
    assert q._putters == deque([])
   

# Generated at 2022-06-14 12:46:41.741715
# Unit test for method get of class Queue
def test_Queue_get():
    def testFunc1():
        # Queue(maxsize=None)
        # Queue.get()
        q = Queue(maxsize=None)

        # Test 1
        if not q.empty():
            if q.get().result():
                return False
        else:
            if q.get().exception():
                return False
        # Test 2
        q.put_nowait(1)
        if not q.empty():
            if q.get().result() != 1:
                return False
        else:
            if q.get().exception():
                return False
        # Test 3
        if not q.empty():
            if q.get().result() != 1:
                return False
        else:
            if q.get().exception():
                return False
        # Test 4
        q.put_now

# Generated at 2022-06-14 12:46:50.252904
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    # Case when queue is not full
    try:
        q.put_nowait(1)
        q.put_nowait(2)
        assert q.qsize() == 2
    except:
        # If the queue is full, we raise QueueFull error
        assert False
    # Case when queue is full
    try:
        q.put_nowait(3)
        q.put_nowait(4)
        assert False
    except:
        assert q.qsize() == 2


# Generated at 2022-06-14 12:46:54.986713
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    q.get_nowait()
    print(q.qsize())
    with pytest.raises(QueueFull):
        q.put_nowait(3)

    f = q.put(3)
    f.result()
    assert q.qsize() == 1

        

# Generated at 2022-06-14 12:47:07.807552
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

# Generated at 2022-06-14 12:47:13.850825
# Unit test for method put of class Queue
def test_Queue_put():
    import asyncio

    q = Queue(maxsize=10)
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
        # Start consumer without waiting (since it never finishes).
        asyncio.ensure_future(consumer())
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    asyncio.run(main())


# Generated at 2022-06-14 12:47:19.997328
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    def f():
        if not self._putters:
            raise QueueEmpty
        assert self.full(), "queue not full, why are putters waiting?"
        item, putter = self._putters.popleft()
        self.__put_internal(item)
        future_set_result_unless_cancelled(putter, None)
        return self._get()

# Generated at 2022-06-14 12:47:30.465036
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


# Generated at 2022-06-14 12:47:40.219661
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

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

    async def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        await producer()  # Wait for producer to put all tasks.
        await q.join()  # Wait for consumer to finish all tasks.
        print("Done")

# Generated at 2022-06-14 12:47:46.210828
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(0)
    q.put_nowait(1)
    #if(q.full() == True):
    #    q.put_nowait(2)
    #else:
    #    print("q is not full")


# Generated at 2022-06-14 12:47:57.610898
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=3)
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3


# Generated at 2022-06-14 12:48:09.758901
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    _QueueIterator = _QueueIterator
    QueueEmpty = QueueEmpty
    QueueFull = QueueFull
    _set_timeout = _set_timeout
    Queue = Queue
    QueueEmpty = QueueEmpty
    QueueFull = QueueFull
    collections = collections
    Future = Future
    future_set_result_unless_cancelled = future_set_result_unless_cancelled
    ioloop = ioloop
    gen = gen
    _display_list_as_list = _display_list_as_list
    _display_list_as_list = _display_list_as_list
    q = Queue(maxsize=2)

# Generated at 2022-06-14 12:48:18.432344
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize = 2)
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

# Generated at 2022-06-14 12:48:24.611254
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    print(q)
    print(q._putters)  # deque([])
    print(q.put(1, timeout=1))
    print(q.put(2, timeout=2))
    #print(q.put(3, timeout=3))  # will raise QueueFull()
    print(q._putters)  # deque([(3, <Future pending cb=[<TaskWakeupMethWrapper object at 0x10c338dd8>()]>]))
    print(q)  # <Queue at 0x10c338948 maxsize=2 queue=[1, 2]>
    print(q)  # <Queue at 0x10c338948 maxsize=2 queue=[1, 2]>

# Generated at 2022-06-14 12:48:38.390670
# Unit test for method get of class Queue
def test_Queue_get():
    def setUp():
        def get(timeout):
            pass
        queue = Queue()
        queue.get = get
    # """
    # Test the method get of the class Queue.
    # """

    # def get(self, timeout: Optional[Union[float, datetime.timedelta]] = None) -> Awaitable[_T]:
    #     """Remove and return an item from the queue.
    #     """
    #     future = Future()  # type: Future[_T]
    #     try:
    #         future.set_result(self.get_nowait())
    #     except QueueEmpty:
    #         self._getters.append(future)
    #         _set_timeout(future, timeout)
    #     return future

# Generated at 2022-06-14 12:48:46.725827
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    print(type(q))
    from tornado.ioloop import IOLoop
    from tornado import gen
    @gen.coroutine
    def test_put_nowait():
        q.put_nowait(1)
        yield gen.sleep(1)
        q.put_nowait(2)
        yield gen.sleep(1)
        q.put_nowait(3)
        yield gen.sleep(1)
        q.put_nowait(5)
        yield gen.sleep(1)
        q.put_nowait(6)

    try:
        IOLoop.current().run_sync(test_put_nowait)
    except Exception as e:
        print(e)



# Generated at 2022-06-14 12:48:50.226260
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    try:
        q.put_nowait(3)
    except QueueFull:
        pass
    else:
        assert False, 'expect raise QueueFull'

# Generated at 2022-06-14 12:48:56.701732
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    def test(q):
        t,i=q.get_nowait()
        return t==1 and i=='i'
    q=Queue(maxsize=5)
    q.put_nowait((1,2))
    q.put_nowait((1,'i'))
    q.put_nowait((2,'i'))
    res=test(q)
    assert res==True


# Generated at 2022-06-14 12:49:08.530084
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

# Unit test

# Generated at 2022-06-14 12:49:15.555131
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    import asyncio
    async def consumer():
        for i in range(3):
            print('consume: ' + str(await q.get()))
            await gen.sleep(0.01)
        print('consume: done')
        q.task_done()
    q = Queue(maxsize=2)
    IOLoop.current().spawn_callback(consumer)
    # q.put_nowait(0)
    # q.put_nowait(1)
    # q.put_nowait(2)
    IOLoop.current().start()

test_Queue_put_nowait()


# Generated at 2022-06-14 12:49:30.529013
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    @gen.coroutine
    def producer():
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

    @gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')

    ioloop.IOLoop.current

# Generated at 2022-06-14 12:49:41.276985
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    """
    This is only a local unit test.
    To run this unit test, please enter the following command in the terminal:
        /path/to/tornado/tornado/test/queues_test.py Queue.get_nowait

    Example:
        python3 /path/to/tornado/tornado/test/queues_test.py Queue.get_nowait
    """
    print("===== Start of Unit Test of method get_nowait in class Queue =====")
    q = Queue(maxsize = 0)
    # add items
    q.put_nowait(0)
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    q.put_nowait(4)
    print(q)
    # remove two

# Generated at 2022-06-14 12:49:45.451133
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    assert not q.empty()
    assert not q.full()
    assert q.put_nowait(1) == 1
    assert not q.empty()
    assert not q.full()

# Generated at 2022-06-14 12:49:49.637446
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    try:
        q.put_nowait(1)
    except QueueFull:
        pass
    else:
        print("test_Queue_put_nowait fails")


# Generated at 2022-06-14 12:49:58.339065
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado
    import datetime
    import time
    from tornado.queue import Queue

    @tornado.gen.coroutine
    def consumer():
        while True:
            item = yield q.get()
            try:
                print('Doing work on %s' % item)
                yield tornado.gen.sleep(0.01)
            finally:
                q.task_done()

    @tornado.gen.coroutine
    def producer():
        for item in range(5):
            yield q.put(item)
            print('Put %s' % item)

    @tornado.gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        tornado.ioloop.IOLoop.current().spawn_callback(consumer)
        yield producer()     # Wait for producer to put all tasks.

# Generated at 2022-06-14 12:50:09.244646
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.queues import Queue

    q = Queue()

    assert q.empty()
    assert q.qsize() == 0

    rs = []
    rs.append(q.get_nowait())
    assert rs[-1].exception() is not None

    q.put_nowait(1)
    assert not q.empty()
    assert q.qsize() == 1
    assert q.get_nowait() == 1
    assert q.empty()
    assert q.qsize() == 0

    f = q.put(1)
    assert f.done()
    assert f.result() is None
    assert not q.empty()
    assert q.qsize() == 1
    assert q.get_nowait() == 1

    for i in range(10):
        q.put

# Generated at 2022-06-14 12:50:16.291637
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    async def consumer():
        while True:
            item = await q.get()
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

# Generated at 2022-06-14 12:50:20.959568
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    # We test the functionality of the Queue method get_nowait
    # In this case it will return the element in the queue.
    assert q.get_nowait()== 1




# Generated at 2022-06-14 12:50:25.878323
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(2)
    assert q.empty() is True
    assert q.qsize() == 0
    assert q.full() is False
    item = 1
    result = q.put(item, timeout=None)
    assert result.done() is True
    assert result.result() is None
    assert q.empty() is False
    assert q.qsize() == 1
    assert q.full() is False
    future = Future()
    io_loop = ioloop.IOLoop.current()
    timeout_handle = io_loop.add_timeout(0.01, lambda:future_set_result_unless_cancelled(future, None))
    future_set_result_unless_cancelled(future, None)
    result = q.put(item, timeout=0.01)
    assert result.done

# Generated at 2022-06-14 12:50:30.163448
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=1)
    for i in range(5):
        q.put(i)
    for i in range(5):
        print(nonblocking_next(q.get()))



# Generated at 2022-06-14 12:50:47.893053
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue()
    f = q.put(object())
    assert isinstance(f, Future)
    assert f.result() is None


# Generated at 2022-06-14 12:50:49.466454
# Unit test for method get of class Queue
def test_Queue_get():
  q = Queue()
  a = q.get()
  assert a == None


# Generated at 2022-06-14 12:50:56.826645
# Unit test for method get of class Queue
def test_Queue_get():
    async def f():
        q = Queue(maxsize=2)
        # Put 2 items
        q.put_nowait(1)
        q.put_nowait(2)
        # Get 2 items
        await q.get()
        await q.get()
        # Get 1 item with timeout
        try:
            await q.get(timeout=0.1)
        except gen.TimeoutError:
            print("Get item timeout")

    ioloop.IOLoop.current().run_sync(f)



# Generated at 2022-06-14 12:50:59.003803
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    assert q.empty()==True
    q.put(1)
    assert q.empty()==False
    assert q.get_nowait()==1
    assert q.empty()==True

# Generated at 2022-06-14 12:51:03.432113
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    try:
        q = Queue()
        q.put_nowait('TongTEX')
        q.put_nowait(None)
    except QueueFull:
        print('Queue is full, cannot put value in it')
    except Exception as e:
        print('Exception: ', e)


# unit test for method get_nowait of class Queue

# Generated at 2022-06-14 12:51:12.227859
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    Queue_get_nowait_q1 = Queue(10)
    Queue_get_nowait_q1.put_nowait("hello")
    Queue_get_nowait_q1.put_nowait("world")
    Queue_get_nowait_q1.put_nowait("hello")
    Queue_get_nowait_q1.put_nowait("world")
    Queue_get_nowait_q1.put_nowait("hello")
    Queue_get_nowait_q1.put_nowait("world")
    Queue_get_nowait_q1.put_nowait("hello")
    Queue_get_nowait_q1.put_nowait("world")
    Queue_get_nowait_q1.put_nowait("hello")
   

# Generated at 2022-06-14 12:51:14.440933
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    try:
        q.get_nowait()
        assert False
    except QueueEmpty:
        assert True

# Generated at 2022-06-14 12:51:16.750584
# Unit test for method get of class Queue
def test_Queue_get():
    queue = Queue()
    queue.put(1)
    assert queue.get() == 1


# Generated at 2022-06-14 12:51:28.465171
# Unit test for method get of class Queue
def test_Queue_get():
    import asyncio
    import time
    
    
    def test_case_1():
        q = Queue()
        q.put_nowait(1)
        #assert q.get()==1
        fut = asyncio.get_event_loop().create_future()
        fut.set_result(1)
        assert q.get()==fut
    
    def test_case_2():
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)
        assert q.get()==1
        assert q.get()==2
        
    #test_case_2()

    
    async def test_case_3():
        q = Queue()
        q.put_nowait(1)
        q.put_nowait(2)

# Generated at 2022-06-14 12:51:33.126353
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.qsize() == 2
    assert q.get_nowait() == 1
    assert q.qsize() == 1
    assert q.get_nowait() == 2
    assert q.qsize() == 0


# Generated at 2022-06-14 12:52:01.430848
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize=0)

    q._queue.append(0)
    assert q.get_nowait() == 0
    assert q.empty()



# Generated at 2022-06-14 12:52:10.594848
# Unit test for method put of class Queue
def test_Queue_put():
    import random
    import asyncio
    import tornado.gen

    q = Queue(maxsize=2)

    async def consumer():
        while True:
            item = await q.get()
            print('Doing work on %s' % item)
            await tornado.gen.sleep(0.01)
            q.task_done()

    async def producer():
        for item in range(10):
            await q.put(item)
            print('Put %s' % item)
            await tornado.gen.sleep(random.random())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(producer(), consumer()))



# Generated at 2022-06-14 12:52:20.278558
# Unit test for method put of class Queue
def test_Queue_put():
    def main_f1():
        q = Queue(maxsize=2)
        async def consumer():
            async for item in q:
                try:
                    print('Doing work on %s' % item)
                    await gen.sleep(0.01)
                finally:
                    q.task_done()

        ioloop.IOLoop.current().spawn_callback(consumer)
        async def producer():
            for item in range(5):
                await q.put(item)
                print('Put %s' % item)

        ioloop.IOLoop.current().run_sync(producer)
        async def main():
            await q.join()       # Wait for consumer to finish all tasks.
            print('Done')

        ioloop.IOLoop.current().run_sync(main)

    main_f1

# Generated at 2022-06-14 12:52:24.260448
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=0)
    f = q.get()
    assert str(q) == "<Queue maxsize=0 queue=deque([]) getters[1]>"
    assert not isinstance(f, Future)
    print(f)
test_Queue_get.test_name="test_Queue_get"


# Generated at 2022-06-14 12:52:35.824103
# Unit test for method get of class Queue
def test_Queue_get():
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop
    import time

    @gen.coroutine
    def consumer():
        while True:
            item = yield q.get()
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
            time.sleep(0.01)

    @gen.coroutine
    def main():
        # Start consumer without waiting (since it never finishes).
        IOLoop.current().spawn_callback(consumer)
        yield producer()     # Wait for producer to put all tasks.
        yield

# Generated at 2022-06-14 12:52:37.148161
# Unit test for method get of class Queue
def test_Queue_get():
    # Testing method get of class Queue
    pass

# Generated at 2022-06-14 12:52:48.080010
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(3)
    assert q.qsize() == 0, "Erreur valeur attendue : 0 valeur reçu : %s" % q.qsize()

    assert q.empty() == True, "Erreur valeur attendue : True valeur reçu : %s" % q.empty()

    assert q.full() == False, "Erreur valeur attendue : False valeur reçu : %s" % q.full()

    f = q.put("1")
    assert f.result() == None, "Erreur valeur attendue : None valeur reçu : %s" % f.result()


# Generated at 2022-06-14 12:52:56.369196
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

# Generated at 2022-06-14 12:53:03.096939
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    future = q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    #print(q._putters)
    #print(q._getters)
    print(q.get_nowait())
    print(q.get_nowait())


# Generated at 2022-06-14 12:53:15.427723
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    assert q.qsize() == 0
    # 1. q.put_nowait(1)
    q.put_nowait(1)
    assert q.qsize() == 1
    # 2. q.put_nowait(2)
    q.put_nowait(2)
    assert q.qsize() == 2
    # 3. q.put_nowait(3)
    try:
        q.put_nowait(3)
    except QueueFull:
        pass
    else:
        assert False
    assert q.qsize() == 2
    # 4. q.put_nowait(4, 0.01)
    try:
        q.put_nowait(4, 0.01)
    except gen.TimeoutError:
        pass

# Generated at 2022-06-14 12:54:17.687820
# Unit test for method get of class Queue
def test_Queue_get():
    result = None
    def assert_value():
        nonlocal result
        assert  result == None
    def on_done(val):
        nonlocal result
        result = val
    q = Queue(maxsize=10)
    for val in range(0,10):
        q.put_nowait(val)

    future = q.get()
    future.add_done_callback(on_done)

    Future.from_callable(assert_value).add_done_callback(callback)
    


# Generated at 2022-06-14 12:54:24.387051
# Unit test for method put of class Queue
def test_Queue_put():
    # Create a new queue
    q = Queue(maxsize=2)
    # Call put and add element 1 to the queue
    q.put(1)
    # Call put and add element 2 to the queue
    q.put(2)
    # Call the property empty
    assert q.empty() != True
    # Call the property full
    assert q.full() != False
    # Call the property maxsize
    assert q.maxsize == 2
    # Call the property qsize
    assert q.qsize() == 2
    # Call put with a timeout
    future = q.put(3, timeout=None)
    # Call the property done of future
    assert future.done() != False


# Generated at 2022-06-14 12:54:34.930944
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

# Generated at 2022-06-14 12:54:38.914515
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    try:
        q.put_nowait(1)
        q.put_nowait(2)
        q.put_nowait(3)
    except QueueFull:
        print("queue was full")



# Generated at 2022-06-14 12:54:48.125409
# Unit test for method get of class Queue

# Generated at 2022-06-14 12:54:53.657452
# Unit test for method put of class Queue
def test_Queue_put():
	# create a queue
	q = Queue(maxsize = 3)
	# set value to the queue
	q.put(1)
	# check the value
	if q.empty() != False:
		return False
	return True


# Generated at 2022-06-14 12:54:57.608161
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    q.put(1)
    assert q.get() == 1
    q.put(None)
    assert q.get() is None
    assert q.empty()
    q.put(1)
    assert q.get() == 1



# Generated at 2022-06-14 12:55:02.546976
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    io_loop = ioloop.IOLoop()
    io_loop.make_current()
    q = Queue()
    q.put_nowait(5)
    def test_get(q):
        val = q.get_nowait()
        if (val == 5):
            print("OK")
    io_loop.add_callback(test_get, q)
    io_loop.run_sync(lambda : 1)
test_Queue_put_nowait()


# Generated at 2022-06-14 12:55:07.887617
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    future = Future()  # type: Future[None]
    future.set_result(None)
    assert str(future) == "<Future finished result=None>"
    assert future.done() == True
    assert future.cancelled() == False
    assert future._delegate == _FutureReturn(value = None)



# Generated at 2022-06-14 12:55:15.418158
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(1)
    q.put_nowait(1)
    q.put_nowait(2)
    q._putters.append((1, Future()))
    q._putters.append((1, Future()))
    result = len(q._putters)
    context.test_result = result
