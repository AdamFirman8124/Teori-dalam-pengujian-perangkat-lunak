

# Generated at 2022-06-14 12:16:01.861086
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    Condition.notify_all()



# Generated at 2022-06-14 12:16:08.144414
# Unit test for method wait of class Event
def test_Event_wait():
    from tornado.ioloop import IOLoop
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
    IOLoop.current().run_sync(setter)
    IOLoop.current().run_sync(waiter)

# Generated at 2022-06-14 12:16:11.762139
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    from tornado.locks import Semaphore
    semaphore = Semaphore(2)
    semaphore._value = 0
    semaphore._waiters = deque([Future(), Future(), Future()])
    semaphore.release()
    # can't find consistent test result
    # todo

# Generated at 2022-06-14 12:16:13.779412
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
  semaphore = Semaphore()
  fut = Future()
  fut.set_result(None)
  semaphore._value = 1
  semaphore._waiters = deque()
  semaphore._value = 0
  return



# Generated at 2022-06-14 12:16:17.891873
# Unit test for method wait of class Event
def test_Event_wait():
    event = Event()
    print("Event has been set", event.is_set())
    event.clear()
    print("Event has been cleared", event.is_set())
    event.set()
test_Event_wait()


# Generated at 2022-06-14 12:16:20.028162
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    @gen.coroutine
    def call_notify_all():
        res = condition.notify_all()
        raise gen.Return(res)
    result = IOLoop.current().run_sync(call_notify_all)
    assert result == None


# Generated at 2022-06-14 12:16:26.633951
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



# Generated at 2022-06-14 12:16:28.197636
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    lock = Lock()
    async def f2():
        async with lock:
            lock.release()

    f2().close()


# Generated at 2022-06-14 12:16:28.905128
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    pass


# Generated at 2022-06-14 12:16:35.490440
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()

    async def waiter():
        await condition.wait()
        print("I'm done waiting")

    async def notifier():
        print("About to notify")
        condition.notify()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(), notifier()])

    # runner()
        
if __name__ == "__main__":
    test_Condition_notify()
    


# Generated at 2022-06-14 12:17:01.789988
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    assert len(condition._waiters) == 0
    condition.notify_all()
    assert len(condition._waiters) == 0



# Generated at 2022-06-14 12:17:07.297152
# Unit test for method release of class BoundedSemaphore
def test_BoundedSemaphore_release():
    x = BoundedSemaphore(value = 1)
    x.release()
    try:
        x.release()
    except ValueError:
        print("ValueError: Semaphore released too many times")
    else:
        print("Error: Expected exception not thrown")

test_BoundedSemaphore_release()


# Generated at 2022-06-14 12:17:11.125837
# Unit test for method __aexit__ of class Semaphore
def test_Semaphore___aexit__():
    sem = Semaphore()
    with pytest.raises(RuntimeError):
        with sem:
            pass
    result = sem.__aexit__()
    assert result is None
    assert sem._value == 1

# Generated at 2022-06-14 12:17:15.523026
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    sem = Semaphore(2)
    sem.release()
    sem.release()
    print(sem)
    sem.release()
    print(sem)
    assert sem._value==0
    sem.acquire()
    print(sem)

# Generated at 2022-06-14 12:17:24.288856
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()

    async def waiter(name):
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


# Generated at 2022-06-14 12:17:36.031154
# Unit test for method wait of class Condition
def test_Condition_wait():
    import typing
    import unittest
    import unittest.mock as mock
    from tornado.locks import Condition
    from tornado import gen

    @typing.overload
    def wait(self: Condition) -> typing.Coroutine[typing.Any, typing.Any, bool]:
        pass

    @typing.overload
    def wait(
        self: Condition,
        timeout: typing.Union[
            float,
            typing.Optional[
                typing.Union[
                    datetime.timedelta,
                    typing.Optional[
                        typing.Union[
                            typing.Optional[datetime.timedelta], float
                            ]
                        ]
                    ]
                ]
            ]
        ) -> typing.Coroutine[typing.Any, typing.Any, bool]:
        pass


# Generated at 2022-06-14 12:17:38.855718
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    semaphore = Semaphore(1)
    with util.disable_async_assertions():
        result = semaphore.__aenter__()
        assert result is None


# Generated at 2022-06-14 12:17:41.329520
# Unit test for method wait of class Event
def test_Event_wait():
    Event().wait(2)

if typing.TYPE_CHECKING:
    semaphore_sem_t = Type[Any]
else:
    semaphore_sem_t = typing.Any



# Generated at 2022-06-14 12:17:50.303434
# Unit test for method notify of class Condition
def test_Condition_notify():
    IOloop = ioloop.IOLoop.current()
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
        async def main():
            # Wait for waiter() and notifier() in parallel
            await gen.multi([waiter(), notifier()])
        IOloop.run_sync(main)
    test_Condition_notify.__doc__ = Condition.notify.__doc__
    test_Condition_notify()

# Generated at 2022-06-14 12:17:59.795957
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()
    async def do_work(n):
        print("I'll wait right here")
        await condition.wait()
        print("I'm done waiting: {}".format(n))

    # Test case 1
    c1 = do_work(1)
    c2 = do_work(2)
    c3 = do_work(3)
    c4 = do_work(4)
    c5 = do_work(5)
    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([c1, c2, c3, c4, c5])
        print("About to notify")
        condition.notify_all()
        print("Done notifying")

    IOLoop.current().run_sync(runner)
    assert c1.done()

# Generated at 2022-06-14 12:18:34.616323
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from tornado.locks import Lock
    import tornado.ioloop
    import tornado.testing
    import unittest
    import unittest.mock
    import typing

    TEST_TIMEOUT = 30.0

    class _LockTestCase(tornado.testing.AsyncTestCase):
        def setUp(self) -> None:
            super().setUp()
            self.lock = Lock()

        def tearDown(self) -> None:
            super().tearDown()
            self.lock = None


# Generated at 2022-06-14 12:18:38.536673
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    import inspect
    condition = Condition()
    set_methods = [func for func in dir(condition) if callable(
        getattr(condition, func)) and func not in dir(object)]
    set_member = [func for func in dir(condition)]
    assert (len(set_methods) == 5)
    assert (len(set_member) == 0)


# Generated at 2022-06-14 12:18:46.711730
# Unit test for method wait of class Condition
def test_Condition_wait():
    # testcode
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
    # testoutput
    print("I'll wait right here")
    print("About to notify")
    print("Done notifying")
    print("I'm done waiting")


# Generated at 2022-06-14 12:18:50.178353
# Unit test for method set of class Event
def test_Event_set():
    import unittest

    class TestEvent(unittest.TestCase):
        def test_Event_set(self):
            event = Event()
            event.set()
            self.assertTrue(event.wait())

    unittest.main()



# Generated at 2022-06-14 12:18:51.201692
# Unit test for method wait of class Condition
def test_Condition_wait():
    condition = Condition()
    condition.wait()



# Generated at 2022-06-14 12:18:53.174934
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    '''
    Test: (Warning) Method __aenter__ of class Semaphore is not tested.
    '''
    stat = 1
    return stat


# Generated at 2022-06-14 12:18:58.504748
# Unit test for method notify of class Condition
def test_Condition_notify():
    #async def f():
        #print('wait1')
        #await condition.wait()
        #print('wait1': done)
        #print('wait2')
        #await condition.wait()
        #print('wait2: done')
    #f()
    #condition = Condition()
    #IOLoop.current().run_sync(f)
    print(1)

# Generated at 2022-06-14 12:19:10.828541
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    from tornado_py3.locks import Condition
    from tornado import gen
    from tornado.ioloop import IOLoop
    condition = Condition()
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
        yield gen.multi([waiter(), notifier()])

    IOLoop.current().run_sync(runner)


if __name__ == '__main__':
    import tornado
    import tornado.ioloop
    import tornado.options
    tornado.ioloop.IOL

# Generated at 2022-06-14 12:19:14.171630
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    condition.notify()
    condition.notify(2)
    condition.notify_all()
    condition = Condition()
    condition.notify(1)



# Generated at 2022-06-14 12:19:26.351959
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    from tornado.locks import Condition

    condition = Condition()
    count = 10
    result = collections.deque()
    def waiter(n):
        def _():
            await condition.wait()
            result.append(n)
            return True
        return _

    for i in range(count):
        condition.io_loop.spawn_callback(waiter(i))

    condition.notify(5)
    condition.io_loop.run_sync(lambda: condition.wait(timeout=0.5))
    assert len(result) == 5
    condition.notify_all()
    condition.io_loop.run_sync(lambda: condition.wait(timeout=0.5))
    assert len(result) == 10



# Generated at 2022-06-14 12:20:25.850753
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    semaphore = Semaphore()

    assert semaphore.acquire() == None



# Generated at 2022-06-14 12:20:28.578996
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    sem = Semaphore(2)
    print("Worker 0 is working")
    sem.__aenter__()
    print("Worker 0 is done")


# Generated at 2022-06-14 12:20:32.830553
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    # __aenter__(self: tornado.locks.Semaphore) -> Awaitable[NoneType]
    # Test for method __aenter__ of class Semaphore
    # self.assertEqual(expected, Semaphore.__aenter__(self))
    assert True # TODO: implement your test here


# Generated at 2022-06-14 12:20:41.910724
# Unit test for method notify of class Condition
def test_Condition_notify():
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
    return "Done"


# Generated at 2022-06-14 12:20:43.140549
# Unit test for method __aenter__ of class Semaphore
def test_Semaphore___aenter__():
    return None

# Generated at 2022-06-14 12:20:51.250612
# Unit test for method wait of class Event
def test_Event_wait():
    '''
    Example:
        $ python -m tornado.locks
    '''
    from tornado import gen
    from tornado.ioloop import IOLoop

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

    IOLoop.current().run_sync(lambda: gen.multi([waiter(), setter()]))



# Generated at 2022-06-14 12:20:55.558203
# Unit test for method release of class Semaphore
def test_Semaphore_release():
    semaphore=Semaphore()
    semaphore.release()
    assert semaphore._value == 2
    semaphore.release()
    assert semaphore._value == 3
    semaphore._value = 1
    semaphore._waiters = deque([1,2,3])
    semaphore.release()
    assert semaphore._value == 0
    assert semaphore._waiters == deque([1,2,3])

# Generated at 2022-06-14 12:21:03.776007
# Unit test for method notify_all of class Condition
def test_Condition_notify_all():
    condition = Condition()

    async def waiter(future):
        print("I'll wait right here")
        await condition.wait()
        future.set_result("I'm done waiting")

    async def notifier(future):
        print("About to notify")
        condition.notify(1)
        condition.notify_all()
        print("Done notifying")

    async def runner():
        # Wait for waiter() and notifier() in parallel
        await gen.multi([waiter(a_future), notifier(a_future)])

    io_loop = ioloop.IOLoop.current()

    io_loop.run_sync(runner)



# Generated at 2022-06-14 12:21:05.633945
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    pass  # TODO

# Generated at 2022-06-14 12:21:06.988846
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    l = Condition()
    assert str(l) == "<Condition>"



# Generated at 2022-06-14 12:23:08.227816
# Unit test for method notify of class Condition
def test_Condition_notify():
    import time
    import logging
    import threading

    condition = Condition()
    lock = threading.Lock()
    waiters = []  # type: List[Future]

    async def waiter():
        print("I'll wait right here")
        await condition.wait()
        lock.acquire()
        print("I'm done waiting")
        condition.notify()
        time.sleep(1)
        lock.release()

    def notifier():
        condition.notify()

    def runner():
        # Wait for waiter() and notifier() in parallel
        io_loop = ioloop.IOLoop.current()
        io_loop.add_callback(waiter)
        io_loop.add_callback(notifier)
        io_loop.start()

    logging.info("start thread")
    t = threading.Thread

# Generated at 2022-06-14 12:23:13.943712
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    condition = Condition()
    condition.wait()
    assert repr(condition) == '<Condition waiters[1]>'
    condition.wait()
    assert repr(condition) == '<Condition waiters[2]>'
    condition.notify()
    assert repr(condition) == '<Condition waiters[1]>'
    condition.notify()
    assert repr(condition) == '<Condition>'

# Generated at 2022-06-14 12:23:15.858545
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from tornado import locks
    lock = locks.Lock()
    async def f():
        async with lock:
            pass
    await f()
    assert True

# Generated at 2022-06-14 12:23:26.835203
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    sem = Semaphore(2)
    fut1 = Future()
    fut2 = Future()
    fut3 = Future()
    fut4 = Future()
    fut5 = Future()
    fut6 = Future()
    fut7 = Future()
    fut8 = Future()
    fut9 = Future()
    fut10 = Future()
    fut11 = Future()
    def worker1():
        async def worker(worker_id):
            await sem.acquire()
            try:
                print("Worker %d is working" % worker_id)
                #await use_some_resource()
            finally:
                print("Worker %d is done" % worker_id)
                sem.release()
        io_loop = ioloop.IOLoop.current()
        io_loop.run_sync(worker, 1)
   

# Generated at 2022-06-14 12:23:31.423395
# Unit test for method acquire of class Semaphore
def test_Semaphore_acquire():
    c = Semaphore()
    #todo: make mock of Future class
    f = Future()
    f.set_result(_ReleasingContextManager(c))
    c._waiters.append(f)
    assert c.acquire() == f


# Generated at 2022-06-14 12:23:43.016983
# Unit test for method notify of class Condition
def test_Condition_notify():
    condition = Condition()
    notification_count = 0
    @gen.coroutine
    def waiter():
        nonlocal notification_count
        print("condition is %s"%condition)
        print("I'll wait right here")
        notification_received = yield condition.wait()
        print("I'm done waiting")
        notification_count += 1

    @gen.coroutine
    def notifier():
        print("About to notify")
        print("condition is %s"%condition)
        condition.notify()
        print("Done notifying")

    @gen.coroutine
    def runner():
        # Wait for waiter() and notifier() in parallel
        print("condition is %s"%condition)
        yield gen.multi([waiter(), notifier()])

    ioloop.IOLoop.current().run_sync(runner)
   

# Generated at 2022-06-14 12:23:46.949538
# Unit test for method __repr__ of class Condition
def test_Condition___repr__():
    """Test case for `Condition.__repr__()`"""
    condition = Condition()
    assert "Condition" in condition.__repr__()



# Generated at 2022-06-14 12:23:50.433631
# Unit test for method __aenter__ of class Lock
def test_Lock___aenter__():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.locks import Lock

    l = Lock()
    IOLoop.current().run_sync(l.__aenter__)
    print('Lock___aenter__ success')



# Generated at 2022-06-14 12:23:52.233153
# Unit test for method set of class Event
def test_Event_set():
    event = Event()
    event.set()
    print("test Event succeed")


# Generated at 2022-06-14 12:23:59.713182
# Unit test for method notify of class Condition
def test_Condition_notify():
    main_loop = ioloop.IOLoop()
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
    main_loop.run_sync(runner)

