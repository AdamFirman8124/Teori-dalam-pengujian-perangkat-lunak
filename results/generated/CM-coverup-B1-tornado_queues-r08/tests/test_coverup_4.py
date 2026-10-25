# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueFull


@pytest.fixture
def current_event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        asyncio.set_event_loop(None)
        loop.close()


def test_put_nowait_wakes_waiting_getter(current_event_loop):
    q = Queue(maxsize=1)
    getter = q.get()

    assert q.empty()
    assert len(q._getters) == 1
    assert not getter.done()

    q.put_nowait("item")

    assert getter.done()
    assert not getter.cancelled()
    assert getter.result() == "item"
    assert q.empty()
    assert not q._getters

    q.task_done()


def test_put_nowait_full_raises_queue_full():
    q = Queue(maxsize=1)
    q.put_nowait("first")

    assert q.full()
    assert not q._getters

    with pytest.raises(QueueFull):
        q.put_nowait("second")

    assert q.qsize() == 1
    assert q.get_nowait() == "first"
    assert q.empty()

    q.task_done()


def test_put_nowait_enqueues_when_space_is_available():
    q = Queue(maxsize=2)

    assert q.empty()
    assert not q._getters

    q.put_nowait("a")

    assert q.qsize() == 1
    assert not q.full()

    q.put_nowait("b")

    assert q.qsize() == 2
    assert q.full()
    assert q.get_nowait() == "a"
    q.task_done()
    assert q.get_nowait() == "b"
    q.task_done()
    assert q.empty()
