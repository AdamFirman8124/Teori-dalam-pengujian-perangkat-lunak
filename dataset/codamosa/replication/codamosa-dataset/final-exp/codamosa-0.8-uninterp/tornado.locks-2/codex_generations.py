

# Generated at 2022-06-14 12:16:08.630563
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    # obj = Semaphore()
    # timeout = None
    # ret = obj.acquire(timeout=timeout)
    # assert ret is not None
    pass



# Generated at 2022-06-14 12:16:10.135616
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    event.set()
    fut = event.wait()
    assert fut.is_done()



# Generated at 2022-06-14 12:16:17.181895
# Unit test for method wait of class Condition
def test_Condition_wait():
    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify(1)
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier()])

    condition = Condition()
    ioloop.IOLoop.current().run_sync(runner)
    # output:
    # I'll wait right here
    # About to notify
    # Done notifying
    # I'm done waiting


# Generated at 2022-06-14 12:16:18.180255
# Unit test for method release of class Lock
def test_Lock_release():
    lock = Lock()
    lock.release()

# Generated at 2022-06-14 12:16:20.755086
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    condition = Condition()
    result = condition.__repr__()
    expected = '<Condition>'
    assert isinstance(result, str)
    assert result == expected


# Generated at 2022-06-14 12:16:23.976123
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    print("Waiting for event")
    event.wait()
    print("Not waiting this time")
    event.wait()
    print("Done")

# Generated at 2022-06-14 12:16:24.802791
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    _test_Semaphore_acquire()

# Generated at 2022-06-14 12:16:27.429827
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    import unittest
    sem = Semaphore(1)
    sem.release()
    sem.release()
    sem.release()
    sem.release()


test_Semaphore_release()

# Generated at 2022-06-14 12:16:28.309619
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    pass

# Generated at 2022-06-14 12:16:32.291887
# Unit test for method wait of class Condition
def test_Condition_wait():
    condition = Condition();
    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier()])

    ioloop.IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:16:50.200908
# Unit test for method wait of class Condition
def test_Condition_wait():
    print('testing Condition.wait...')
    condition = Condition()

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier()])

    ioloop.IOLoop.current().run_sync(runner)



# Generated at 2022-06-14 12:16:51.212926
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    if not event.is_set():
        event.wait()



# Generated at 2022-06-14 12:16:51.922700
# Unit test for method __aexit__ of class Lock
def test_Lock___aexit__():
    lock = Lock()
    lock.release()

# Generated at 2022-06-14 12:17:00.748497
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Semaphore
    sem = Semaphore(2)
    @gen.coroutine
    def worker(worker_id):
        with (yield sem.acquire()):
            print("Worker %d is working" % worker_id)
            yield use_some_resource()

            # Now the semaphore has been released.
        print("Worker %d is done" % worker_id)
    @gen.coroutine
    def worker1(worker_id):
        with (yield sem.acquire()):
            print("Worker %d is working" % worker_id)
            yield use_some_resource()

            # Now the semaphore has been released.
        print("Worker %d is done" % worker_id)

# Generated at 2022-06-14 12:17:09.081565
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition

    condition = Condition()

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier()])

    IOLoop.current().run_sync(runner)



# Generated at 2022-06-14 12:17:16.132979
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    from tornado.locks import Semaphore
    from tornado.ioloop import IOLoop
    from tornado.concurrent import Future
    import time

    async def test1():
        # need to test this scenario when the acquire is timed out and the acquire
        # is successfully executed the next time
        sem = Semaphore(0)
        sem.release()
        await sem.acquire(timeout = time.time())
        await sem.acquire(timeout = time.time())

    IOLoop.current().run_sync(test1)

    # test method acquire when the counter is non zero
    # need to test this scenario when the acquire is timed out and the acquire
    # is successfully executed the next time
    sem = Semaphore(1)
    waiter = Future()
    if sem._value > 0:
        sem._value -= 1

# Generated at 2022-06-14 12:17:18.394276
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    condition = Condition()
    assert condition.__repr__() == '<Condition>'

# Generated at 2022-06-14 12:17:27.831267
# Unit test for method notify of class Condition
def test_Condition_notify():
    import asyncio
    condition = Condition()

    async def fun1():
        print("fun1 runing...")
        await condition.wait()
        print("fun1 done...")

    async def fun2():
        print("fun2 runing...")
        condition.notify(1)
        print("fun2 done...")

    async def main():
        await asyncio.wait([fun1(), fun2()])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()


# Generated at 2022-06-14 12:17:31.055424
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    print(condition.__repr__())
    print(condition._timeouts)
    print(condition._waiters)
    condition.notify()
    print()


# Generated at 2022-06-14 12:17:38.361238
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    # Fixture
    condition = Condition()
    waiters = []  # Waiters we plan to run right now.

    while condition._waiters:
        waiter = condition._waiters.popleft()
        if not waiter.done():  # Might have timed out.
            waiters.append(waiter)

    for waiter in waiters:
        future_set_result_unless_cancelled(waiter, True)

    # Verification
    assert len(condition._waiters) == 0


# Generated at 2022-06-14 12:18:06.889227
# Unit test for method __aexit__ of class Lock
def test_Lock___aexit__():
    ae = Lock.__aexit__
    import unittest.mock as mock

    async def _():
        i = await ae(mock.MagicMock(), mock.MagicMock(), mock.MagicMock())
        return i
    return _()

# Generated at 2022-06-14 12:18:14.152027
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    sem = Semaphore(2)
    async def worker(worker_id):
        assert await sem.acquire()
        assert sem.is_locked()
        assert await sem.acquire()
        assert sem.is_locked()
        assert await sem.acquire()
        assert sem.is_locked()

    async def test_runner():
        await worker(1)

    ioloop.IOLoop.current().run_sync(test_runner)


# Generated at 2022-06-14 12:18:16.187047
# Unit test for method set of class Event
def test_Event_set():
    event = Event()
    event.set()
    print(event.is_set())



# Generated at 2022-06-14 12:18:23.440027
# Unit test for method wait of class Condition
def test_Condition_wait():
    condition = Condition()

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier()])

    ioloop.IOLoop.current().run_sync(runner)



# Generated at 2022-06-14 12:18:26.163545
# Unit test for method wait of class Event
def test_Event_wait():
    global result
    result = Event()
    event = Event()
    event.set()
    assert event.wait(None) == None
    assert result.is_set() == True

# Generated at 2022-06-14 12:18:27.927256
# Unit test for method __aexit__ of class Semaphore
def test_Semaphore___aexit__():
    s = Semaphore()
    s.__aexit__(None, None, None)


# Generated at 2022-06-14 12:18:31.001302
# Unit test for method release of class BoundedSemaphore
def test_BoundedSemaphore_release():
    a = BoundedSemaphore(value=3)
    a.release()
    a.release()
    a.release()
    try:
        a.release()
    except:
        return False
    return True


# Generated at 2022-06-14 12:18:34.597757
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    l = Lock()
    async def test():
        async with l:
            pass
    IOLoop.current().run_sync(test)

# Generated at 2022-06-14 12:18:36.904741
# Unit test for method __aexit__ of class Lock
def test_Lock___aexit__():
    from tornado.locks import Lock
    lock = Lock()
    assert lock.__aexit__(None, None, None) is None

# Generated at 2022-06-14 12:18:40.293027
# Unit test for method wait of class Event
def test_Event_wait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Event

    event = Event()

    async def waiter():
        await event.wait()
        print ("Not waiting")
        await event.wait()
        print ("Done")

    async def setter():
        event.set()

    async def runner():
        await gen.multi([waiter(), setter()])

    IOLoop.current().run_sync(runner)



# Generated at 2022-06-14 12:19:30.180897
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    condition.notify(2)
    #condition.notify_all()
    print('===== END TEST FOR CLASS Condition =====')

test_Condition_notify()



# Generated at 2022-06-14 12:19:31.277429
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    repr(Condition())

# Generated at 2022-06-14 12:19:41.878330
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    from collections import deque
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.concurrent import Future
    from tornado.locks import Semaphore

    # Ensure reliable doctest output: resolve Futures one at a time.
    futures_q = deque([Future() for _ in range(3)])

    async def simulator(futures):
        for f in futures:
            # simulate the asynchronous passage of time
            await gen.sleep(0)
            await gen.sleep(0)
            f.set_result(None)

    IOLoop.current().add_callback(simulator, list(futures_q))
    sem = Semaphore(2)
    async def use_some_resource():
        return futures_q.popleft()

# Generated at 2022-06-14 12:19:52.072702
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")
    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), waiter()])
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(runner)
    #Condition is already empty
    condition.notify_all()
    io_loop.run_sync(runner)
    condition.notify(1)
    io_loop.run_sync(runner)
    condition.notify_all()
    io_loop.run_sync(runner)


# Generated at 2022-06-14 12:19:58.354258
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier(times):
        print("About to notify")
        for i in range(times):
            condition.notify()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier(2)])
    ioloop.IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:20:00.247494
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    waiter = condition.wait()
    
    condition.notify()
    
    assert waiter.result() == True


# Generated at 2022-06-14 12:20:04.864403
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Semaphore

    sem = Semaphore(2)

    async def worker(worker_id):
        await sem.acquire()
        try:
            print("Worker %d is working" % worker_id)
            #await use_some_resource()
        finally:
            print("Worker %d is done" % worker_id)
            sem.release()

    async def runner():
        # Join all workers.
        await gen.multi([worker(i) for i in range(3)])

    IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:20:11.524775
# Unit test for method wait of class Condition
def test_Condition_wait():
    import time
    import threading
    def run():
        threading.current_thread().name = "Test_Thread"
        for i in range(0,4):
            time.sleep(0.5)
            print("abc")
    condition = Condition()
    t1 = threading.Thread(target=run)
    t1.start()

    try:
        condition.wait()
    except Exception as e:
        print(e)

# Generated at 2022-06-14 12:20:12.644373
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    pass



# Generated at 2022-06-14 12:20:20.873067
# Unit test for method wait of class Event
def test_Event_wait():
    # the first wait blocks
    e = Event()
    result_awaitable = e.wait()
    #result = yield result_awaitable
    e.set()
    new_result_awaitable = e.wait()
    #new_result = yield new_result_awaitable
    e.clear()
    new_result_awaitable = e.wait()
    #new_result = yield new_result_awaitable
    e.set()
    new_result_awaitable = e.wait(timeout=1)
    #new_result = yield new_result_awaitable
    


# Generated at 2022-06-14 12:21:57.956664
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    # @TODO Test if method notify_all of class Condition can work.
    cond = Condition()
    cond.notify_all()



# Generated at 2022-06-14 12:22:02.110190
# Unit test for method set of class Event
def test_Event_set():
    e = Event()
    if e.is_set():
        print("set")
    else:
        print("not set")
    e.set()
    if e.is_set():
        print("set")
    else:
        print("not set")


# Generated at 2022-06-14 12:22:07.968406
# Unit test for method notify of class Condition
def test_Condition_notify():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition
    cond = Condition()
    def func():
        print("hello")
    def func1():
        print("hello1")
    async def test_Condition_notify():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([func(), func1()])
    IOLoop.current().run_sync(test_Condition_notify)
# Function to test method notify of class Condition
test_Condition_notify()


# Generated at 2022-06-14 12:22:17.328841
# Unit test for method wait of class Condition
def test_Condition_wait():
    from tornado.ioloop import IOLoop
    import tornado.locks
    import tornado.platform.asyncio
    import asyncio
    import tornado
    tornado.platform.asyncio.AsyncIOLoop().install()
    loop = asyncio.get_event_loop()
    a = tornado.locks.Condition()
    async def waiter():
        print("I'll wait right here")
        await a.wait()
        print("I'm done waiting")
    async def notifier():
        print("About to notify")
        a.notify()
        print("Done notifying")
    async def runner():
        # Wait for waiter() and notifier() in parallel
        await tornado.gen.multi([waiter(), notifier()])
    loop.run_until_complete(runner())



# Generated at 2022-06-14 12:22:29.191121
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    # we manually add the repr of the class name to a list
    class_name_repr = []

    # we need to replace Condition with a mock class, so that we can
    # intercept calls to the __repr__ method
    class MockCondition:
        def __repr__(self):
            class_name_repr.append(super().__repr__())
            return super().__repr__()

    Condition.__bases__ = (MockCondition,)

    # call code under test
    cond = Condition()

    assert len(class_name_repr) == 1

    # we split the string and take the second part. This is the class name
    assert class_name_repr[0].split()[1] == cond.__class__.__name__


# Generated at 2022-06-14 12:22:34.053806
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    print("test_Semaphore___aenter__ begin")
    asyncio.run(test_Semaphore___aenter___())
    print("test_Semaphore___aenter__ end")

async def test_Semaphore___aenter___():
    print("test_Semaphore___aenter__ inside")
    print("test_Semaphore___aenter__ inside end")


# Generated at 2022-06-14 12:22:37.312650
# Unit test for method __aexit__ of class Semaphore
def test_Semaphore___aexit__():
    assert False # TODO: implement your test here


# Generated at 2022-06-14 12:22:41.259555
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    event.set()
    @gen.coroutine
    def f():
        kk = yield event.wait()
        return kk
    res = f()
    print(res)
    # print(f().result())
test_Event_wait()


# Generated at 2022-06-14 12:22:52.136945
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    async def waiter1():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")
        return True

    async def waiter2():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")
        return True

    async def waiter3():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")
        return True

    async def waiter4():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")
        return True

    async def notifier():
        print("About to notify")
        condition.notify_all()
        print("Done notifying")


# Generated at 2022-06-14 12:22:59.842954
# Unit test for method wait of class Condition
def test_Condition_wait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition

    condition = Condition()

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier()])
    IOLoop.current().run_sync(runner)
test_Condition_wait()
