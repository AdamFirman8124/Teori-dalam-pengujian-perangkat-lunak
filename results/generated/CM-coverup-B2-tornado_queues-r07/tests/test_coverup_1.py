# file: project/tornado/queues.py:153-166
# asked: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}
# gained: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}

import collections

import pytest

from tornado.locks import Event
from tornado.queues import Queue


def test_queue_init_rejects_none_maxsize():
    with pytest.raises(TypeError) as exc_info:
        Queue(maxsize=None)
    assert "maxsize can't be None" in str(exc_info.value)


def test_queue_init_rejects_negative_maxsize():
    with pytest.raises(ValueError) as exc_info:
        Queue(maxsize=-1)
    assert "maxsize can't be negative" in str(exc_info.value)


def test_queue_init_invalid_maxsize_does_not_init(monkeypatch):
    calls = []
    monkeypatch.setattr(Queue, "_init", lambda self: calls.append(self))

    with pytest.raises(TypeError):
        Queue(maxsize=None)
    with pytest.raises(ValueError):
        Queue(maxsize=-5)

    assert calls == []


def test_queue_init_sets_initial_state():
    q = Queue()

    assert q.maxsize == 0
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()
    assert isinstance(q._getters, collections.deque)
    assert isinstance(q._putters, collections.deque)
    assert len(q._getters) == 0
    assert len(q._putters) == 0
    assert q._unfinished_tasks == 0
    assert isinstance(q._finished, Event)
    assert q._finished.is_set()


def test_queue_init_with_maxsize_sets_maxsize():
    q = Queue(maxsize=3)

    assert q.maxsize == 3
    assert q.empty()
    assert not q.full()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()


def test_queue_init_calls_init_hook(monkeypatch):
    calls = []
    original_init = Queue._init

    def spy(self):
        calls.append(self)
        return original_init(self)

    monkeypatch.setattr(Queue, "_init", spy)

    q = Queue(maxsize=1)

    assert calls == [q]
    assert q.maxsize == 1
    assert q._finished.is_set()


def test_queue_init_creates_independent_state_per_instance():
    q1 = Queue()
    q2 = Queue()

    assert q1._finished is not q2._finished
    assert q1._getters is not q2._getters
    assert q1._putters is not q2._putters

    q1._finished.clear()
    assert not q1._finished.is_set()
    assert q2._finished.is_set()
