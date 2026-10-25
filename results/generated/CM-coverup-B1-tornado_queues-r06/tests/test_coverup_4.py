# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueFull


@pytest.fixture(autouse=True)
def _event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        pending = [t for t in asyncio.all_tasks(loop) if not t.done()]
        for task in pending:
            task.cancel()
        if pending:
            loop.run_until_complete(
                asyncio.gather(*pending, return_exceptions=True)
            )
        loop.close()
        asyncio.set_event_loop(None)


def test_put_nowait_delivers_to_waiting_getter():
    q = Queue()
    getter = q.get()
    assert not getter.done()
    assert len(q._getters) == 1

    q.put_nowait("item")

    assert getter.done()
    assert not getter.cancelled()
    assert getter.result() == "item"
    assert q.qsize() == 0
    assert q.empty()
    assert not q._getters
    assert q._unfinished_tasks == 1

    q.task_done()
    assert q._unfinished_tasks == 0


def test_put_nowait_raises_queue_full():
    q = Queue(maxsize=1)
    q.put_nowait("first")
    assert q.full()
    assert q.qsize() == 1

    with pytest.raises(QueueFull):
        q.put_nowait("second")

    assert q.qsize() == 1
    assert q.get_nowait() == "first"
    q.task_done()
    assert q.empty()


def test_put_nowait_appends_when_space_available():
    q = Queue(maxsize=2)
    q.put_nowait("a")
    q.put_nowait("b")

    assert q.qsize() == 2
    assert q.full()
    assert not q._getters

    assert q.get_nowait() == "a"
    assert q.get_nowait() == "b"
    q.task_done()
    q.task_done()
    assert q.empty()
    assert q._unfinished_tasks == 0


def test_put_nowait_consumes_expired_getter():
    q = Queue()
    getter = q.get()
    getter.cancel()
    assert getter.done()

    q.put_nowait("a")

    assert not q._getters
    assert q.qsize() == 1
    assert q.get_nowait() == "a"
    q.task_done()


def test_put_nowait_consumes_expired_putter():
    q = Queue(maxsize=1)
    q.put_nowait("a")

    putter = q.put("b")
    assert not putter.done()
    assert len(q._putters) == 1

    putter.cancel()
    assert putter.done()

    with pytest.raises(QueueFull):
        q.put_nowait("c")

    assert not q._putters
    assert q.qsize() == 1
    assert q.get_nowait() == "a"
    q.task_done()
