# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueFull


@pytest.fixture
def event_loop():
    # tornado.concurrent.Future() requires a current asyncio event loop,
    # which does not exist by default in Python 3.14's main thread.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    asyncio.set_event_loop(None)
    loop.close()


def test_put_nowait_wakes_waiting_getter(event_loop):
    q = Queue(maxsize=1)
    getter = q.get()
    assert not getter.done()

    q.put_nowait("item")

    assert getter.done()
    assert not getter.cancelled()
    assert getter.result() == "item"
    assert q.empty()
    assert q.qsize() == 0


def test_put_nowait_raises_queue_full(event_loop):
    q = Queue(maxsize=1)
    q.put_nowait("first")
    assert q.full()

    with pytest.raises(QueueFull):
        q.put_nowait("second")

    assert q.qsize() == 1
    assert q.get_nowait() == "first"
    assert q.empty()


def test_put_nowait_appends_when_space_available(event_loop):
    q = Queue(maxsize=2)
    q.put_nowait("a")
    q.put_nowait("b")

    assert q.qsize() == 2
    assert q.full()
    assert q.get_nowait() == "a"
    assert q.get_nowait() == "b"
    assert q.empty()


def test_put_nowait_discards_cancelled_getter(event_loop):
    q = Queue(maxsize=1)
    getter = q.get()
    getter.cancel()
    assert getter.cancelled()

    q.put_nowait("item")

    assert q.qsize() == 1
    assert q.get_nowait() == "item"
    assert q.empty()


def test_put_nowait_discards_cancelled_putter(event_loop):
    q = Queue(maxsize=1)
    q.put_nowait("first")
    putter = q.put("second")
    putter.cancel()
    assert putter.cancelled()

    assert q.get_nowait() == "first"

    q.put_nowait("third")
    assert q.qsize() == 1
    assert q.get_nowait() == "third"
    assert q.empty()
