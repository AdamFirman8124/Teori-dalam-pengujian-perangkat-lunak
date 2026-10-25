# file: project/tornado/queues.py:153-166
# asked: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}
# gained: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}

import collections

import pytest

from tornado.queues import Queue


def test_queue_rejects_none_maxsize():
    with pytest.raises(TypeError, match="maxsize can't be None"):
        Queue(maxsize=None)


def test_queue_rejects_negative_maxsize():
    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-1)


def test_queue_initializes_internal_state():
    queue = Queue(maxsize=2)

    assert queue.maxsize == 2
    assert queue.qsize() == 0
    assert queue.empty()
    assert not queue.full()
    assert isinstance(queue._getters, collections.deque)
    assert isinstance(queue._putters, collections.deque)
    assert not queue._getters
    assert not queue._putters
    assert queue._unfinished_tasks == 0
    assert queue._finished.is_set()
