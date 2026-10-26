# file: project/tornado/queues.py:153-166
# asked: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}
# gained: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}

import collections

import pytest

from tornado.queues import Queue


def test_queue_init_default():
    q = Queue()
    try:
        assert q.maxsize == 0
        assert q._maxsize == 0
        assert q.qsize() == 0
        assert q.empty() is True
        assert q.full() is False
        assert isinstance(q._queue, collections.deque)
        assert list(q._queue) == []
        assert isinstance(q._getters, collections.deque)
        assert list(q._getters) == []
        assert isinstance(q._putters, collections.deque)
        assert list(q._putters) == []
        assert q._unfinished_tasks == 0
        assert q._finished.is_set() is True
    finally:
        q._getters.clear()
        q._putters.clear()
        q._queue.clear()


def test_queue_init_zero_maxsize_unbounded():
    q = Queue(maxsize=0)
    try:
        assert q.maxsize == 0
        assert q._maxsize == 0
        assert q.qsize() == 0
        assert q.empty() is True
        assert q.full() is False
        assert q._unfinished_tasks == 0
        assert q._finished.is_set() is True
        q.put_nowait("item")
        assert q.qsize() == 1
        assert q.empty() is False
        assert q.full() is False
        assert q.get_nowait() == "item"
        q.task_done()
        assert q._unfinished_tasks == 0
    finally:
        q._getters.clear()
        q._putters.clear()
        q._queue.clear()


def test_queue_init_positive_maxsize():
    q = Queue(maxsize=2)
    try:
        assert q.maxsize == 2
        assert q._maxsize == 2
        assert q.qsize() == 0
        assert q.empty() is True
        assert q.full() is False
        assert list(q._getters) == []
        assert list(q._putters) == []
        assert q._unfinished_tasks == 0
        assert q._finished.is_set() is True
        q.put_nowait(1)
        q.put_nowait(2)
        assert q.qsize() == 2
        assert q.full() is True
    finally:
        q._getters.clear()
        q._putters.clear()
        q._queue.clear()


def test_queue_init_none_raises_type_error():
    with pytest.raises(TypeError, match="maxsize can't be None"):
        Queue(maxsize=None)  # type: ignore[arg-type]


@pytest.mark.parametrize("bad_maxsize", [-1, -2, -100])
def test_queue_init_negative_raises_value_error(bad_maxsize):
    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=bad_maxsize)
