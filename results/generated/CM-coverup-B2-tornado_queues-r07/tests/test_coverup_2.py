# file: project/tornado/queues.py:256-272
# asked: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}
# gained: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}

import asyncio

import pytest

from tornado.concurrent import Future
from tornado.queues import Queue, QueueEmpty


def test_get_nowait_raises_on_empty_queue():
    """Covers line 272: QueueEmpty is raised when the queue is empty."""
    q = Queue()
    with pytest.raises(QueueEmpty):
        q.get_nowait()
    # Postcondition: queue is still empty and has no waiters.
    assert q.qsize() == 0
    assert not q._putters
    assert not q._getters


def test_get_nowait_returns_item_when_available():
    """Covers lines 269-270: item returned via _get() when qsize() > 0."""
    q = Queue()
    q.put_nowait("a")
    q.put_nowait("b")

    item = q.get_nowait()

    # Postcondition: FIFO order respected and queue shrunk.
    assert item == "a"
    assert q.qsize() == 1
    assert q.get_nowait() == "b"
    assert q.empty()


def test_get_nowait_resolves_waiting_putter_on_full_queue():
    """Covers lines 263-268: a blocked putter's item is taken, the putter
    future is resolved, and the previously stored item is returned."""

    async def scenario():
        q = Queue(maxsize=1)
        q.put_nowait("first")

        # Queue is full now, so put() registers a waiting putter.
        # The Future must be created while an event loop is running.
        putter_future = q.put("second")
        assert len(q._putters) == 1
        assert not putter_future.done()

        item = q.get_nowait()

        # Postconditions: the original item is returned, the putter's item
        # is now in the queue, and the putter future resolved with None.
        assert item == "first"
        assert putter_future.done()
        assert putter_future.result() is None
        assert q.qsize() == 1
        assert not q._putters
        assert q.get_nowait() == "second"
        assert q.empty()

    asyncio.run(scenario())


def test_get_nowait_consumes_expired_putters():
    """Covers line 262 (and the putter-expiry loop in _consume_expired):
    done putter futures are discarded before the size check."""

    async def scenario():
        q = Queue()
        stale_future = Future()
        stale_future.set_result(None)
        q._putters.append(("stale", stale_future))
        q.put_nowait("real")

        item = q.get_nowait()

        # Postcondition: expired putter was consumed, real item returned.
        assert item == "real"
        assert not q._putters
        assert q.empty()

    asyncio.run(scenario())
