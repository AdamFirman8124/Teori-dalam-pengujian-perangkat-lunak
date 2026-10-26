# file: project/tornado/queues.py:153-166
# asked: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}
# gained: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}

import collections

import pytest

from tornado.locks import Event
from tornado.queues import Queue


def test_queue_init_default():
    q = Queue()
    assert q._maxsize == 0
    assert q.maxsize == 0
    assert q._unfinished_tasks == 0
    assert isinstance(q._getters, collections.deque)
    assert len(q._getters) == 0
    assert isinstance(q._putters, collections.deque)
    assert len(q._putters) == 0
    assert isinstance(q._finished, Event)
    assert q._finished.is_set()
    assert q.qsize() == 0
    assert q.empty() is True


def test_queue_init_with_positive_maxsize():
    q = Queue(maxsize=5)
    assert q._maxsize == 5
    assert q.maxsize == 5
    assert q._unfinished_tasks == 0
    assert isinstance(q._getters, collections.deque)
    assert len(q._getters) == 0
    assert isinstance(q._putters, collections.deque)
    assert len(q._putters) == 0
    assert isinstance(q._finished, Event)
    assert q._finished.is_set()
    assert q.qsize() == 0
    assert q.empty() is True


def test_queue_init_none_raises():
    with pytest.raises(TypeError, match="maxsize can't be None"):
        Queue(maxsize=None)  # type: ignore[arg-type]


def test_queue_init_negative_raises():
    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-1)
    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-100)
