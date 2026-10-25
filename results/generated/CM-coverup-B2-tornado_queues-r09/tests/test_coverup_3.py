# file: project/tornado/queues.py:256-272
# asked: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}
# gained: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}

import asyncio
import pytest
from tornado.queues import Queue, QueueEmpty


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
    try:
        old_loop = asyncio.get_event_loop()
    except RuntimeError:
        old_loop = None
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        q = Queue(maxsize=1)
        q.put_nowait("first")
        assert q.full()
        assert q.qsize() == 1
        put_fut = q.put("second")
        assert len(q._putters) == 1
        assert not put_fut.done()
        result = q.get_nowait()
        assert result == "first"
        assert put_fut.done()
        assert put_fut.result() is None
        assert len(q._putters) == 0
        assert q.qsize() == 1
        assert q.full()
        second = q.get_nowait()
        assert second == "second"
        assert q.empty()
        assert q.qsize() == 0
    finally:
        try:
            loop.close()
        finally:
            asyncio.set_event_loop(old_loop)
