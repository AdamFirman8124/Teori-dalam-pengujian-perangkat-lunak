# file: project/tornado/queues.py:256-272
# asked: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}
# gained: {"lines": [262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}

import collections
import pytest
from unittest.mock import MagicMock
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
    q = Queue(maxsize=1)
    q.put_nowait("first")
    assert q.full()
    assert q.qsize() == 1
    putter_future = MagicMock()
    putter_future.done.return_value = False
    putter_future.cancelled.return_value = False
    q._putters.append(("second", putter_future))
    assert len(q._putters) == 1
    result = q.get_nowait()
    assert result == "first"
    putter_future.set_result.assert_called_once_with(None)
    assert len(q._putters) == 0
    assert q.qsize() == 1
    assert q.full()
    second = q.get_nowait()
    assert second == "second"
    assert q.empty()
    assert q.qsize() == 0
