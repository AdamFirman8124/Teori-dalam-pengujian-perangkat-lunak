

# Generated at 2022-06-14 12:15:55.253826
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    pass



# Generated at 2022-06-14 12:15:57.504982
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    with pytest.raises(ValueError):
        semaphore=Semaphore( -1)


# Generated at 2022-06-14 12:16:02.017706
# Unit test for method __repr__ of class Semaphore
def test_Semaphore___repr__():
    import string,random,time
    #Prepare
    #This is a really stupid way to generate a random string
    random_string=lambda n: ''.join([random.choice(string.ascii_letters+string.digits) for i in range(n)])
    #This function return a Semaphore object whose value is random
    def init_Semaphore(max_value=10):
        return Semaphore(random.randint(1,max_value))
    #Test
    sem=init_Semaphore()
    assert eval(repr(sem))==sem


# Generated at 2022-06-14 12:16:07.636244
# Unit test for method release of class BoundedSemaphore
def test_BoundedSemaphore_release():
    sem = BoundedSemaphore(value=1)
    sem.release()
    try:
        sem.release()
    except ValueError as e:
        assert "Semaphore released too many times" in str(e)
        print("ValueError test passed")
        return
    raise AssertionError("ValueError test failed")



# Generated at 2022-06-14 12:16:13.115043
# Unit test for method wait of class Event
def test_Event_wait():
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
        yield gen.multi([waiter(), setter()])

    ioloop.IOLoop.current().run_sync(runner)

    # Output:
    # Waiting for event
    # About to set the event
    # Not waiting this time
    # Done



# Generated at 2022-06-14 12:16:13.731736
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    assert True

# Generated at 2022-06-14 12:16:18.577618
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    # Testing for method release of class Semaphore
    sem = Semaphore(0)
    waiter = Future()
    sem._waiters.append(waiter)
    sem.release()
    assert waiter.done()
    assert isinstance(waiter.result(), _ReleasingContextManager)


# Generated at 2022-06-14 12:16:24.371795
# Unit test for method wait of class Condition
def test_Condition_wait():
    import tornado
    import tornado.gen
    import tornado.locks
    import tornado.ioloop

    async def async_main(
        _io_loop: tornado.ioloop.IOLoop = None
    ):
        wait_future = Condition().wait()

    # start the IOLoop, and run the async_main function.
    tornado.ioloop.IOLoop.current().run_sync(async_main)

    # TODO: How can I write a unit test for this???


# Generated at 2022-06-14 12:16:28.253029
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    sem = Semaphore(2)

    async def worker(worker_id):
        async with sem:
            print("Worker %d is working" % worker_id)
            await use_some_resource()

        # Now the semaphore has been released.
        print("Worker %d is done" % worker_id)

    sem.__aenter__()



# Generated at 2022-06-14 12:16:38.189961
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


# Generated at 2022-06-14 12:16:54.629220
# Unit test for method wait of class Condition
def test_Condition_wait():
    async def run():
        condition = Condition()
        condition._waiters = collections.deque()
        condition._timeouts = 0
        waiters = []
        for i in range(10):
            waiter = Future()
            waiters.append(waiter)
            condition._waiters.append(waiter)

        condition.notify(5)

        for i in range(len(waiters)):
            assert waiters[i].done() == (i < 5)



# Generated at 2022-06-14 12:17:02.641841
# Unit test for method wait of class Condition
def test_Condition_wait():
    import sys
    io_loop = ioloop.IOLoop.current()
    sys.path.append('../')
    from tornado.gen import Return
    from tornado.locks import Condition
    from tornado import gen

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


    io_loop.run_sync(runner)

Event = Condition

# Generated at 2022-06-14 12:17:07.216366
# Unit test for method wait of class Condition
def test_Condition_wait():
    import time
    import threading
    # ------------------------------------------------------------------------------------
    def worker():
        time.sleep(1)
        print('Worker notify')
        condition.notify()
    # ------------------------------------------------------------------------------------
    condition = Condition()
    threading.Thread(target=worker).start()
    print('Main wait')
    condition.wait()


# Generated at 2022-06-14 12:17:15.109966
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():

    import unittest
    import sys 
    print_orig = sys.stdout
    stderr_orig = sys.stderr

    try:  
        from io import StringIO

        sys.stdout = StringIO()
        sys.stderr = StringIO()

        from tornadowrapper import Condition

        a = Condition()
        b = repr(a)
        assert(b == "<Condition>")
    finally:
        sys.stdout = print_orig
        sys.stderr = stderr_orig


# Generated at 2022-06-14 12:17:25.197673
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


# Generated at 2022-06-14 12:17:36.438672
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    from tornado.ioloop import IOLoop
    from tornado.locks import Semaphore
    sem = Semaphore(2)
    @asyncio.coroutine
    def worker(worker_id):
        print('worker_id={}'.format(worker_id))
        yield from gen.sleep(0.5)
        print('Worker {} is working'.format(worker_id))
        yield from gen.sleep(0.5)
        sem.release()
        print('Worker {} is done'.format(worker_id))
    @asyncio.coroutine
    def runner():
        # Join all workers.
        yield from gen.multi([worker(i) for i in range(3)])
    IOLoop.current().run_sync(runner)

# Generated at 2022-06-14 12:17:41.135482
# Unit test for method wait of class Condition
def test_Condition_wait():
    # Test case: yield condition.wait(short_timeout)
    # Expected: to the next iteration of the current IOLoop
    async def _waiter():
        print("I'll wait right here")
        await condition_wait.wait()
        print("I'm done waiting")

    globals()["condition_wait"] = Condition()
    runner = _waiter()
    runner.send(None)

# Generated at 2022-06-14 12:17:42.001038
# Unit test for method set of class Event
def test_Event_set():
    pass


# Generated at 2022-06-14 12:17:47.976493
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    # Test for method __aenter__(self) of class Semaphore
    # Testing for proper working of method for a Semaphore with value of 1
    ioloop.IOLoop.current().run_sync(lambda: Semaphore(1).__aenter__())

    # Testing for proper working of method for a Semaphore with value of 0
    ioloop.IOLoop.current().run_sync(lambda: Semaphore(0).__aenter__())


# Generated at 2022-06-14 12:17:57.093443
# Unit test for method notify of class Condition
def test_Condition_notify():
    # create an object of class Condition
    cond = Condition()
    # get the waiters number
    wnum1 = len(cond._waiters)
    print('waiters number before notify: %s' % wnum1)
    # notify
    cond.notify(1)
    # get the waiters number again
    wnum2 = len(cond._waiters)
    print('waiters number after notify: %s' % wnum2)
    # check if it releases the lock
    if wnum1 != wnum2:
        print('notify success!')
    else:
        print('notify error!')

# Test for constructor of class Condition

# Generated at 2022-06-14 12:18:16.799338
# Unit test for method notify of class Condition
def test_Condition_notify():
    cond = Condition()

    @gen.coroutine
    def print_after_notify():
        yield cond.wait()
        print('Notified!')

    @gen.coroutine
    def notify():
        yield gen.sleep(1)
        print('Notifying...')
        cond.notify()

    @gen.coroutine
    def main():
        yield gen.multi([
            print_after_notify(),
            notify()
        ])

    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)

if __name__ == '__main__':
    from tornado.testing import AsyncTestCase, gen_test

    test_Condition_notify()

# Generated at 2022-06-14 12:18:19.904099
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    # Unit test for method __aenter__ of class Semaphore
    _done = False
    async def _test(_self):
        nonlocal _done
        _done = True
    __aenter___instance = Semaphore()
    __aenter___instance.__aenter__()
    _test(__aenter___instance)
    assert _done



# Generated at 2022-06-14 12:18:22.455934
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    lock = Lock()
    res = lock.__aenter__()
    assert res == None
    lock.release()
    assert lock._block._value == 1


# Generated at 2022-06-14 12:18:30.877520
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    type_error = None
    try:
        sem = Semaphore(1)
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
    except TypeError as e:
        type_error = e
    assert type_error == None

# Generated at 2022-06-14 12:18:33.808820
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    from tornado.locks import Condition
    condition = Condition()
    condition.__repr__()

# Generated at 2022-06-14 12:18:43.271434
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    inst = Semaphore(0)
    try:
        with (await inst.acquire()) as _ReleasingContextManager:
            pass
    except Exception as e:
        if e is not None:
            if type(e) is ValueError:
                assert e.args[0] == "semaphore initial value must be >= 0", \
                    "unexpected Semaphore.__aenter__ error message"
            else:
                raise Exception(
                    "unexpected Semaphore.__aenter__ exception type: %s" % (
                        type(e),
                    )
                )


    inst = Semaphore(0)

# Generated at 2022-06-14 12:18:52.241920
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    import pytest
    from tornado.locks import Semaphore
    # Test Case 1: Call to release with 
    #              _value = 0, number of waiters = 0
    # Expected Output: None
    s = Semaphore(0)
    s.release()
    assert s._value == 1
    # Test Case 2: Call to release with 
    #              _value = 1, number of waiters = 5 
    #              and the waiter list having Futures with 
    #              cancelled and not cancelled
    # Expected Output: None
    s._value = 1
    f1 = Future()
    f1.cancel()
    f2 = Future()
    f3 = Future()
    f4 = Future()
    f4.cancel()
    f5 = Future()

# Generated at 2022-06-14 12:18:55.103835
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    condition = Condition()
    condition._waiters = collections.deque([123, 456])
    assert repr(condition) == '<Condition waiters[2]>'


# Generated at 2022-06-14 12:19:01.502369
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()

    # Start waiting for notifications.
    async def waiter():
        await condition.wait()
        print("I'm done waiting")

    # Notify all the waiters.
    async def notifier():
        print("About to notify")
        condition.notify_all()
        print("Done notifying")

    # Wait for waiter() and notifier() in parallel.
    async def runner():
        await gen.multi([waiter(), notifier()])

    ioloop.IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:19:07.452854
# Unit test for method wait of class Event
def test_Event_wait():
    import time
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Event

    event = Event()
    event.set()
    def set():
        event.set()
    @gen.coroutine
    def waiter():
        start = time.time()
        yield event.wait()
        print(time.time() - start)
    @gen.coroutine
    def runner():
        yield gen.multi([waiter()])

    IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:19:28.830006
# Unit test for method acquire of class Semaphore

# Generated at 2022-06-14 12:19:33.816354
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Semaphore
    sem = Semaphore(2)
    def setter():
        sem.release()
    def waiter(worker_id):
        sem.acquire()
        print("Worker %d is working" % worker_id)
        return True
    async def runner():
        await gen.multi([setter(), waiter(1)])
    IOLoop.current().run_sync(runner)



# Generated at 2022-06-14 12:19:37.450910
# Unit test for method __aexit__ of class Semaphore
def test_Semaphore___aexit__():
    sem = Semaphore()
    loop = asyncio.get_event_loop()
    async def main():
        async with sem:
            pass
    loop.run_until_complete(main())


# Generated at 2022-06-14 12:19:42.518581
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from tornado.locks import Lock
    
    # Test raises type error for unexpected types
    try:
        Lock().__aenter__(name = 'str')
    except TypeError:
        pass
    else:
        raise AssertionError


# Generated at 2022-06-14 12:19:45.274908
# Unit test for method set of class Event
def test_Event_set():
    event = Event()
    assert event.is_set() == False

    event.set()
    assert event.is_set() == True

    event.clear()
    assert event.is_set() == False


# Generated at 2022-06-14 12:19:54.776726
# Unit test for method wait of class Condition
def test_Condition_wait():
    import tornado.ioloop
    import tornado.gen

    cond = Condition()

    @gen.coroutine
    def waiter():
        print("I'll wait right here")
        yield cond.wait()
        print("I'm done waiting")

    @gen.coroutine
    def notifier():
        print("About to notify")
        cond.notify()
        print("Done notifying")

    @gen.coroutine
    def runner():
        # Wait for waiter() and notifier() in parallel
        yield tornado.gen.multi([waiter(), notifier()])

    tornado.ioloop.IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:20:01.334146
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

# Generated at 2022-06-14 12:20:03.028816
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():

    with pytest.raises(RuntimeError):
        Semaphore().__enter__()



# Generated at 2022-06-14 12:20:05.727014
# Unit test for method release of class BoundedSemaphore
def test_BoundedSemaphore_release():
    # Create a BoundedSemaphore with value 1
    m = BoundedSemaphore(value = 1)
    # Call release 1 time correctly
    m.release()
    # Call release 2 times
    # Should raise ValueError
    try:
        m.release()
        m.release()
        print("ERROR: Call release 2 times, but don't raise ValueError")
    except ValueError:
        print("OK: Call release 2 times and raise ValueError")

# Generated at 2022-06-14 12:20:09.577814
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    s = Semaphore()
    assert s._value == 1
    s.acquire()
    assert s._value == 0
    s.release()
    assert s._value == 1
    

# Generated at 2022-06-14 12:20:29.524459
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    global Condition
    Condition = Condition()
    assert(isinstance(Condition.__repr__(), str))
    

# Generated at 2022-06-14 12:20:37.147795
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    from tornado.locks import Semaphore
    import asyncio as asyncio
    import tornado
    import tornado.ioloop
    import tornado.queues
    import concurrent.futures
    import concurrent.futures
    import threading

    # ---------- ---------- ---------- ---------- ----------
    # Setup
    # ---------- ---------- ---------- ---------- ----------
    def on_timeout():
        raise RuntimeError('test timed out')

    timeout_handle = tornado.ioloop.IOLoop.current().call_later(
        5, on_timeout)

    S1 = Semaphore(1)
    S2 = Semaphore(value=2)

    def test(op1,op2,op3):
        import tornado.ioloop
        import asyncio as asyncio
        import concurrent.futures


# Generated at 2022-06-14 12:20:39.823120
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    """Unit test for method __aenter__ of class Lock"""
    from tornado import locks
    lock = locks.Lock()
    lock.acquire()
    lock.release();



# Generated at 2022-06-14 12:20:45.199505
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    _waiters = collections.deque()  # type: Deque[Future[bool]]
    _timeouts = 0
    self = Condition()
    self._waiters = _waiters
    self._timeouts = _timeouts
    result = repr(self)
    assert result == "<Condition waiters[0]>"

# Generated at 2022-06-14 12:20:47.544343
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    a = Lock()
    a.__aenter__()
    a.__aexit__(None, None, None)



# Generated at 2022-06-14 12:20:55.703936
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition
    
    def f():
        pass
    
    def g():
        pass
    
    def h():
        pass
    
    def i():
        pass
    
    async def async_1():
        condition.wait()
        return True
    
    async def async_2():
        await condition.wait()
        return True
    
    def test_1():
        # Test __repr__
        assert(repr(Condition()) == "<Condition>")
        assert(repr(Condition()) == "<Condition>")
        asyncio_loop = asyncio.get_event_loop()
        io_loop_1 = IOLoop.current()
        io_loop_2 = IOLoop()
        condition_1 = Condition()
        condition_2

# Generated at 2022-06-14 12:20:56.449076
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
	pass

# Generated at 2022-06-14 12:21:03.152037
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    from tornado.ioloop import IOLoop
    loop = IOLoop.current()
    c = Condition()

    @gen.coroutine
    def f():
        yield c.wait()
        print("hello")

    @gen.coroutine
    def g():
        print("here")
        c.notify_all()

    @gen.coroutine
    def h():
        yield [f(), g()]

    loop.run_sync(h)
#test_Condition_notify_all()


# Generated at 2022-06-14 12:21:04.033936
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    a = Semaphore()
    a.release()


# Generated at 2022-06-14 12:21:12.355097
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
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

    IOLoop.current().run_sync(runner)