# file: project/tornado/queues.py:256-272
# asked: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}
# gained: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}

import pytest
from concurrent.futures import Future as ConcurrentFuture

from tornado.queues import Queue

try:
    from tornado.queues import QueueEmpty
except ImportError:
    from queue import Empty as QueueEmpty


def test_get_nowait_returns_available_item_no_putters():
    q = Queue()
    q.put_nowait(42)
    assert q.qsize() == 1
    assert len(q._putters) == 0
    result = q.get_nowait()
    assert result == 42
    assert q.qsize() == 0
    assert q.empty()


def test_get_nowait_empty_raises():
    q = Queue()
    assert q.empty()
    assert q.qsize() == 0
    assert len(q._putters) == 0
    with pytest.raises(QueueEmpty):
        q.get_nowait()
    assert q.empty()
    assert q.qsize() == 0


def test_get_nowait_consumes_waiting_putter():
    q = Queue(maxsize=1)
    q.put_nowait("first")
    assert q.full()
    assert q.qsize() == 1
    assert len(q._putters) == 0
    putter = ConcurrentFuture()
    assert not putter.done()
    q._putters.append(("second", putter))
    try:
        result = q.get_nowait()
        assert result == "first"
        assert putter.done()
        assert putter.result() is None
        assert len(q._putters) == 0
        assert q.qsize() == 1
        assert q.full()
        second = q.get_nowait()
        assert second == "second"
        assert q.empty()
        assert q.qsize() == 0
    finally:
        q._putters.clear()
