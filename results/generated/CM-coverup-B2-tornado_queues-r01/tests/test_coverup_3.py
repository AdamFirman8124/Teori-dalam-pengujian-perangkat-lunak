# file: project/tornado/queues.py:256-272
# asked: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}
# gained: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueEmpty


@pytest.fixture
def current_event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        asyncio.set_event_loop(None)
        loop.close()


def test_get_nowait_releases_waiting_putter(current_event_loop):
    queue = Queue(maxsize=1)
    queue.put_nowait("first")
    pending_put = queue.put("second")

    assert queue.full()
    assert not pending_put.done()

    assert queue.get_nowait() == "first"
    assert pending_put.done()
    assert not pending_put.cancelled()
    assert pending_put.result() is None

    assert queue.get_nowait() == "second"
    assert queue.empty()

    queue.task_done()
    queue.task_done()
    assert queue.join().done()


def test_get_nowait_discards_cancelled_putter(current_event_loop):
    queue = Queue(maxsize=1)
    queue.put_nowait("queued")
    cancelled_put = queue.put("cancelled")

    assert cancelled_put.cancel()
    assert cancelled_put.cancelled()

    assert queue.get_nowait() == "queued"
    assert queue.empty()

    queue.task_done()
    assert queue.join().done()


def test_get_nowait_raises_when_queue_is_empty(current_event_loop):
    queue = Queue()

    with pytest.raises(QueueEmpty):
        queue.get_nowait()

    assert queue.empty()
    assert queue.qsize() == 0
