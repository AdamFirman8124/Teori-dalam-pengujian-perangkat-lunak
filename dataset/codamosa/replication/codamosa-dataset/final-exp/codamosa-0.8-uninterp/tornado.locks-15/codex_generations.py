

# Generated at 2022-06-14 12:16:11.934352
# Unit test for method wait of class Condition
def test_Condition_wait():

    import datetime

    cond = Condition()
    print('cond:', cond)

    async def test_waiter(num: int, timeout: Optional[Union[float, datetime.timedelta]] = None):
        print('Waiter-%s wait: %s' % (num, timeout))
        res = await cond.wait(timeout=timeout)
        print('Waiter-%s done: %s' % (num, res))

    async def test_notifier():
        print('Notifier... waitting')
        await gen.sleep(3)
        print('Notifier... Notifying')
        cond.notify()
        await gen.sleep(3)
        print('Notifier... Notifying all')
        cond.notify_all()

    async def test():
        print('Running test')
        loop = ioloop.I

# Generated at 2022-06-14 12:16:22.234463
# Unit test for method notify of class Condition
def test_Condition_notify():
  import unittest
  import asyncio
  import time
  import tornado
  from tornado.httpclient import AsyncHTTPClient
  import tornado.gen
  import tornado.ioloop
  from tornado.locks import Condition
  from tornado.platform.asyncio import to_asyncio_future
  from tornado.platform.asyncio import to_tornado_future
  from tornado.testing import AsyncTestCase
  from tornado.testing import gen_test
  import tornado.platform.asyncio
  import asyncio
  import uvloop
  # We must monkeypatch asyncio to use EventLoopPolicy
  # for tornado.platform.asyncio.BaseAsyncIOLoop.

  #asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy()) # @TODO : bug here
  #asyncio.

# Generated at 2022-06-14 12:16:28.711580
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    global cnt
    cnt = 0
    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")
    async def notifier():
        print("About to notify")
        condition.notify_all()
        print("Done notifying")
    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier()])
    condition = Condition()
    while(cnt < 4):
        IOLoop.current().run_sync(runner)
        cnt = cnt + 1

test_Condition_notify_all()

# Generated at 2022-06-14 12:16:33.949557
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    import tornado.ioloop
    sem = Semaphore()
    ioloop.IOLoop.current().make_current()
    import asyncio
    async def test():
        async with sem as x:
            assert x is None
    try:
        asyncio.run(test())
    finally:
        tornado.ioloop.IOLoop.clear_current()


# Generated at 2022-06-14 12:16:40.328038
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


# Generated at 2022-06-14 12:16:44.581732
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from unittest import TestCase
    from unittest.mock import patch
    from .locks import Lock
    mock_acquire = patch('Lock.acquire', return_value=None)
    mock_acquire.start()
    with TestCase.assertRaises(TestCase, NotImplementedError):
        lock = Lock()
        lock.acquire()
        try:
            lock.__aenter__()
        except NotImplementedError:
            raise NotImplementedError
    mock_acquire.stop()


# Generated at 2022-06-14 12:16:52.607703
# Unit test for method wait of class Event
def test_Event_wait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    import time
    import logging
    import sys
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    event = Event()
    async def waiter():
        logging.debug("Waiting for Event")
        await event.wait()
        logging.debug("Not waiting this time")
        await event.wait()
        logging.debug("Done")

    async def setter():
        logging.debug("About to set the event")
        event.set()
        logging.debug("About to set the event again")
        event.set()

    async def runner():
        await gen.multi([waiter(), setter()])

    IOLoop.current().run_sync(runner)
    # Output:
    # DEBUG:root:Waiting for Event

# Generated at 2022-06-14 12:16:54.603319
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    import tornado
    import tornado.locks as locks
    lock = locks.Lock()
    result = lock.__aenter__()
    assert result == None


# Generated at 2022-06-14 12:16:56.239831
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    C = Condition()
    assert repr(C) == "<Condition>"
test_Condition___repr__()

# Generated at 2022-06-14 12:16:57.471675
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    with pytest.raises(RuntimeError):
        Lock().__aenter__()

# Generated at 2022-06-14 12:17:12.886733
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():

    cond = Condition()
    assert str(cond) == "<Condition>"

    cond.wait()
    assert str(cond) == "<Condition waiters[1]>"


# Generated at 2022-06-14 12:17:20.912170
# Unit test for method wait of class Event
def test_Event_wait():
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


# Generated at 2022-06-14 12:17:28.033408
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    import pytest
    # We mock the ioloop.IOLoop.current() function because the function it returns depends on the specific thread. 
    # We mock it here because tests are run not in the main thread
    # TODO: How to mock yield?
    new_acquire = Semaphore(1)
    new_acquire.release()
    if new_acquire.acquire() == None:
        assert True
        
    else:
        assert False


# Generated at 2022-06-14 12:17:39.021356
# Unit test for method wait of class Condition
def test_Condition_wait():
    @gen.coroutine
    def wait_test_coro(condition) -> None:
        print("I'll wait right here")
        yield condition.wait()
        assert True
        print("I'm done waiting")

    # Unit test for method notify of class Condition
    @gen.coroutine
    def notify_test_coro(condition) -> None:
        print("About to notify")
        condition.notify()
        assert True
        print("Done notifying")

    @gen.coroutine
    def runner_test_coro() -> None:
        # Wait for waiter() and notifier() in parallel
        condition = Condition()
        yield [wait_test_coro(condition), notify_test_coro(condition)]

    ioloop.IOLoop.current().run_sync(runner_test_coro)
# Unit test

# Generated at 2022-06-14 12:17:40.904247
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from tornado import locks
    lock = locks.Lock()
    lock.__aenter__()
    assert True, "Shouldn't raise"

# Generated at 2022-06-14 12:17:46.309457
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    sem = Semaphore(2)
    assert sem._value == 2
    sem.release()
    assert sem._value == 3
    sem.release()
    assert sem._value == 4
    path = "test_Semaphore_release.txt"
    with open (path, "w") as f:
        f.write("test_Semaphore_release: pass\n")


# Generated at 2022-06-14 12:17:57.189051
# Unit test for method __aexit__ of class Semaphore
def test_Semaphore___aexit__():
    class MockSemaphore(Semaphore):
        # create a mock object to simulate a Semaphore object
        def __init__(self):
            Semaphore.__init__(self, 1)
            self.release_called = False

        def release(self):
            self.release_called = True
            Semaphore.release(self)

    def provide_MockSemaphore() -> MockSemaphore:
        return MockSemaphore()
    mock_sema = provide_MockSemaphore()
    # mock the Semaphore.acquire method
    mock_sema.acquire = lambda: gen.sleep(0)
    ioloop.IOLoop.current().run_sync(lambda: mock_sema.__aexit__(None, None, None))
    assert mock_sema.release_called

# Generated at 2022-06-14 12:18:07.966137
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
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



# Generated at 2022-06-14 12:18:10.526153
# Unit test for method release of class BoundedSemaphore
def test_BoundedSemaphore_release():
    from tornado.locks import BoundedSemaphore
    sem = BoundedSemaphore(value=0)
    sem.release()

# Generated at 2022-06-14 12:18:13.543917
# Unit test for method notify of class Condition
def test_Condition_notify():
    semaphore = Condition()
    count = 0
    def waiter():
        print("I'll wait right here")
        semaphore.wait()
        print("I'm done waiting")
    def notifier():
        print("About to notify")
        semaphore.notify()
        print("Done notifying")
    def runner():
        loop = ioloop.IOLoop.current()
        loop.add_callback(waiter)
        loop.add_callback(notifier)
    ioloop.IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:18:34.309922
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
            # await use_some_resource()
        finally:
            print("Worker %d is done" % worker_id)
            sem.release()

    async def runner():
        # Join all workers.
        await gen.multi([worker(i) for i in range(3)])

    IOLoop.current().run_sync(runner)
test_Semaphore_acquire()


# Generated at 2022-06-14 12:18:41.828703
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    sem = Semaphore(5)
    assert(sem.is_locked())
    sem.acquire()
    sem.acquire()
    sem.acquire()
    sem.acquire()
    sem.acquire()
    assert(sem.is_locked())
    sem.release()
    assert(sem.is_locked())
    sem.release()
    assert(sem.is_locked())
    sem.release()
    assert(sem.is_locked())
    sem.release()
    assert(sem.is_locked())
    sem.release()
    assert(not sem.is_locked())


# Generated at 2022-06-14 12:18:50.834501
# Unit test for method notify of class Condition
def test_Condition_notify():
    class TestCondition(Condition):
        pass
    test_condition = TestCondition()
    #Test wait function doesn't accept invalid timeout argument
    waiter_test_1 = test_condition.wait(timeout=datetime.datetime(1,1,1,0,0,0,0))
    waiter_test_1.add_done_callback(lambda _: print('waiter_test_1 throws an exception'))
    waiter_test_2 = test_condition.wait(timeout=datetime.timedelta(seconds=1))
    waiter_test_2.add_done_callback(lambda _: print('waiter_test_2 is notified'))
    test_condition.notify(n=1)
    test_condition.notify_all()

# Generated at 2022-06-14 12:18:52.162744
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from tornado import locks
    lock = locks.Lock()
    pass

# Generated at 2022-06-14 12:19:00.577162
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
if __name__ == "__main__":
    test_Condition_wait()


# Generated at 2022-06-14 12:19:08.543301
# Unit test for method notify of class Condition
def test_Condition_notify():
    from tornado import gen
    from tornado.ioloop import IOLoop

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


# Generated at 2022-06-14 12:19:20.107151
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    import tornado.locks
    import tornado.testing
    import tornado.testing

    lock = tornado.locks.Lock()
    # test that Lock.__aenter__ can be called even if the lock is already
    #  in a locked state
    with lock:
        async def coroutine(lock):
            assert lock is not None

            async with lock:
                pass

        tornado.testing.gen_test(coroutine(lock))

    # test that Lock.__aexit__ is called when exception is raised during
    #  acquisition
    lock = tornado.locks.Lock()
    with lock:
        async def coroutine(lock):
            assert lock is not None

            try:
                async with lock:
                    raise tornado.testing.gen_test.StreamClosedError()
            except tornado.testing.gen_test.StreamClosedError:
                pass

# Generated at 2022-06-14 12:19:31.381195
# Unit test for method notify of class Condition
def test_Condition_notify():
    from tornado.locks import Condition, Semaphore
    import time
    import math
    import datetime
    condition = Condition()

    def my_func():
        return True

    async def waiter(i: int) -> int:
        print("I'll wait right here", i)
        await condition.wait()
        print("I'm done waiting", i)
        return i


    async def notifier(i: int) -> None:
        print("About to notify",i)
        condition.notify()
        print("Done notifying",i)
    async def waiter_with_timeout(i: int) -> None:
        print("waiter_with_timeout", i, "start")
        await condition.wait(datetime.timedelta(seconds = i))
        print("waiter_with_timeout", i, "end")

   

# Generated at 2022-06-14 12:19:34.576712
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    lock = Lock()
    fut = lock.acquire()
    fut2 = lock.acquire()

    async def test():
        async with lock:
            lock.release()
            print("finished")

    loop = ioloop.IOLoop.current()
    loop.add_future(test(), lambda x: loop.stop())

    loop.start()



# Generated at 2022-06-14 12:19:36.349581
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    assert event.is_set() == False


# Generated at 2022-06-14 12:20:14.157520
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


# Generated at 2022-06-14 12:20:16.675089
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    def waiter():
        print('waiter start')
        condition.wait()
        print('waiter end')

    g1 = gen.coroutine(waiter)
    g2 = gen.coroutine(waiter)
    
    ioloop.IOLoop.current().run_sync(lambda: gen.multi([g1(), g2()]))
    condition.notify_all()


# Generated at 2022-06-14 12:20:24.760578
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    from tornado.locks import Semaphore
    from tornado.concurrent import Future
    from tornado.ioloop import IOLoop
    from tornado import gen
    from time import time
    #print('start Semaphore...')
    sem = Semaphore(0)
    io_loop = IOLoop.current()
    #print('io_loop:', io_loop)
    value = 0
    waiters = set()  # type: Set[Future[None]]
    waiter = Future()
    if value > 0:
        value -= 1
        waiter.set_result(_ReleasingContextManager(sem))
    else:
        waiters.add(waiter)
        #timeout = 5
        timeout = 0.5
        #print('timeout:', timeout)

# Generated at 2022-06-14 12:20:31.408529
# Unit test for method wait of class Event
def test_Event_wait():
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

# Generated at 2022-06-14 12:20:33.638336
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    cons=Condition()
    l=[]
    for i in range(100):
        l.append(i)
    for item in l:
        item.wait()



# Generated at 2022-06-14 12:20:45.784945
# Unit test for method notify of class Condition
def test_Condition_notify():
    from tornado.locks import Condition
    from tornado.gen import coroutine, Task
    from tornado.ioloop import IOLoop
    # Set timeout_timestamp.
    timeout_timestamp = 0.
    # Set n.
    n = 0
    # Set waiters.
    waiters = []
    # Set waiters_pop.
    waiter_pop = 0
    # Set waiter.
    waiter = 0
    # Set waiters_append.
    waiters_append = 0
    # Set waiters_loop.
    waiters_loop = []
    # Set done_status.
    done_status = True
    # Set timeout_handle.
    timeout_handle = 0
    # Set c.
    c = Condition()
    assert len(c._waiters) == 0
    # Set futures.
    futures = []
   

# Generated at 2022-06-14 12:20:47.688069
# Unit test for method notify of class Condition
def test_Condition_notify():
    cond = Condition()
    cond.notify()
    cond.notify_all()



# Generated at 2022-06-14 12:20:50.965540
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    import sys
    import unittest
    class Test_Semaphore_release(unittest.TestCase):
        def test_release(self):
            import tornado
            import tornado.locks
            sem = tornado.locks.Semaphore()
            self.assertEqual(sem._value,1)
            self.assertEqual(sem._waiters,[])
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Semaphore_release)
    unittest.TextTestRunner(verbosity=2).run(suite)


# Generated at 2022-06-14 12:21:02.045883
# Unit test for method wait of class Condition
def test_Condition_wait():
    async def demo():
        # wait() waits for notify() to be called in some other coroutine.
        condition = Condition()
        async def waiter(name):
            # wait() may be called with a timeout, making it easy to implement
            # a timeout for an operation.
            print("I'll wait right here")
            await condition.wait(timeout=ioloop.IOLoop.current().time() + 1)
            print("done waiting %s" % name)

        async def notifier():
            # Notifications are not lost if a coroutine calls notify() while
            # no coroutines are waiting; in this case, the next coroutine to
            # wait() will be woken up.
            print("About to notify")
            condition.notify()
            print("Done notifying")

        # Wait for waiter() to finish, or for 1 second to

# Generated at 2022-06-14 12:21:05.216580
# Unit test for method notify of class Condition
def test_Condition_notify():
    c = Condition()
    c.notify()
    c.notify(n=10)
    c.notify_all()
    return True


# Generated at 2022-06-14 12:21:59.953100
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    lock = Lock()
    async def f():
        return await lock.__aenter__()
    assert f() == None

# Generated at 2022-06-14 12:22:07.409947
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    # The method is only used when using the semaphore in an async context with
    # Python >= 3.5, so no need to test it in other Python versions.
    if sys.version_info < (3, 5):
        return

    sem = Semaphore()
    loop = get_event_loop()

    async def test_with():
        with pytest.raises(gen.TimeoutError):
            await gen.with_timeout(timedelta(milliseconds=1), sem.acquire())
        async with sem:
            pass
        async with sem:
            pass
    loop.run_sync(test_with)



# Generated at 2022-06-14 12:22:14.980433
# Unit test for method notify of class Condition
def test_Condition_notify():
    import typing
    import tutil
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition

    async def waiter(name: str, condition: Condition):
        print(f"waiter {name} wait for notify")
        await condition.wait()
        print(f"waiter {name} received notify")

    async def notifier(condition: Condition):
        await gen.sleep(2)
        for i in range(3):
            print(f"notifier notify {i} times")
            condition.notify(i+1)
            await gen.sleep(2)

    condition = Condition()
    IOLoop.current().run_sync(lambda: gen.multi([waiter('1', condition), waiter('2', condition), waiter('3', condition), notifier(condition)]))


# Generated at 2022-06-14 12:22:17.746386
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    s=Semaphore(1)
    from queue import LifoQueue
    s._waiters=LifoQueue()
    s._waiters.put(None)
    s.release()


# Generated at 2022-06-14 12:22:21.388012
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    lock = Lock()

    # __aenter__ = async def __aenter__(self)
    assert callable(lock.__aenter__)
    assert lock.__aenter__() is None

# Generated at 2022-06-14 12:22:28.680451
# Unit test for method wait of class Condition
def test_Condition_wait():
    # test for class Condition
    condition = Condition()
    io_loop = ioloop.IOLoop.current()

    # Wait up to 1 second for a notification.
    waitrs = condition.wait(timeout=io_loop.time() + 1)
    assert waitrs == False
    condition.notify()
    waitrs = condition.wait(timeout=io_loop.time() + 1)
    assert waitrs == True




# Generated at 2022-06-14 12:22:32.094663
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    s = Semaphore(1)

    count = 0
    for i in range(0, 10):
        count += 1
        s.release()

    assert count == 10
    # print("Test method release of class Semaphore: Passed")


# Generated at 2022-06-14 12:22:39.983450
# Unit test for method wait of class Event
def test_Event_wait():
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


# Generated at 2022-06-14 12:22:42.488865
# Unit test for method __repr__ of class Semaphore
def test_Semaphore___repr__():
  # TODO: This is likely to be a false positive.
  raise SkipTest('Unit test not yet implemented.')


# Generated at 2022-06-14 12:22:47.164462
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    future = Future()
    lock = Lock()
    coro = lock.__aenter__()
    assert isinstance(coro, coroutine)
    assert isinstance(coro, Awaitable)
    future.set_result(None)
    result = IOLoop.current().run_sync(coro)
    assert result is None


# Generated at 2022-06-14 12:24:41.948055
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    condition = Condition()
    assert type(condition) == Condition
    assert len(repr(condition))>10


# Generated at 2022-06-14 12:24:44.809462
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    try:
        cond=Condition()
        cond.notify_all()
    except:
        return False
    return True
# Test: Condition -> notify_all



# Generated at 2022-06-14 12:24:54.449367
# Unit test for method wait of class Condition
def test_Condition_wait():
    e = Condition()

    def _wait(timeout):
        return e.wait(timeout)
    _wait.__name__ = "wait"
    e._wait = _wait

    def _notify():
        e.notify()
    _notify.__name__ = "notify"
    e._notify = _notify

    @gen.coroutine
    def f():
        yield e.wait()

    @gen.coroutine
    def g():
        yield e.notify()

    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(lambda: gen.multi([f(), g()]))



# Generated at 2022-06-14 12:25:02.764179
# Unit test for method wait of class Event
def test_Event_wait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Event

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

    IOLoop.current().run_sync(runner)
test_Event_wait()



# Generated at 2022-06-14 12:25:06.978116
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    S = Semaphore(2)
    assert S._value == 2
    S.release()
    assert S._value == 3
    S.release()
    assert S._value == 4
    S.release()
    assert S._value == 5


# Generated at 2022-06-14 12:25:11.010040
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from tornado import locks
    lock = locks.Lock()
    gen_test.assert_true(asyncio.iscoroutinefunction(lock.acquire), "method async Lock.acquire should return coroutine function")

# Generated at 2022-06-14 12:25:12.992540
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    future1 = Future()
    gen_test(Semaphore._ReleasingContextManager.__aenter__, future1)



# Generated at 2022-06-14 12:25:16.134891
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    # expected threshold value
    expected = 0
    # actual threshold value
    actual = len(self._waiters)
    # check if the actual value equals to expected value
    if expected == actual:
        return True
    else:
        return False


# Generated at 2022-06-14 12:25:20.458899
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    A = Lock()
    B = Lock()
    C = Lock()

    assert A is not B
    assert A is not C
    assert B is not C

    assert A.__aenter__() == B.__aenter__() == C.__aenter__()

# Generated at 2022-06-14 12:25:27.794939
# Unit test for method notify of class Condition
def test_Condition_notify():
    async def notify(condition):
        await condition.wait()
        print('notify condition')
        #await gen.sleep(0.01)
        print('finish notify condition')
    async def waiter(condition):
        print('Start waiting')
        await condition.wait()
        print('finish waiting')
    condition = Condition()
    loop = ioloop.IOLoop.current()
    loop.spawn_callback(notify,condition)
    loop.spawn_callback(waiter,condition)
    loop.call_later(0.02,lambda : condition.notify())
    loop.start()
