

# Generated at 2022-06-14 12:15:57.111202
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
# test_Condition_wait()



# Generated at 2022-06-14 12:16:05.292940
# Unit test for method notify of class Condition
def test_Condition_notify():
    c = Condition()
    print("c.wait(timeout=10) was returned to let the main thread wait 10 seconds")
    print(c.wait(timeout=10))
    fut = Future()
    print("fut.set_result(True) was called to let the main thread continue")
    fut.set_result(True)
    print("fut was passed to c.notify(n=1) to wake up the main thread, so the program terminates")
    c.notify(n=1)
    print("fut:", fut)
#test_Condition_notify()



# Generated at 2022-06-14 12:16:09.286396
# Unit test for method wait of class Event
def test_Event_wait():
    evt = Event()
    f = evt.wait(timeout=datetime.timedelta(seconds=1))
    f.add_done_callback(lambda fut: fut.result())
    ioloop.IOLoop.current().start()


# Generated at 2022-06-14 12:16:14.956159
# Unit test for method wait of class Event
def test_Event_wait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Event

    event = Event()

    async def waiter():
        print("Waiting for event")
        await event.wait()
        print("Not waiting this time")
        await event.wait()
        print("Done")

    async def setter():
        print("About to set the event")
        event.set()

    async def runner():
        await gen.multi([waiter(), setter()])

    IOLoop.current().run_sync(runner)
#test_Event_wait()



# Generated at 2022-06-14 12:16:20.298008
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    from tornado import gen
    import asyncio
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition
    from tornado.platform.asyncio import to_asyncio_future
    loop = IOLoop.current()
    condition = Condition()
    @gen.coroutine
    def waiter():
        print('I will wait')
        yield condition.wait()
        print('I am done waiting')
    @gen.coroutine
    def notifier():
        print('About Notifying')
        condition.notify_all()
        print('Done Notifying')
    loop.add_callback(lambda: loop.spawn_callback(waiter))
    loop.add_callback(lambda: loop.spawn_callback(waiter))
    loop.call_later(3, lambda: loop.spawn_callback(notifier))
    loop

# Generated at 2022-06-14 12:16:21.444315
# Unit test for method __aexit__ of class Semaphore
def test_Semaphore___aexit__():
    semaphore = Semaphore(0)
    with pytest.raises(AssertionError):
        assert next(semaphore._value)

# Generated at 2022-06-14 12:16:26.353973
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    sem = Semaphore(2)
    async def worker(worker_id):
        print("worker_id",worker_id)
        async with sem:
            print("Worker %d is working" % worker_id)
            await gen.sleep(0)
    # Join all workers.
    ioloop.IOLoop.current().run_sync(lambda : gen.multi([worker(i) for i in range(3)]))



# Generated at 2022-06-14 12:16:29.562648
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    condition.notify()
    assert(condition.n == 1)


# Generated at 2022-06-14 12:16:31.940238
# Unit test for method notify of class Condition
def test_Condition_notify():
    cond = Condition()
    cond.notify()
    cond.notify(2)
    cond.notify_all()


# Generated at 2022-06-14 12:16:40.481585
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    scheduler = Scheduler(asyncio.get_event_loop())
    n = 10
    sem1 = Semaphore(10)
    sem2 = Semaphore(0)
    scheduler.add_task(sem1.release, None, name="Semaphore.release")
    scheduler.add_task(sem1.release, None, name="Semaphore.release")
    scheduler.add_task(sem1.release, None, name="Semaphore.release")
    scheduler.add_task(sem1.release, None, name="Semaphore.release")
    scheduler.add_task(sem1.release, None, name="Semaphore.release")
    scheduler.add_task(sem1.release, None, name="Semaphore.release")

# Generated at 2022-06-14 12:17:01.934297
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()

    def foo():
        print("I'm foo")
        condition.notify()
        print("Done notifying")

    def bar():
        print("I'll wait right here")
        condition.wait()
        print("I'm done waiting")

    def runner():
        # Wait for foo() and bar() in parallel
        return gen.multi([foo(), bar()])

    ioloop.IOLoop.current().run_sync(runner)



# Generated at 2022-06-14 12:17:06.398560
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    sem = Semaphore(2)
    print("Test for method release of class Semaphore")
    print("Before release, value = {}".format(sem._value))
    sem.release()
    print("After release, value = {}".format(sem._value))

# Generated at 2022-06-14 12:17:12.671990
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Semaphore
    sem = Semaphore(2)
    async def worker(worker_id):
        async with sem:
            print("Worker %d is working" % worker_id)
        print("Worker %d is done" % worker_id)
    async def runner():
        await gen.multi([worker(i) for i in range(3)])
    IOLoop.current().run_sync(runner)
test_Semaphore___aenter__()

# Generated at 2022-06-14 12:17:21.624657
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    from random import randint
    from types import TracebackType
    from typing import Any, Generator, Optional, Type
    from unittest import TestCase
    import asyncio
    from tornado.locks import Semaphore
    from asyncio import AbstractEventLoop
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    mys = Semaphore()
    await mys.__aenter__()
    print(mys._waiters)
    

test_Semaphore___aenter__()

# Generated at 2022-06-14 12:17:31.605289
# Unit test for method wait of class Condition
def test_Condition_wait():
    condition = Condition()
    @gen.coroutine
    def waiter(condition):
        print("I'll wait right here")
        r = yield condition.wait()
        print("I'm done waiting")
        return r
    @gen.coroutine
    def notifier(condition):
        print("About to notify")
        condition.notify()
        print("Done notifying")
    @gen.coroutine
    def runner(condition):
        # Wait for waiter() and notifier() in parallel
        yield gen.multi([waiter(condition), notifier(condition)])
    result = ioloop.IOLoop.current().run_sync(lambda :runner(condition))
    print(result)


# Generated at 2022-06-14 12:17:34.700458
# Unit test for method set of class Event
def test_Event_set():
    event = Event()
    assert event.is_set() == False
    event.set()
    assert event.is_set() == True


# Generated at 2022-06-14 12:17:36.531914
# Unit test for method set of class Event
def test_Event_set():
    event = Event()
    event.set()
    print("\n")


# Generated at 2022-06-14 12:17:43.901744
# Unit test for method notify of class Condition
def test_Condition_notify():
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



# Generated at 2022-06-14 12:17:45.925503
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    condition = Condition()
    ret = condition.__repr__()
    assert isinstance(ret, str)


# Generated at 2022-06-14 12:17:54.677913
# Unit test for method wait of class Event
def test_Event_wait():
    async def waiter(event, timeout):
        try:
            await event.wait(timeout)
            print("wait")
        except Exception as e:
            print("not wait", e)

    # set the event before wait, so wait will not block
    event = Event()
    event.set()
    # timeout is 1 second
    timeout = datetime.timedelta(seconds=1)
    waiter(event, timeout)

# test for method waitof class Event
# now we only test the cases when event is set
# the cases when event is not set will be tested in the testing to test is_set
test_Event_wait()

# Generated at 2022-06-14 12:18:07.262543
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    assert event.wait() == None


# Generated at 2022-06-14 12:18:16.234987
# Unit test for method wait of class Event
def test_Event_wait():
    print("----------Test in Event------------")
    event = Event()

    @gen.coroutine
    def waiter():
        print("Waiting for event")
        yield event.wait()
        print("Not waiting this time")
        yield event.wait()
        print("Done")

    @gen.coroutine
    def setter():
        print("About to set the event")
        event.set()

    @gen.coroutine
    def runner():
        yield [waiter(), setter()]
    loop = IOLoop.instance()
    loop.run_sync(runner)
#test_Event_wait()


# Generated at 2022-06-14 12:18:19.559883
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    import asyncio
    condition= Condition()
    result=None
    async def waiter():
        nonlocal result
        result=await condition.wait()
    async def notifier():
        condition.notify_all()
    async def main():
        nonlocal result
        await asyncio.gather(waiter(),notifier())
        print(result)
    asyncio.run(main())

# Generated at 2022-06-14 12:18:28.172519
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    print("**************start test of Semaphore_release**************")
    # Create three workers
    async def worker(worker_id):
        await sem.acquire()
        try:
            print("Worker %d is working" % worker_id)
            await use_some_resource()
        finally:
            print("Worker %d is done" % worker_id)
            sem.release()

    async def runner():
        # Join all workers.
        await gen.multi([worker(i) for i in range(3)])

    IOLoop.current().run_sync(runner)

    print("**************end test of Semaphore_release**************")

# Generated at 2022-06-14 12:18:30.201081
# Unit test for method notify of class Condition
def test_Condition_notify():
    x = Condition()
    y = Condition()
    runner = y.wait()
    x.notify()


# Generated at 2022-06-14 12:18:37.314956
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    print("test for method acquire of class Semaphore")
    async def test_acquire_async(test_sem):
        await test_sem.acquire()
        print("Test acquire works")

    loop = asyncio.get_event_loop()
    test_sem = Semaphore()
    loop.run_until_complete(test_acquire_async(test_sem))


# Generated at 2022-06-14 12:18:41.110632
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    def check():
        if event.is_set():
            event.wait()
    # Check the code path where the event is set
    event.set()
    check()
    # Check the code path where the event is not set
    event.clear()
    check()

# Generated at 2022-06-14 12:18:45.539320
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    from unittest.mock import Mock
    value = Mock()
    # Call method
    assert Semaphore().__aenter__() == Mock(), "Did not call method correctly"
    # Check call count of mock
    assert value.acquire.call_count == 1, "Method was called unexpected amount of times"

# Generated at 2022-06-14 12:18:54.074311
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    def get_futures_q():
        from collections import deque
        from tornado.concurrent import Future
        futures_q = deque([Future() for _ in range(10)])
        return futures_q

    sem = Semaphore(4)

    futures_q = get_futures_q()

    @gen.coroutine
    def worker(worker_id):
        with (yield sem.acquire()):
            print("Worker %d is working" % worker_id)
            yield use_some_resource()

        # Now the semaphore has been released.
        print("Worker %d is done" % worker_id)

    async def runner():
        # Join all workers.
        await gen.multi([worker(i) for i in range(10)])

    IOLoop.current().run_sync

# Generated at 2022-06-14 12:18:56.558651
# Unit test for method notify of class Condition
def test_Condition_notify():
    c = Condition()
    f = c.wait()
    assert not f.done()
    c.notify()
    assert f.done()
    assert f.result()



# Generated at 2022-06-14 12:19:18.018389
# Unit test for method set of class Event
def test_Event_set():
    event = Event()  # type: Event
    assert event.is_set() == False
    event.set()
    assert event.is_set() == True

# Generated at 2022-06-14 12:19:21.791401
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    from tornado.locks import Condition
    from tornado.ioloop import IOLoop
    from tornado import gen

    condition = Condition()
    with gen.coroutine():
        assert condition.__repr__() == '<Condition>'

# Generated at 2022-06-14 12:19:24.130765
# Unit test for method __aexit__ of class Semaphore
def test_Semaphore___aexit__():
    c = Semaphore()
    c._value = 0
    c._waiters = None
    # Test TypeError raised
    with pytest.raises(RuntimeError) as e:
        c.__aexit__('type','value','trace')
        assert 'Use' in str(e)
    # Test other case
    c._value = 1
    assert c.__aexit__(None,None,None) == None

# Generated at 2022-06-14 12:19:27.040061
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    '''
    Test method __repr__
    '''
    cond = Condition()
    print(cond)

# Generated at 2022-06-14 12:19:29.209734
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    sem = Semaphore()
    if(sem.value_ == 0):
        assert sem.release() == 0


# Generated at 2022-06-14 12:19:32.022200
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from tornado import gen
    from tornado.locks import Lock
    lock = Lock()
    async def f():
        async with lock:
            # Do something holding the lock.
            pass

        # Now the lock is released.



# Generated at 2022-06-14 12:19:35.008022
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    event.wait()
    event.wait(timeout=1)
    event.wait(timeout=datetime.timedelta(seconds=1))



# Generated at 2022-06-14 12:19:38.414708
# Unit test for method release of class BoundedSemaphore
def test_BoundedSemaphore_release():
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        sem = BoundedSemaphore(value=1)
        sem.release()
        sem.release()


# Generated at 2022-06-14 12:19:42.690521
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    cond = Condition()
    assert repr(cond) == "<Condition>"
    cond.wait()
    cond.wait()
    assert repr(cond) == "<Condition waiters[2]>"


# Generated at 2022-06-14 12:19:45.468869
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    sem = Semaphore()
    sem.acquire()
    # test time out
    sem.acquire(timeout=datetime.timedelta(seconds=1))
    sem.acquire(timeout=1)

# Generated at 2022-06-14 12:20:16.203519
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    cond = Condition()
    assert repr(cond) == "<Condition>"
    cond.notify()
    assert repr(cond) == "<Condition>"
    cond.wait()
    assert repr(cond) == "<Condition waiters[1]>"
    cond.wait()
    assert repr(cond) == "<Condition waiters[2]>"
    assert cond.wait().done()
    assert repr(cond) == "<Condition waiters[1]>"
    assert cond.wait().done()
    assert repr(cond) == "<Condition waiters[0]>"



# Generated at 2022-06-14 12:20:20.253365
# Unit test for method __aexit__ of class Lock
def test_Lock___aexit__():
    class Lock(object):
        def __aexit__(self, typ, value, tb):
            pass
    obj = Lock()
    result = obj.__aexit__('typ', 'value', 'tb')
    assert result == None, 'result is None'

# Generated at 2022-06-14 12:20:32.050329
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
        finally:
            print("Worker %d is done" % worker_id)
            sem.release()

    async def runner():
        # Join all workers.
        await gen.multi([worker(i) for i in range(3)])

    IOLoop.current().run_sync(runner)
test_Semaphore_acquire()
test_Semaphore_acquire()
test_Semaphore_acquire()
test_Semaphore_acquire()



# Generated at 2022-06-14 12:20:39.982562
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    semaphore = Semaphore(3)
    assert semaphore._value == 3
    assert len(semaphore._waiters) == 0
    for n in range(4):
        semaphore.release()
        assert semaphore._value == 4
        assert len(semaphore._waiters) == 0
    semaphore.release()
    assert semaphore._value == 5
    assert len(semaphore._waiters) == 0
    semaphore = Semaphore(0)
    assert semaphore._value == 0
    assert len(semaphore._waiters) == 0
    for n in range(4):
        semaphore.release()
        assert semaphore._value == n + 1
        assert len(semaphore._waiters) == 0
    semaphore.release()
    assert sem

# Generated at 2022-06-14 12:20:45.343833
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()

    async def waiter():
        print("Waiting for event")
        await event.wait()
        print("Not waiting this time")
        await event.wait()
        print("Done")

    io_loop = ioloop.IOLoop.current()

    io_loop.run_sync(waiter)
    assert True



# Generated at 2022-06-14 12:20:50.186887
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    print(condition, condition._waiters)
    #condition.wait()
    condition.notify()
    print(condition, condition._waiters)
    condition.notify_all()
    print(condition, condition._waiters)

#test_Condition_notify()
# A lock is basically a condition that also provides exclusive access.
Lock = Condition

# Generated at 2022-06-14 12:20:53.248591
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    sem = Semaphore(0)
    sem.release()
    assert sem._value == 1
    sem.release()
    assert sem._value == 2
    sem.release()
    assert sem._value == 3


# Generated at 2022-06-14 12:21:02.751707
# Unit test for method wait of class Condition
def test_Condition_wait():
    import pytest
    from tornado import gen
    from tornado.ioloop import IOLoop

    @gen.coroutine
    def waiter():
        print("I'll wait right here")
        yield condition.wait()
        print("I'm done waiting")

    @gen.coroutine
    def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    @gen.coroutine
    def runner():
        # Wait for waiter() and notifier() in parallel
        yield [waiter(), notifier()]

    condition = Condition()
    pytest.run_in_thread(IOLoop.current().run_sync, runner)


Event = Condition  # For backwards compatibility.



# Generated at 2022-06-14 12:21:06.111164
# Unit test for method __aexit__ of class Semaphore
def test_Semaphore___aexit__():
    # callable objects
    semaphore: Semaphore = Semaphore(
        value=3,
    )
    semaphore.__aexit__(
        typ=None,
        value=None,
        tb=None,
    )
    assert type(semaphore) is Semaphore
    assert semaphore._value == 4
    assert semaphore._waiters == deque([])

# Generated at 2022-06-14 12:21:07.843103
# Unit test for method release of class Lock
def test_Lock_release():
    with pytest.raises(RuntimeError):
        Lock().release()



# Generated at 2022-06-14 12:21:31.902932
# Unit test for method __aexit__ of class Semaphore
def test_Semaphore___aexit__():

    sem = Semaphore(2)
    async def worker(worker_id):
        async with sem:
            print("Worker %d is working" % worker_id)
        # Now the semaphore has been released.
        print("Worker %d is done" % worker_id)

    asyncio.run(worker(1))



# Generated at 2022-06-14 12:21:32.506157
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    pass

# Generated at 2022-06-14 12:21:35.593357
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    # An instance of Semaphore
    sem_0 = Semaphore()
    # The return type of the method
    rt_0 = type(None)
    assert rt_0 == Semaphore.__aenter__(sem_0)



# Generated at 2022-06-14 12:21:45.559329
# Unit test for method __repr__ of class Semaphore
def test_Semaphore___repr__():
    sem = Semaphore(2)

    async def worker(worker_id):
        await sem.acquire()
        try:
            print("Worker %d is working" % worker_id)
            await use_some_resource()
        finally:
            print("Worker %d is done" % worker_id)
            sem.release()

    async def runner():
        # Join all workers.
        await gen.multi([worker(i) for i in range(3)])

    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(runner)
    



# Generated at 2022-06-14 12:21:50.522627
# Unit test for method set of class Event
def test_Event_set():

    event = Event()

    async def waiter():
        print("Waiting for event")
        await event.wait()
        print("Not waiting this time")
        await event.wait()
        print("Done")

    async def setter():
        print("About to set the event")
        event.set()

    async def runner():
        await gen.multi([waiter(), setter()])

    ioloop.IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:21:53.796119
# Unit test for method release of class BoundedSemaphore
def test_BoundedSemaphore_release():
    sem = BoundedSemaphore(1)
    sem.release() # return None
    sem.release() # return ValueError



# Generated at 2022-06-14 12:22:02.755302
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


# Generated at 2022-06-14 12:22:08.376661
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    loop = IOLoop()
    loop.make_current()
    try:
        semaphore = Semaphore(1)
        asyncio.Task(semaphore.acquire())
        assert semaphore._value == 0
        assert len(semaphore._waiters) == 1
        semaphore.release()
        asyncio.Task(semaphore.acquire())
        assert semaphore._value == 0
        assert len(semaphore._waiters) == 2
    finally:
        loop.close()



# Generated at 2022-06-14 12:22:15.321495
# Unit test for method wait of class Condition
def test_Condition_wait():
    @gen.coroutine
    def runner():
        condition = Condition()
        async def waiter():
            print("I'll wait right here")
            await condition.wait()
            print("I'm done waiting")
        async def notifier():
            print("About to notify")
            condition.notify()
            print("Done notifying")
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier()])
    ioloop.IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:22:24.547689
# Unit test for method wait of class Condition
def test_Condition_wait():
    conditions = Condition()
    print(dir(conditions))
    print('\n')
    ioloop.IOLoop.current().run_sync(conditions.wait)
    print('\n')
    for name in dir(conditions):
        if name.startswith('_'):
            continue
        attr = getattr(conditions, name)
        if getattr(attr, "__doc__", None):
            print(name, attr.__doc__)
    # print('\n')
    # print(conditions.__dict__)
    print('\n')
    print(conditions._waiters)
