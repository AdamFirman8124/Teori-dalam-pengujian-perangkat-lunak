

# Generated at 2022-06-14 12:15:57.252958
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    # type: () -> None
    """Test for method Condition.__repr__ of class Condition""" 
    condition = Condition() # type: Condition
    assert repr(condition) == "<Condition>"
    condition.wait() # type: Future
    assert repr(condition) == "<Condition waiters[1]>"
    condition.wait() # type: Future
    condition.wait() # type: Future
    condition.wait() # type: Future
    condition.wait() # type: Future
    assert repr(condition) == "<Condition waiters[5]>"


# Generated at 2022-06-14 12:16:05.752503
# Unit test for method wait of class Condition
def test_Condition_wait():
    io_loop = ioloop.IOLoop.current()

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
    condition = Condition()
    #test_Condition_wait()
    io_loop.run_sync(runner)
#test_Condition_wait()


# Generated at 2022-06-14 12:16:14.681269
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    se = Semaphore(3)
    assert se._value == 3

    se.release()
    assert se._value == 4

    se.release()
    assert se._value == 5

    se.release()
    assert se._value == 6

    # Test that release works correctly with waiters
    waiter = Future()
    assert se._value == 6
    se._waiters.append(waiter)
    assert not waiter.done()
    assert se._value == 6

    se.release()
    assert se._value == 6
    assert waiter.done()
    assert se._value == 5

    # Test that a waiting Future is not released twice
    waiter2 = Future()
    assert se._value == 5
    se._waiters.append(waiter2)
    assert not waiter2.done()
    assert se._value == 5



# Generated at 2022-06-14 12:16:17.696237
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    s = Semaphore(0)
    fut = s.acquire()
    assert isinstance(fut, Future)
    assert isinstance(fut.result(), _ReleasingContextManager)


# Generated at 2022-06-14 12:16:23.598572
# Unit test for method set of class Event
def test_Event_set():
    E = Event()
    if E.is_set():
        print("Event is already set")
    else:
        print("Event is not set")
    E.set()
    if E.is_set():
        print("Event is already set")
    else:
        print("Event is not set")
    print("Now clearing Event")
    E.clear()
    if E.is_set():
        print("Event is already set")
    else:
        print("Event is not set")


# Generated at 2022-06-14 12:16:25.569840
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    s = Semaphore(2)
    s.release()
    val = s._value
    assert val == 3
    

# Generated at 2022-06-14 12:16:33.193014
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    c = Condition()

    def test():
        yield c.notify_all()
        print(c._waiters)  # Should be 0
        return c._waiters
    num_waiters = 3
    for _ in range(0, num_waiters):
        c._waiters.append(Future())
    print(c._waiters)
    c.io_loop.run_sync(test)



# Generated at 2022-06-14 12:16:38.805734
# Unit test for method release of class BoundedSemaphore
def test_BoundedSemaphore_release():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import BoundedSemaphore
    sem = BoundedSemaphore(value=1)
    @gen.coroutine
    def test():
        try:
            sem.release()
            assert False
        except ValueError:
            pass
    IOLoop.current().run_sync(test)

# Generated at 2022-06-14 12:16:49.173275
# Unit test for method wait of class Event
def test_Event_wait():
    """

    :return:
        >>> from tornado.locks import Event
        >>> event = Event()
        >>> 
        >>> async def a():
        ...     print('start a')
        ...     await event.wait()
        ...     print('a receives notification')
        >>> 
        >>> async def b():
        ...     print('start b')
        ...     event.set()
        ...     print('b send notification')
        >>> 
        >>> async def main():
        ...     tasks = [a(), b()]
        ...     await gen.wait(tasks)
        >>> 
        >>> ioloop.IOLoop.current().run_sync(main)
        start a
        start b
        b send notification
        a receives notification
    """



# Generated at 2022-06-14 12:16:51.981384
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    condition = Condition()
    assert repr(condition) == "<Condition>"


# Generated at 2022-06-14 12:17:05.733516
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    semaphore = Semaphore(2)
    raise NotImplementedError()


# Generated at 2022-06-14 12:17:11.597444
# Unit test for method wait of class Condition
def test_Condition_wait():
    condition = Condition()
    with gen.coroutine() as waiter:
        with gen.coroutine() as notifier:
            print('waiter started')
            print('notifier started')
            yield condition.wait()
            print('waiter done waiting')
            print('notifier done notifying')
    waiter()
    notifier()
    print('done')


# Generated at 2022-06-14 12:17:13.470380
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    cond = Condition()
    print(cond)

# Generated at 2022-06-14 12:17:15.475454
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    c = Condition()  
    print("notify_all")  
    c.notify_all() 

# Generated at 2022-06-14 12:17:18.760014
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    # notify
    condition.notify()
    # notify_all
    condition.notify_all()
    # return
    return True



# Generated at 2022-06-14 12:17:21.338086
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    sem = Semaphore()
    sem.release()

# Generated at 2022-06-14 12:17:24.735340
# Unit test for method wait of class Event
def test_Event_wait():
    # Sets the Event object e
    e = Event()
    e.set()
    # Waits for the event object e to be set
    result = e.wait()
    assert result == None
    return


# Generated at 2022-06-14 12:17:30.792156
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    f = Lock.__aenter__
    l = Lock()
    m = mock.Mock(return_value = 3)
    with mock.patch('{0}.{1}'.format(Lock.__module__, 'Lock.acquire'), new = m):
        p = f(l)
    with pytest.raises(AttributeError):
        m.assert_called_with()

# Generated at 2022-06-14 12:17:35.533902
# Unit test for method release of class Lock
def test_Lock_release():
    l = Lock()
    assert not l._block.is_set()
    l._block = Event()
    assert l._block.is_set()
    try:
        l.release()
    except ValueError:
        pass
    assert not l._block.is_set()


# Generated at 2022-06-14 12:17:37.637268
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    condition.notify_all()
    assert len(condition._waiters) == 0


# Generated at 2022-06-14 12:17:52.822825
# Unit test for method __aexit__ of class Lock
def test_Lock___aexit__():
    from tornado.locks import Lock
    lock = Lock()
    with pytest.raises(RuntimeError):
        with lock:
            pass

    async def async_with():
        async with lock:
            pass
    test_runner(async_with(), "Lock (async context manager)")


# Generated at 2022-06-14 12:17:54.724605
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    value = Semaphore()
    try:
        value.release()
    except:
        assert False

# Generated at 2022-06-14 12:18:02.203583
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    print("In test_Condition_notify_all ...")
    condition = Condition()

    # Wait for waiter() and notifier() in parallel
    IOLoop.current().run_sync(runner)

async def waiter():
    print("In waiter ...")
    await condition.wait()
    print("I'm done waiting")

async def notifier():
    print("In notifier ...")
    condition.notify_all()
    print("Done notifying")

async def runner():
    # Wait for waiter() and notifier() in parallel
    await gen.multi([waiter(), notifier()])

if __name__ == "__main__":
    print("In main ...")
    #test_Condition_notify_all()
    pass


# Generated at 2022-06-14 12:18:14.773807
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

    async def waiter1():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting")

    async def notifier1():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier(),waiter1(),notifier1()])
   

# Generated at 2022-06-14 12:18:18.738556
# Unit test for method notify of class Condition
def test_Condition_notify():
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition
    condition = Condition()
    num = 0
    condition.notify_all()
    # condition.notify(2)
    # condition.notify(3)


# Generated at 2022-06-14 12:18:21.103957
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    sema = Semaphore()
    print(sema.acquire())
    return

# Generated at 2022-06-14 12:18:29.321782
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


# Generated at 2022-06-14 12:18:37.412635
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    
    sem = Semaphore(value = 1)
    waiter = Future()  # type: Future[_ReleasingContextManager]
    waiter.set_result(None)
    if (sem._value > 0) :
        sem._value -= 1
        waiter.set_result(_ReleasingContextManager(sem))
    else:
        sem._waiters.append(waiter)
        if (timeout != None) :
            def on_timeout() -> None:
                if (not (waiter.done())) :
                    waiter.set_exception(gen.TimeoutError())
                sem._garbage_collect()
            io_loop = ioloop.IOLoop.current()
            timeout_handle = io_loop.add_timeout(timeout, on_timeout)

# Generated at 2022-06-14 12:18:39.078902
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    """Test for  release method of class Semaphore"""
    sem = Semaphore(2)
    expected = 2
    actual = sem._value
    assert actual == expected


# Generated at 2022-06-14 12:18:47.168821
# Unit test for method wait of class Event
def test_Event_wait():
    # Prepare test data
    class Future(object):
        def __init__(self):
            self.value = False
        def done(self):
            return self.value
        def set_result(self, value):
            self.value = value
        def add_done_callback(self, func):
            self.value = func(self.value)
        def cancel(self):
            self.value = False
    f = Future()
    f.value = False
    e = Event()
    e._value = True
    e._waiters={f}
    # Test method wait of class Event
    timeout = None
    assert e.wait(timeout) == f
    assert e.is_set()
    assert f.value == None
    assert e._waiters == {f}
    print('test_Event_wait passed!')


# Generated at 2022-06-14 12:19:03.914534
# Unit test for method set of class Event
def test_Event_set():
    abc = Event()
    assert abc._value == False
    abc.set()
    assert abc._value == True


# Generated at 2022-06-14 12:19:10.947151
# Unit test for method wait of class Event
def test_Event_wait():

    from tornado.ioloop import IOLoop
    from utils.locks import Event

    event = Event()

    async def waiter():
        print("Waiting for event")
        await event.wait()
        print("Not waiting this time")
        await event.wait()
        print("Done")

    async def setter():
        print("About to set the event")
        # Set the event
        event.set()

    async def runner():
        # Wait for waiter() and setter() in parallel
        await gen.multi([waiter(), setter()])

    IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:19:23.353833
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition

    condition = Condition()

    async def f1():
        print('I\'m f1')
        await condition.wait()
        print('I\'m f1 got notify')

    async def f2():
        print('I\'m f2')
        await condition.wait()
        print('I\'m f2 got notify')

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([f1(), f2()])
        condition.notify_all()
        print('Done notifying')

    IOLoop.current().run_sync(runner)
if __name__ == '__main__':
    test_Condition_notify_all()


# Generated at 2022-06-14 12:19:32.091508
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    waiters = []
    # _waiters is of type Deque
    for i in range(0, 20):
        waiters.append(Future())
    semaphore = Semaphore(value=20)
    semaphore._waiters = deque(waiters)
    # Semaphore.acquire() is defined as a coroutine
    result = semaphore.acquire()
    # Calling the method acquire with a timeout is an error
    with pytest.raises(RuntimeError):
        result = semaphore.acquire(timeout=0)
    # Calling the method acuire without a timeout, return a Future object
    assert result == Future()


# Generated at 2022-06-14 12:19:35.693047
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    coro = event.wait()
    if isinstance(coro, Future):
        print("Future!")
    else:
        print("Not a Future!")


# Generated at 2022-06-14 12:19:38.911667
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    sem = Semaphore(2)
    assert sem._value == 2
    sem.release()
    assert sem._value == 3
    sem.release()
    assert sem._value == 4



# Generated at 2022-06-14 12:19:42.849492
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    waiters = [condition.wait() for _ in range(3)]
    condition.notify_all()
    io_loop.run_sync(lambda: gen.multi(waiters))



# Generated at 2022-06-14 12:19:44.712020
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    # Lock_case_001
    lock = Lock()
    await lock.acquire()
    lock.release()


# Generated at 2022-06-14 12:19:47.840489
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    lock = Lock()
    print(repr(lock))
    #async def f():
    #    async with lock:
    #        print(lock)
    #    print(lock)

    #IOLoop.current().run_sync(f)
    
    

# Generated at 2022-06-14 12:19:52.939475
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    waiters = [condition.wait() for i in range(3)]
    condition.notify(2)
    condition.notify_all()
    condition.notify()


# Generated at 2022-06-14 12:20:19.047463
# Unit test for method notify of class Condition
def test_Condition_notify():
    import asyncio
    from tornado.ioloop import IOLoop
    from tornado.locks import Lock, Condition, Event

    def test_condition_notify(self):
        # test notify
        self.flag = False
        self.num = 0
        self.lock = Lock()

        def worker():
            for _ in range(5):
                self.lock.acquire()
                self.num += 1
                self.lock.release()
            self.flag = True
            self.condition.notify()

        self.condition = Condition()
        self.event = Event()

        # run a worker thread
        asyncio.new_event_loop().run_in_executor(None, worker)

        @gen.coroutine
        def f():
            yield self.condition.wait()
            self.event.set()

# Generated at 2022-06-14 12:20:25.210470
# Unit test for method __repr__ of class Semaphore
def test_Semaphore___repr__():
    assert Semaphore(value=0).__repr__() == "<Semaphore [locked]>"
    assert Semaphore(value=1).__repr__() == "<Semaphore [unlocked,value:1]>"
    assert Semaphore(value=2).__repr__() == "<Semaphore [unlocked,value:2]>"

    # when waiters is not empty
    s = Semaphore(value=1)
    assert s.__repr__() == "<Semaphore [unlocked,value:1]>"

    # when waiters is empty
    s = Semaphore(value=0)
    assert s.__repr__() == "<Semaphore [locked]>"



# Generated at 2022-06-14 12:20:28.894163
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    from tornado.locks import Semaphore
    sem = Semaphore(2)
    try:
        await sem.__aenter__()
    except RuntimeError as e:
        assert True
    else:
        assert False



# Generated at 2022-06-14 12:20:30.724081
# Unit test for method release of class Lock
def test_Lock_release():
    print("release")
    lock = Lock()
    i = 0
    try:
        lock.release()
        i+=1
    except RuntimeError:
        pass
    assert(i == 0)
    
    

# Generated at 2022-06-14 12:20:39.577018
# Unit test for method wait of class Event
def test_Event_wait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Event
    import time
    import random
    event = Event()
    def waiter():
        print("Waiting for event")
        yield event.wait()
        print("Not waiting this time")
        yield event.wait()
        print("Done")
    def setter():
        print("About to set the event")
        event.set()
    loop = IOLoop.current()
    loop.add_callback(waiter)
    loop.add_callback(lambda: setter())
    loop.start()
# test_Event_wait()



# Generated at 2022-06-14 12:20:41.318154
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    sem = Semaphore(0)
    assert(sem.release() == None)

# Generated at 2022-06-14 12:20:46.875548
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():

    lock = Lock()
    async def async_test():
        with pytest.raises(RuntimeError) as excinfo:
            lock.__aenter__()
        assert str(excinfo.value) == "Use 'async with' instead of 'with' for Lock"
    ioloop.IOLoop.current().run_sync(async_test)


# Generated at 2022-06-14 12:20:54.143217
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()

    async def waiter():
        print("Waiting for event")
        try:
            await event.wait(timeout=datetime.timedelta(seconds=1))
            print("Not waiting this time")
        except gen.TimeoutError as e:
            print("Time out")
        print("Done")

    async def setter():
        print("About to set the event")
        event.set()

    async def runner():
        await gen.multi([waiter(), setter()])

    ioloop.IOLoop.current().run_sync(runner)


# Generated at 2022-06-14 12:20:56.437880
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    lock = Lock()
    async def worker():
        async with lock:
            pass



# Generated at 2022-06-14 12:20:57.469908
# Unit test for method __aexit__ of class Lock
def test_Lock___aexit__():
    pass


# Generated at 2022-06-14 12:21:14.629288
# Unit test for method notify of class Condition
def test_Condition_notify():
    waiters = []
    c = Condition()
    for _ in range(3):
        waiters.append(c.wait())
    c.notify(1)
    f1 = gen.multi(waiters)
    ioloop.IOLoop.current().run_sync(f1)



# Generated at 2022-06-14 12:21:17.301955
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    c = Condition()
    assert(not c)
    assert(len(c) == 0)
    c.notify()
    c.notify()
    assert(c)
    assert(len(c) == 2)


# Generated at 2022-06-14 12:21:20.697402
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    """Test Semaphore class"""
    sem = Semaphore(1)
    await sem.__aenter__()
    await sem.__aenter__()
    await sem.__aenter__()
    await sem.__aenter__()

# Generated at 2022-06-14 12:21:32.845219
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    
    from unittest import TestCase
    from unittest.mock import patch
    import tornado.ioloop

    class TestSemaphore(TestCase):
        def setUp(self):
            self.semaphore = Semaphore()

        def test_acquire(self):
            # Test with timeout
            waiter = Future() 
            self.semaphore._value = 0
            self.semaphore._waiters.append(waiter)
            # future should not be done
            expected = False
            actual = waiter.done()
            assert expected == actual
            # assert identity of waiter
            expected = waiter
            actual = self.semaphore._waiters.popleft()
            assert expected == actual
            # Test with no timeout
            waiter = Future() 
            self.semaphore._value = 1
            #

# Generated at 2022-06-14 12:21:36.991842
# Unit test for method notify of class Condition
def test_Condition_notify():
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
        await gen.multi([waiter(), notifier()])

    ioloop.IOLoop.current().run_sync(runner)

# Generated at 2022-06-14 12:21:46.504440
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    import tornado
    import tornado.ioloop
    import tornado.concurrent
    import tornado.locks
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
        await tornado.gen.multi([waiter(), setter()])

    tornado.ioloop.IOLoop.current().run_sync(runner)



# Generated at 2022-06-14 12:21:53.406797
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    try:
        # For both Lock and BoundedSemaphore
        lock = Lock()
        lock.__aenter__()
    except Exception as e:
        import sys
        import traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        formatted_lines = traceback.format_exc().splitlines()
        print(formatted_lines)
        while exc_traceback:
            frame = exc_traceback.tb_frame
            lineno = exc_traceback.tb_lineno
            filename = frame.f_code.co_filename
            linecache.checkcache(filename)
            line = linecache.getline(filename, lineno, frame.f_globals)

# Generated at 2022-06-14 12:22:02.533970
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



# Generated at 2022-06-14 12:22:03.098264
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    pass

# Generated at 2022-06-14 12:22:10.066087
# Unit test for method notify of class Condition
def test_Condition_notify():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Condition

    condition = Condition()

    async def waiter1():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting 1")

    async def waiter2():
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting 2")

    async def notifier():
        print("About to notify")
        condition.notify(n=1)
        condition.notify(n=1)
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter1(), waiter2(), notifier()])

    IOLoop.current().run_sync(runner)

# Unit test

# Generated at 2022-06-14 12:22:41.214583
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    waiters = []
    waiters.append(condition.wait())
    waiters.append(condition.wait())
    waiters.append(condition.wait())
    waiters.append(condition.wait())
    condition.notify(3)
    print(waiters)



# Generated at 2022-06-14 12:22:48.824482
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

# Generated at 2022-06-14 12:22:52.746633
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    """Test method __aenter__ of class Lock"""

    # Constructor test
    lock = locks.Lock()

    # Method __aenter__ test
    lock.__aenter__()



# Generated at 2022-06-14 12:22:56.829723
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    # if the lock is unlocked, acquire it and return the lock
    lock = Lock()
    assert lock.__aenter__() == lock

    # if the lock is already locked, wait until it is unlocked
    lock = Lock()
    lock.acquire()
    with pytest.raises(RuntimeError):
        lock.acquire()


# Generated at 2022-06-14 12:23:05.481672
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


# Generated at 2022-06-14 12:23:14.330405
# Unit test for method wait of class Event
def test_Event_wait():
    def test():
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

    test()



# Generated at 2022-06-14 12:23:21.595819
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    def waiter(condition):
        print('I"ll wait right here')
        condition.wait()
        print('Im done waiting')
    def notifier(condition):
        print('About to notify')
        condition.notify()
        print('Done notifying')
    waiter(condition)
    notifier(condition)
# test_Condition_notify()



# Generated at 2022-06-14 12:23:30.119535
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    # Lock.__aenter__() -> None
    # x is Lock
    __test_yielded__ = set()
    __test_coroutine_stack__ = []
    __test_coroutine_started__ = False
    __test_coroutine_exception__ = None
    __test_yielded__.add("acquire")
    __test_coroutine_stack__.append(("acquire", None, ("x", ), {"timeout", }, None))
    __test_coroutine_started__ = True
    try:
        __test_coroutine_returned__ = x.acquire()
    except Exception as __test_coroutine_exc__:
        __test_coroutine_exception__ = __test_coroutine_exc__
    else:
        __test_coroutine_exception__ = None

# Generated at 2022-06-14 12:23:36.851030
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():

    # FIXME: this test is wrong.
    # It tests a local function if its assert is true,
    # otherwise it tests the __aenter__ method of class Semaphore.
    # It should be the other way around.
    async def __aenter__(self) -> None:
        await self.acquire()
    assert False



# Generated at 2022-06-14 12:23:42.061938
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from tornado.concurrent import Future
    from tornado.locks import BoundedSemaphore
    from tornado.locks import Lock
    from unittest.mock import call
    from unittest.mock import MagicMock
    from unittest.mock import patch
    from unittest.mock import sentinel
    from unittest.mock import create_autospec
    from unittest.mock import mock_open
    from asyncio import coroutine
    from typing import Any
    import pytest
    import sys

    class MockFuture(Future):
        """A mock Future.

        Returns the value passed to ``set_result()``.
        """

        def __init__(self, result, exception=None):
            Future.__init__(self)
            self.result = result
            self.exception = exception



# Generated at 2022-06-14 12:24:42.316244
# Unit test for method notify of class Condition
def test_Condition_notify():
    c = Condition()
    future = c.wait()
    ioloop.IOLoop.current().call_later(0.01, c.notify)
    result = ioloop.IOLoop.current().run_sync(lambda: future)
    assert(result)

test_Condition_notify()



# Generated at 2022-06-14 12:24:49.334493
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    io_loop = ioloop.IOLoop.current()
    
    sem = Semaphore(0)
    # Test if acquire blocks on initial value 0
    time_start = time.time()
    acquired = sem.acquire()
    
    # Acquire another time
    sem.acquire()
    # Release once
    sem.release()
    # Test if acquire unblocks
    acquired.result()
    time_end = time.time()
    # Test if acquire did block
    if time_end - time_start < 1:
        raise Exception('Test for class Semaphore on method acquire failed')
    
    sem = Semaphore(1)
    # Test if acquire doesn't block on initial value 1
    time_start = time.time()
    acquired = sem.acquire()
    time_end = time.time()

# Generated at 2022-06-14 12:24:53.032025
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    from tornado.locks import Condition

    condition = Condition()
    assert repr(condition) == '<Condition>'
    condition._waiters.append(1)
    assert repr(condition) == "<Condition waiters[1]>"



# Generated at 2022-06-14 12:25:01.370382
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    async def waite():
        print("I'm waiting right here")
        await condition.wait()
        print("I'm done waiting")
    async def notifi():
        await gen.sleep(1)
        print("I'm notifying")
        condition.notify_all()
        print("Done notifying")
    ioloop.IOLoop.current().run_sync(asyncio.gather(waite(), notifi()))
    # Output:
    # I'm waiting right here
    # I'm notifying
    # Done notifying
    # I'm done waiting


# Generated at 2022-06-14 12:25:02.424877
# Unit test for method set of class Event
def test_Event_set():
    assert 1 == 1


# Generated at 2022-06-14 12:25:05.299214
# Unit test for method notify of class Condition
def test_Condition_notify():
    """
    Test cases for method notify of class Condition
    """
    condition = Condition()
    waiter = condition.wait()
    waiter.result()
    condition.notify()

# Generated at 2022-06-14 12:25:07.180630
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    condition = Condition()
    assert condition.__repr__() == "<Condition>"


# Generated at 2022-06-14 12:25:12.195601
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    import asyncio
    lock = Lock()
    coro = asyncio.coroutine(lock.__aenter__())
    try:
        coro.send(None)
    except StopIteration as exc:
        assert exc.value is None
    except RuntimeError:
        pass

# Generated at 2022-06-14 12:25:14.420490
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    def _(cond: Condition) -> str:
        return cond.__repr__()
    cond = Condition()
    assert '<Condition' in _(cond)


# Generated at 2022-06-14 12:25:15.307138
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    s = Semaphore()

