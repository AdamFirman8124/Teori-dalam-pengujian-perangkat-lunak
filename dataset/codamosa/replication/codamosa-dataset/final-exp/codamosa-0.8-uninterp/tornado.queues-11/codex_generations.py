

# Generated at 2022-06-14 12:46:31.580429
# Unit test for method put of class Queue
def test_Queue_put():
    _putters = collections.deque([(4, None), (5, None)])
    empty_q = Queue(0)
    empty_q._putters = _putters
    full_q = Queue(1)
    full_q._putters = _putters
    full_q._put(1)
    empty_q.put(1)
    full_q.put(2)
    full_q.put(3)
    full_q.put(4)
    full_q.put(5)
    full_q.put(6)


# Generated at 2022-06-14 12:46:36.297173
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    #testcase 1
    m = Queue()
    try:
        m.get_nowait()
    except QueueEmpty:
        pass
    #testcase 2
    m = Queue()
    m._queue.append(1)
    m.get_nowait()
    assert(not m.empty())

# Generated at 2022-06-14 12:46:39.286905
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    assert q.get() == None

if __name__ == "__main__":
    test_Queue_get()

# Generated at 2022-06-14 12:46:51.045761
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)

    # Start consumer without waiting (since it never finishes).
    # ioloop.IOLoop.current().spawn_callback(consumer)
    # await producer()     # Wait for producer to put all tasks.
    # await q.join()       # Wait for consumer to finish all tasks.
    # print('Done')
    q.put_nowait(1)
    q.put_nowait(2)
    let_put = q.put(3)
    get_one = q.get()
    let_put.result()
    get_one.result()
    assert q.qsize() == 2
    assert q.get_nowait() == 2
    q.task_done()



# Generated at 2022-06-14 12:46:55.903526
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import unittest
    import asyncio
    from tornado.queues import Queue
    class TestQueue(unittest.TestCase):
        def test_get_nowait(self):
            q = Queue(maxsize=0)
            q.put_nowait(2)
            #x = q.get_nowait()
            self.assertEqual(q.get_nowait(), 2)
    unittest.main()



# Generated at 2022-06-14 12:47:04.678068
# Unit test for method put of class Queue
def test_Queue_put():
    q = Queue(maxsize=2)
    q.qsize()
    q.empty()
    q.full()
    q.put(1)
    q.qsize()
    q.put(2)
    q.put(3)
    q.qsize()
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    q.qsize()
    # print(q)


# Generated at 2022-06-14 12:47:14.222236
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

# Generated at 2022-06-14 12:47:26.367616
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import random
    import time
    import logging
    # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] %(message)s')
    logging.basicConfig(level=logging.FATAL, format='%(asctime)s - [%(levelname)s] %(message)s')
    def log(message):
        # print(message)
        logging.debug(message)

    q = Queue(maxsize=1)

    log("Testing if maxsize equals 0")
    q.maxsize = 0
    assert q.maxsize == 0

    log("Testing if maxsize equals -1")
    q.maxsize = -1
    assert q.maxsize == 0

    log("Testing if maxsize equals None")
    q.maxsize

# Generated at 2022-06-14 12:47:28.812161
# Unit test for method put of class Queue
def test_Queue_put():
    queue = Queue(maxsize=0)
    future = Future()
    timeout = Optional[Union[float, datetime.timedelta]](timeout)
    assert queue.put(timeout) == future



# Generated at 2022-06-14 12:47:38.733077
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    try:
        q.put_nowait(3)
        print("It is ok to put nowait when queue is not full")
    except QueueFull:
        print("It is not ok to put nowait when queue is not full")
    try:
        q.put_nowait(4)
        print("It is ok to put nowait when queue is not full")
    except QueueFull:
        print("It is not ok to put nowait when queue is not full")
    try:
        q.put_nowait(5)
        print("It is ok to put nowait when queue is not full")
    except QueueFull:
        print("It is not ok to put nowait when queue is not full")
test_Queue_put_nowait()



# Generated at 2022-06-14 12:47:53.287053
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    assert q.qsize() == 1

# Generated at 2022-06-14 12:47:58.057109
# Unit test for method get of class Queue
def test_Queue_get():
    import tornado.ioloop
    import tornado.queues
    q = tornado.queues.Queue()
    tornado.ioloop.IOLoop.current().run_sync(lambda: q.put(1))
    assert tornado.ioloop.IOLoop.current().run_sync(lambda: q.get()) == 1

# Generated at 2022-06-14 12:47:59.261102
# Unit test for method get of class Queue
def test_Queue_get():
    pass


# Generated at 2022-06-14 12:48:11.287243
# Unit test for method put of class Queue
def test_Queue_put():
    import pytest
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


# Generated at 2022-06-14 12:48:19.537492
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop, TimeoutError
    from tornado.gen import Timeout, sleep
    from tornado.testing import AsyncTestCase, main

    q = Queue()

    async def t1():
        await q.put(1)
        await q.put(2)
        await q.put(3)
        await sleep(1)
        raise TimeoutError
        await q.put(4)
        await q.put(5)
        await q.put(6)

    async def t2():
        await q.put(9)
        await q.put(7)
        await q.put(8)
        await sleep(1)
        raise TimeoutError
        await q.put(10)
        await q.put(11)

# Generated at 2022-06-14 12:48:22.276548
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    Q = Queue(1)
    try:
        Q.put_nowait(1)
        Q.put_nowait(1)
        return True
    except:
        pass
    return False


# Generated at 2022-06-14 12:48:35.830709
# Unit test for method get of class Queue
def test_Queue_get():
    # Test cases
    def test_case_1() -> None:
        q = Queue()
        assert q.qsize() == 0
        assert q.empty() == True
        assert q.full() == False
        q.put_nowait(1)
        q.put_nowait(2)
        assert q.qsize() == 2
        assert q.empty() == False
        assert q.full() == False
        assert q.get_nowait() == 1
        assert q.get_nowait() == 2
        assert q.qsize() == 0
        assert q.empty() == True
        assert q.full() == False
        try:
            q.get_nowait()
            assert False
        except QueueEmpty:
            assert True

# Generated at 2022-06-14 12:48:40.118427
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    async def main():
        q = Queue(maxsize=2)

        await q.put_nowait(1)
        await q.put_nowait(2)
        await q.put_nowait(3)

    try:
        ioloop.IOLoop.current().run_sync(main)
    except QueueError as e:
        print(e)


# Generated at 2022-06-14 12:48:48.216941
# Unit test for method get of class Queue
def test_Queue_get():
    from unittest import TestCase
    from tornado.testing import gen_test
    from tornado.ioloop import IOLoop

    class TestCase(TestCase):
        @gen_test
        def test_Queue(self):
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
                await producer()     # Wait for producer to

# Generated at 2022-06-14 12:49:00.035103
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    # q = Queue(maxsize=1)
    # q.put_nowait(1)
    # q.put_nowait(1)
    # q.put_nowait(1)
    # # print(q.qsize())
    # q.put_nowait(1)
    # print(q.qsize())
    # print(q.empty())
    # print(q.full())
    async def consumer():
        async for item in q:
            q.task_done()
            print(item)

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)
            # await q.join()

    q = Queue(maxsize=1)
    loop = ioloop.IOLoop.current()
    loop

# Generated at 2022-06-14 12:49:23.490757
# Unit test for method put of class Queue
def test_Queue_put():
  print("test Queue.put");
  from tornado import gen
  from tornado.ioloop import IOLoop
  from tornado.queues import Queue;

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
    await q.join()       # Wait for consumer

# Generated at 2022-06-14 12:49:37.108182
# Unit test for method get of class Queue
def test_Queue_get():
    import queue
    import unittest
    from tornado.queues import Queue, QueueEmpty
    from tornado import gen, testing, ioloop

    class QueueTestCase(unittest.TestCase):
        def setUp(self):
            self.queue = Queue(1)
            self.io_loop = ioloop.IOLoop()

        def tearDown(self):
            self.queue.join()
            self.queue.close()

        @testing.gen_test
        def test_Queue_get_nowait(self):
            self.queue.put('item')
            item = self.queue.get_nowait()
            self.assertEqual('item', item)
            with self.assertRaises(QueueEmpty):
                self.queue.get_nowait()

# Generated at 2022-06-14 12:49:43.433064
# Unit test for method put of class Queue
def test_Queue_put():
    import time
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    def consumer():
        while True:
            item = yield q.get()
            try:
                print('Doing work on %s' % item)
                yield gen.sleep(0.01)
            finally:
                q.task_done()


# Generated at 2022-06-14 12:49:54.115942
# Unit test for method put of class Queue
def test_Queue_put():
    async def fun():
        pass
    fun()
    q = Queue()
    print(test_Queue_put.__name__+':', q.empty())
    q.put(11)
    q.put(22)
    assert q.full(), "queue not full, why are putters waiting?"
    q.put(33)
    q.put(44)
    q.put(55)
    assert q.full(), "queue not full, why are putters waiting?"
    q.get_nowait()
    print(test_Queue_put.__name__+':', q.empty())
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()
    q.get_nowait()

# Generated at 2022-06-14 12:50:05.312542
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.queues import Queue
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    try:
        q.get_nowait()
    except QueueEmpty:
        assert True
    else:
        assert False
    assert q.maxsize == 2
    assert q.qsize() == 0

    # it is empty
    assert q.empty()

    # it is not full
    assert not q.full()
    q = Queue()
    q.put_nowait(1)
    try:
        q.get_nowait()
    except QueueEmpty:
        assert False

# Generated at 2022-06-14 12:50:13.248229
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    # Queue is empty
    assert q.empty() 
    # Put 1
    q.put_nowait(1)
    # Queue is not full
    assert not q.full()
    # Put 2
    q.put_nowait(2)
    # Queue is full
    assert q.full()
    # Queue is empty
    assert not q.empty()
    # Put 3, will raise exception
    try:
        q.put_nowait(3)
    except Exception as e:
        assert(str(e) == "QueueFull")


# Generated at 2022-06-14 12:50:20.311434
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import unittest
    from unittest.mock import patch

    from tornado.queues import Queue, QueueEmpty

    # Unit test for method get_nowait of class Queue
    class TestQueue_get_nowait(unittest.TestCase):
        @patch("tornado.queues.Queue._get")
        def test_get_nowait_with_qsize_grater_than_0(self, get):
            qsize = 1
            q = Queue()
            q._queue = [1]
            expected = 1
            actual = q.get_nowait()
            self.assertEqual(expected, actual)


# Generated at 2022-06-14 12:50:24.813869
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    item1 = 1
    item2 = 2
    item3 = 3
    q.put_nowait(item1)
    q.put_nowait(item2)
    assert item1 in q._queue and item2 in q._queue
    try:
        q.put_nowait(item3)
        assert False
    except QueueFull:
        assert item1 in q._queue and item2 in q._queue and item3 not in q._queue


# Generated at 2022-06-14 12:50:33.422342
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


# Generated at 2022-06-14 12:50:44.086031
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado.ioloop import IOLoop
    from threading import Thread
    from time import sleep
    from queue import Empty
    q = Queue(maxsize=2)
    def producer():
        for item in range(5):
            q.put_nowait(item)
            print('Put %s' % item)
            sleep(0.01)
    def consumer():
        while True:
            item = q.get_nowait()
            print('Doing work on %s' % item)
    def main():
        # Start consumer without waiting (since it never finishes).
        t1 = Thread(target = consumer)
        t1.start()
        # Wait for producer to put all tasks.
        t2 = Thread(target = producer)
        t2.start()
        # Wait for consumer to finish all tasks.
        t

# Generated at 2022-06-14 12:51:15.306026
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import  tornado
    import  tornado.ioloop
    import  tornado.web
    import tornado.queues
    import   tornado.iostream
    import tornado.gen
    q = tornado.queues.Queue()
    def consume():

        while True:
            print("Doing work on %s" % q.get_nowait())
            yield tornado.gen.sleep(1)
            q.task_done()

    def produce():
        for item in range(5):
            q.put(item)
            print("Put %s" % item)
            tornado.ioloop.IOLoop.current().spawn_callback(produce)
        # tornado.ioloop.IOLoop.current().spawn_callback(consume)
        tornado.ioloop.IOLoop.instance().start()


# Generated at 2022-06-14 12:51:19.930998
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    d = Queue(maxsize=2)
    try:
        d.put_nowait(1)
        d.put_nowait(2)
        d.put_nowait(3)
    except QueueFull:
        return True
    return False


# Generated at 2022-06-14 12:51:30.730249
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
        IOLoop.current().spawn_callback(consumer)
        await producer()
        await q.join()
        print('Done')

    IOLoop.current().run_sync(main)



# Generated at 2022-06-14 12:51:36.142872
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3)
    assert q.qsize() == 2


# Generated at 2022-06-14 12:51:44.286213
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    # import pdb
    # pdb.set_trace()
    q = Queue(maxsize=2)
    
    async def consumer():
        async for item in q:
            print('Doing work on %s' % item)

    async def producer():
        for item in range(5):
            try:
                q.put_nowait(item)
                print('Put %s' % item)
            except QueueFull:
                print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        ioloop.IOLoop.current().spawn_callback(consumer)
        await producer()     # Wait for producer to put all tasks.
        await q.join()       # Wait for consumer to finish all tasks.
        print('Done')
    ioloop.IOL

# Generated at 2022-06-14 12:51:51.125270
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    try:
        # This line will fail because you have not implemented
        # the put_nowait method in class Queue
        Queue.put_nowait(Queue,1)
        print ("Test of method put_nowait() of class Queue failed")
    except NotImplementedError as e:
        print ("method put_nowait() of class Queue is not implemented")



# Generated at 2022-06-14 12:51:55.700956
# Unit test for method put of class Queue
def test_Queue_put():
    a = Queue()
    a.put(1)
    assert a.qsize() == 1
    assert a.get_nowait() == 1
    a.put_nowait(5)
    assert a.get_nowait() == 5


test_Queue_put()


# Generated at 2022-06-14 12:52:02.089934
# Unit test for method put of class Queue
def test_Queue_put():
    queue = Queue()

    test_dict = {'val1': 'test1', 'val2': 'test2', 'val3': 'test3'}
    test_list = []
    for _, val in test_dict.items():
        test_list.append(queue.put(val, timeout=None))
    print(test_list)
    print(queue._format())


# Generated at 2022-06-14 12:52:10.557101
# Unit test for method put of class Queue
def test_Queue_put():
    # first
    try:
        print("Test 1: normal operation")
        q = Queue()
        f1 = q.put(1)
        f2 = q.put(2)
        f3 = q.put(3)
        print(f1, f2, f3)
        print()
    except Exception:
        print()
    # second
    try:
        print("Test 2: normal operation, too many items")
        q = Queue(maxsize = 0)
        f1 = q.put(1)
        f2 = q.put(2)
        f3 = q.put(3)
        print(f1, f2, f3)
        print()
    except Exception:
        print()
    # third

# Generated at 2022-06-14 12:52:13.267828
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue(maxsize=2)
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()

# Generated at 2022-06-14 12:52:47.440799
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    import time
    n = [0]
    def testQueue_put_nowait_case1():
        MAXSIZE = 0
        q = Queue(maxsize=MAXSIZE)
        assert(not q.full())
        q.put_nowait(0)
        assert(not q.full())
        assert(q.qsize()==1)
        q.put_nowait(1)
        assert(not q.full())
        assert(q.qsize()==2)
        def consumer():
            while True:
                try:
                    item = q.get_nowait()
                    print('Doing work on %s' % item)
                    time.sleep(1)
                finally:
                    q.task_done()
                    n[0]+=1
                    if n[0]==3:
                        break

# Generated at 2022-06-14 12:52:55.930673
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
        IOLoop.current().spawn_callback(consumer)
        await producer()
        await q.join()
        print('Done')
    IOLoop.current().run_sync(main)
    
    
    
    

# Generated at 2022-06-14 12:53:07.471453
# Unit test for method get of class Queue
def test_Queue_get():
    producer_putters = [1, 2, 3, 4]
    producer_results = [None, None, None, None]
    consumer_gets = [2, 3, 4, 1]
    producer_exceptions = [None, None, None, None]
    consumer_exceptions = [QueueEmpty(), QueueEmpty(), QueueEmpty(), None]
    # make sure that get is not blocking
    # create a Queue with a maxsize of 1
    q = Queue(maxsize=1)
    producer = q.put
    # get an item from the queue
    consumer = q.get_nowait

# Generated at 2022-06-14 12:53:11.960578
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue()
    q.put(1)
    q.put(4)
    q.put(1)
    q.get_nowait()
    print(q.__dict__)

# Generated at 2022-06-14 12:53:23.425755
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import inspect
    import sys
    import os
    package_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ""))
    sys.path.insert(0, package_folder)
    from tornado.queues import Queue
    from tornado.ioloop import IOLoop
    from tornado import gen
    from tornado.concurrent import Future, future_set_result_unless_cancelled
    from tornado.locks import Event
    import collections
    q = Queue(maxsize=2)
    assert q.qsize() == 0
    async def consumer():
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await gen.sleep(0.01)
            finally:
                q.task_done()
    # Start

# Generated at 2022-06-14 12:53:32.017246
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue()
    initial_size = q.qsize()
    item = ["a","b","c"]

    q.put_nowait(item)
    final_size = q.qsize()
    
    if final_size == initial_size + 1:
        return True
    else:
        return False
    
result = test_Queue_put_nowait()
assert result, "Error: test case for method put_nowait in class Queue failed."
print("Success: Put test case for method put_nowait in class Queue passed.")


# Generated at 2022-06-14 12:53:42.847613
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)

    items_get = []
    async def consumer():
        nonlocal items_get
        async for item in q:
            try:
                print('Doing work on %s' % item)
                items_get.append(item)
                # await gen.sleep(0.01)
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


# Generated at 2022-06-14 12:53:43.854479
# Unit test for method get of class Queue
def test_Queue_get():
  pass


# Generated at 2022-06-14 12:53:47.432497
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    q = Queue(maxsize=2)
    q.put_nowait(2)
    q.put_nowait(3)
    try:
        q.put_nowait(4)
        assert False
    except:
        pass


# Generated at 2022-06-14 12:53:57.610621
# Unit test for method get of class Queue
def test_Queue_get():
    import time
    import sys
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=3)

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
            await  q.put(item)
            print('Put %s' % item)
    async def main():
        IOLoop.current().spawn_callback(consumer)
        await producer()
        await q.join()
        print('Done')
    IOLoop.current().run_sync(main)
    print(q)

# Generated at 2022-06-14 12:55:02.200253
# Unit test for method get of class Queue
def test_Queue_get():
    from typing import Deque, Tuple
    from queue import Queue
    import os
    import time
    import signal
    import threading
    from concurrent.futures import ThreadPoolExecutor
    from tornado import gen, ioloop
    from tornado.concurrent import Future
    from tornado.queues import Queue, QueueEmpty, QueueFull
    from tornado.locks import Event
    from typing import Any, Callable, List, Optional
    from datetime import datetime, timedelta
    import typing
    # Create a new Queue
    queue = Queue()
    # Create a new Event
    finished = Event()
    # Create a new Future
    # Create a new future
    future = Future()
    try:
        queue.put_nowait(1)
    except QueueFull:
        future.set_result(None)

# Generated at 2022-06-14 12:55:11.828970
# Unit test for method get of class Queue
def test_Queue_get():
    print("start Queue get test")
    def get_test():
        print("start Queue get test")
        import asyncio
        from tornado import gen
        from tornado.ioloop import IOLoop
        from tornado.queues import Queue

        q = Queue(maxsize=2)
        async def consumer():
            #for item in await q.get():
            while True:
                if await q.get() == 9:
                    #print("get 9 and break the loop")
                    break
                else:
                    print("keep getting")
                    #q.task_done()

        async def producer():
            await q.put(3)
            await q.put(5)
            await q.put(9)

        async def main():
            # Start consumer without waiting (since it never finishes).
            IOLoop.current().spawn

# Generated at 2022-06-14 12:55:17.702909
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    import tornado.gen
    import tornado.ioloop
    from tornado.queues import Queue
    q = Queue(maxsize=2)

    async def consumer(nb):
        async for item in q:
            try:
                print('Doing work on %s' % item)
                await tornado.gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            print('Put %s' % item)

    async def main():
        # Start consumer without waiting (since it never finishes).
        [tornado.ioloop.IOLoop.current().spawn_callback(consumer) for i in range(nb)]
        await producer()     # Wait for producer to put all tasks.
        await q.join()       #

# Generated at 2022-06-14 12:55:21.037863
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    queuetest = Queue(maxsize=2)
    queuetest.put_nowait(5)
    queuetest.put_nowait(6)
    assert queuetest.qsize() == 2


# Generated at 2022-06-14 12:55:21.772041
# Unit test for method get of class Queue
def test_Queue_get():
    return None

# Generated at 2022-06-14 12:55:23.265334
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    q = Queue(maxsize = 3)
    q.get_nowait()
    assert q.empty() == False


# Generated at 2022-06-14 12:55:27.144921
# Unit test for method get of class Queue
def test_Queue_get():
    q = Queue()
    future1 = q.get()
    future2 = q.get()
    future3 = q.get()
    assert future1 is not None
    assert future1.__class__.__name__ == 'Future'
    assert future2 is not None
    assert future2.__class__.__name__ == 'Future'
    assert future3 is not None
    assert future3.__class__.__name__ == 'Future'


# Generated at 2022-06-14 12:55:39.278589
# Unit test for method put_nowait of class Queue
def test_Queue_put_nowait():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from tornado.queues import Queue

    q = Queue(maxsize=2)
    result = []

    async def consumer(name: str) -> None:
        async for item in q:
            result.append(item)

    async def producer() -> None:
        await q.put("a1")
        await q.put("a2")
        await q.put("a3")
        await q.put("a4")
        await q.put("a5")

    IOLoop.current().run_sync(producer)
    IOLoop.current().run_sync(consumer)
    assert result == ["a1", "a2", "a3", "a4", "a5"]
    assert q.qsize() == 0


# Unit

# Generated at 2022-06-14 12:55:45.434932
# Unit test for method put of class Queue
def test_Queue_put():
    from tornado import gen
    from tornado.ioloop import IOLoop
    from Queue import Queue

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

   

# Generated at 2022-06-14 12:55:46.409324
# Unit test for method get_nowait of class Queue
def test_Queue_get_nowait():
    pass