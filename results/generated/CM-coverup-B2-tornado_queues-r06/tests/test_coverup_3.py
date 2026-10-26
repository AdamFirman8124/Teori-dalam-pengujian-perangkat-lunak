# file: project/tornado/queues.py:256-272
# asked: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}
# gained: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}

import asyncio

import pytest

from tornado.queues import Queue, QueueEmpty


@pytest.fixture()
def _event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        try:
            pending = [t for t in asyncio.all_tasks(loop) if not t.done()]
            for task in pending:
                task.cancel()
            if pending:
                loop.run_until_complete(
                    asyncio.gather(*pending, return_exceptions=True)
                )
        finally:
            asyncio.set_event_loop(None)
            loop.close()


def test_get_nowait_with_waiting_putter(_event_loop):
    q = Queue(maxsize=1)
    q.put_nowait("first")
    putter_future = q.put("second")

    assert q.full()
    assert len(q._putters) == 1
    assert not putter_future.done()

    assert q.get_nowait() == "first"

    assert putter_future.done()
    assert putter_future.result() is None
    assert not q._putters
    assert q.qsize() == 1
    assert q.get_nowait() == "second"
    assert q.empty()


def test_get_nowait_consumes_expired_putter(_event_loop):
    q = Queue(maxsize=1)
    q.put_nowait("first")
    putter_future = q.put("second")
    putter_future.cancel()

    assert putter_future.done()
    assert q.get_nowait() == "first"
    assert not q._putters
    assert q.empty()


def test_get_nowait_returns_available_item(_event_loop):
    q = Queue()
    q.put_nowait(42)

    assert q.get_nowait() == 42
    assert q.empty()
    assert not q._putters


def test_get_nowait_raises_queue_empty(_event_loop):
    q = Queue()

    with pytest.raises(QueueEmpty):
        q.get_nowait()

    assert q.empty()
    assert not q._putters
    assert not q._getters
