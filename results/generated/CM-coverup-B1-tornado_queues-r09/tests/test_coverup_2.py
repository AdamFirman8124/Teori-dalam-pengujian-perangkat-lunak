# file: project/tornado/queues.py:153-166
# asked: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}
# gained: {"lines": [154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}

import pytest

from tornado.queues import Queue


def test_queue_init_maxsize_none_raises():
    with pytest.raises(TypeError, match="maxsize can't be None"):
        Queue(maxsize=None)


def test_queue_init_negative_maxsize_raises():
    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-1)


def test_queue_init_success_sets_state():
    q = Queue(maxsize=3)
    assert q._maxsize == 3
    assert q.qsize() == 0
    assert q.empty()
    assert not q.full()
    assert len(q._getters) == 0
    assert len(q._putters) == 0
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()


def test_queue_init_default_maxsize():
    q = Queue()
    assert q._maxsize == 0
    assert q._finished.is_set()
