# file: project/tornado/queues.py:209-223
# asked: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}
# gained: {"lines": [214, 215, 216, 217, 218, 219, 220, 221, 223], "branches": [[215, 216], [215, 220], [220, 221], [220, 223]]}

import asyncio

import pytest

from tornado.concurrent import Future
from tornado.queues import Queue, QueueFull


@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        asyncio.set_event_loop(None)
        loop.close()


def test_put_nowait_delivers_item_to_waiting_getter(event_loop):
    queue = Queue()
    getter = queue.get()

    assert not getter.done()
    assert queue.empty()

    queue.put_nowait("item")

    assert getter.done()
    assert getter.result() == "item"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()


def test_put_nowait_raises_when_queue_is_full(event_loop):
    queue = Queue(maxsize=1)
    queue.put_nowait("first")

    assert queue.full()

    with pytest.raises(QueueFull):
        queue.put_nowait("second")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "first"

    queue.task_done()
    assert queue.join().done()


def test_put_nowait_enqueues_item_when_space_is_available(event_loop):
    queue = Queue(maxsize=2)

    queue.put_nowait("item")

    assert queue.qsize() == 1
    assert queue.get_nowait() == "item"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()


def test_put_nowait_rejects_nonempty_queue_with_waiting_getter(event_loop):
    queue = Queue()
    queue.put_nowait("existing")
    getter = Future()
    queue._getters.append(getter)

    try:
        with pytest.raises(
            AssertionError, match="queue non-empty, why are getters waiting"
        ):
            queue.put_nowait("new")

        assert queue.qsize() == 1
        assert not getter.done()
    finally:
        if getter in queue._getters:
            queue._getters.remove(getter)
        if not getter.done():
            getter.cancel()

        assert queue.get_nowait() == "existing"
        queue.task_done()

    assert queue.empty()
    assert queue.join().done()
